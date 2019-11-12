from captcha.image import ImageCaptcha

# 指定字体
# image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])
image = ImageCaptcha()

data = image.generate('1234')
image.write('1234', 'out.png')
