import imaplib
import email
import sys
from email.header import decode_header
import email.utils
from datetime import datetime, timezone

# 邮箱 IMAP 服务器地址
IMAP_SERVER = 'imap.qq.com'
IMAP_PORT = 993  # IMAP 通过 SSL 的端口号

# 用于登录的邮箱地址和授权码
YOUR_EMAIL = sys.argv[1]
YOUR_PASSWORD = sys.argv[2]

# 建立与 IMAP 服务器的连接
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

# 登录邮箱
mail.login(YOUR_EMAIL, YOUR_PASSWORD)

# 选择邮箱中的“收件箱”文件夹，可以根据需要更改
mail.select('inbox')

# 搜索邮件
status, messages = mail.search(None, 'ALL')
if status == 'OK':
    # 将邮件 ID 列表转换成 Python 的列表
    messages = messages[0].split()

    # 遍历邮件 ID 列表，从最新的邮件开始
    for mail_id in messages[::-1]:
        # 获取邮件内容
        status, data = mail.fetch(mail_id, '(RFC822)')
        if status == 'OK':
            # 解析邮件内容
            msg = email.message_from_bytes(data[0][1])

            # 解码邮件主题
            subject, encoding = decode_header(msg['Subject'])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or 'utf-8')

            # 解码发件人邮箱
            from_email = msg.get('From')
            # print(f'From: {from_email}\nSubject: {subject}\n')

            # 获取并打印邮件发送时间
            date = msg.get('Date')

            print(f'From: {from_email}\nSubject: {subject}\nDate: {date}\n')

            # 使用 email.utils.parsedate_to_datetime 解析邮件日期字符串
            mail_date = email.utils.parsedate_to_datetime(date)

            # 将邮件日期转换为本地时区（如果需要）
            mail_date_local = mail_date.astimezone(timezone.utc).replace(tzinfo=None)

            # 获取当前日期（不带时分秒）
            current_date = datetime.now().date()

            # 比较邮件日期和当前日期
            if mail_date_local.date() == current_date:
                print("这封邮件是今天发送的。")
            else:
                print("这封邮件不是今天发送的。")

            # 如果邮件内容是 multipart，遍历邮件的每一部分
            if msg.is_multipart():
                for part in msg.walk():
                    # 获取内容类型
                    content_type = part.get_content_type()
                    content_disposition = str(part.get('Content-Disposition'))

                    # 获取邮件正文内容
                    if content_type == 'text/plain' and 'attachment' not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        print(f'Body:\n{body}\n')
                        break
            else:
                # 邮件内容不是 multipart
                body = msg.get_payload(decode=True).decode()
                print(f'Body:\n{body}\n')

            # 您可以在这里添加代码来处理邮件内容，如保存到文件、数据库等

# 关闭与邮箱的连接和退出
mail.close()
mail.logout()
