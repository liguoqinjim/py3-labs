import tinycss2


def extract_background_images(css_text):
    rules = tinycss2.parse_stylesheet(css_text, skip_comments=True, skip_whitespace=True)
    background_images = {}

    for rule in rules:
        if rule.type == 'qualified-rule':
            # 获取并处理所有选择器
            selectors = ''.join([token.serialize() for token in rule.prelude if token.type != 'whitespace'])
            # 检查选择器是否正确
            if selectors.startswith('.Pet_HatchingPotion_'):
                class_name = selectors[1:]  # 去掉开头的点，获取类名
                # 读取每个属性
                for declaration in rule.content:
                    print("li1")
                    print(declaration.type, declaration.value)
                    if declaration.type == "url":
                        print(declaration.value)
                    print("li2")
                    if declaration.type == 'declaration' and declaration.name == 'background-image':
                        url = ''.join([token.serialize() for token in declaration.value])
                        background_images[class_name] = url  # 存储类名和对应的URL

    return background_images


# 使用示例
css_content = """
.Pet_HatchingPotion_Watery { background-image: url(https://habitica-assets.s3.amazonaws.com/mobileApp/images/Pet_HatchingPotion_Watery.png); width: 68px; height: 68px }
.Pet_HatchingPotion_White { background-image: url(https://habitica-assets.s3.amazonaws.com/mobileApp/images/Pet_HatchingPotion_White.png); width: 68px; height: 68px }
.Pet_HatchingPotion_Zombie { background-image: url(https://habitica-assets.s3.amazonaws.com/mobileApp/images/Pet_HatchingPotion_Zombie.png); width: 68px; height: 68px }
"""

images_info = extract_background_images(css_content)
print(images_info)
