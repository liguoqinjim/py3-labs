import imaplib
import sys

email = sys.argv[1]
password = sys.argv[2]  # 是QQ邮箱的授权码，不是QQ密码

# 连接服务器
imap_server = imaplib.IMAP4_SSL("imap.qq.com")

# 登录邮箱
imap_server.login(email, password)

# 选择邮箱文件夹
imap_server.select("INBOX")

# 搜索邮件
status, data = imap_server.search(None, "ALL")
email_ids = data[0].split()
print("邮件列表：", email_ids)

# 获取邮件列表
for email_id in email_ids:
    status, data = imap_server.fetch(email_id, "(RFC822)")
    email_data = data[0][1]
    # 处理邮件内容
    print("邮件内容：", email_data)

    break
