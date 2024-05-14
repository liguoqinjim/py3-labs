import os
import time

from tqdm import tqdm
import requests
import tinycss2


def parse_css(file_path):
    # 读取CSS文件
    with open(file_path, 'r') as f:
        css_text = f.read()

    # 解析CSS
    rules = tinycss2.parse_stylesheet(css_text, skip_comments=True, skip_whitespace=True)

    # 存储结果的字典
    class_definitions = {}

    # 遍历所有规则
    for rule in rules:
        if rule.type == 'qualified-rule':
            # 获取选择器文本
            selectors = ''.join([token.serialize() for token in rule.prelude if token.type != 'whitespace'])
            # 处理每个选择器
            for selector in selectors.split(','):
                selector = selector.strip()
                if selector.startswith('.'):  # 检查是否为类选择器
                    class_name = selector[1:]  # 获取类名
                    properties = {}
                    # 读取每个属性
                    for declaration in rule.content:
                        if declaration.type == 'declaration':
                            property_name = declaration.name
                            property_value = ''.join([token.serialize() for token in declaration.value])
                            properties[property_name] = property_value
                    # 将属性添加到字典
                    class_definitions[class_name] = properties

    return class_definitions


def extract_background_images(file_path):
    with open(file_path, 'r') as f:
        css_text = f.read()

    rules = tinycss2.parse_stylesheet(css_text, skip_comments=True, skip_whitespace=True)
    background_images = {}

    # 添加调试输出
    for rule in rules:
        if rule.type == 'qualified-rule':
            # 获取并处理所有选择器
            selectors = ''.join([token.serialize() for token in rule.prelude if token.type != 'whitespace'])
            # 检查选择器是否正确
            class_name = selectors[1:]  # 去掉开头的点，获取类名

            # 判断是否为需要的class
            need_class_keywords = ['Pet_', 'Mount_Icon_', 'weapon_', "slim_", "shop_", "icon_"]
            # if not any(keyword in class_name for keyword in need_class_keywords):
            #     continue

            # 读取每个属性
            for declaration in rule.content:
                if declaration.type == "url":
                    if "data:image/png;base64" in declaration.value or "/static/img" in declaration.value:
                        continue

                    background_images[class_name] = declaration.value

    return background_images


def create_html_table(data_dict, output_file, base_path):
    """创建HTML表格，显示本地图片路径"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Table</title>
        <style>
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <th>Index</th>
                <th>Class Name</th>
                <th>Image</th>
            </tr>
    """

    # 确保目录存在
    os.makedirs(base_path, exist_ok=True)

    for index, (key, value) in tqdm(enumerate(data_dict.items(), start=1), total=len(data_dict)):
        if value.endswith('.png') or value.endswith('.jpg') or value.endswith('.gif'):
            # 定义文件路径
            file_name = os.path.basename(value)
            local_path = os.path.join(base_path, file_name)
            # 下载并保存图片
            is_saved = download_image(value, local_path)
            if not is_saved:
                continue
            # 更新HTML用本地路径
            # img_src = local_path
            img_src = local_path.replace("data/", "")
        else:
            img_src = value  # 如果不是PNG，使用原始URL

        html_content += f"""
            <tr>
                <td>{index}</td>
                <td>{key}</td>
                <td><img src="{img_src}" alt="{key}" style="width:100px; height:auto;"></td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"HTML file '{output_file}' has been created.")


def download_image(url, file_path):
    """下载图片并保存到指定路径"""
    if os.path.exists(file_path):
        return True

    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # 确保请求成功
            with open(file_path, 'wb') as f:
                f.write(response.content)
                return True
        except Exception as e:
            if attempt < max_attempts - 1:  # i.e. if it's not the last attempt
                time.sleep(1)  # Wait for a second before retrying
                continue
            else:
                print("Error:", e)

    return False


def create_pet_table(data_dict, output_file, base_path, pet_names):
    """创建HTML表格，显示本地图片路径"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Table</title>
        <style>
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <th>Index</th>
                <th>Class Name</th>
                <th>Image</th>
            </tr>
    """

    # 确保目录存在
    os.makedirs(base_path, exist_ok=True)

    # 遍历pet_names，同一个pet放在一行里面
    for index, pet_name in enumerate(pet_names, start=1):
        html_content += f"""
            <tr>
                <td>{index}</td>
                <td>{pet_name}</td>
                <td>
        """

        for key, value in data_dict.items():
            kw = f"Pet-{pet_name}"

            if kw in key:
                if value.endswith('.png') or value.endswith('.jpg') or value.endswith('.gif'):
                    # 定义文件路径
                    file_name = os.path.basename(value)
                    local_path = os.path.join(base_path, file_name)
                    # 下载并保存图片
                    is_saved = download_image(value, local_path)
                    if not is_saved:
                        continue
                    # 更新HTML用本地路径
                    # img_src = local_path
                    img_src = local_path.replace("data/", "")
                else:
                    img_src = value  # 如果不是PNG，使用原始URL

                html_content += f"""
                    <img src="{img_src}" title="{key}" alt="{key}" style="width:100px; height:auto;">
                """

        html_content += """
                </td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"HTML file '{output_file}' has been created.")


def create_mount_table(data_dict, output_file, base_path, monut_names):
    """创建HTML表格，显示本地图片路径"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Table</title>
        <style>
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <th>Index</th>
                <th>Class Name</th>
                <th>Image</th>
            </tr>
    """

    # 确保目录存在
    os.makedirs(base_path, exist_ok=True)

    # 遍历pet_names，同一个pet放在一行里面
    for index, mount_name in enumerate(monut_names, start=1):
        html_content += f"""
            <tr>
                <td>{index}</td>
                <td>{mount_name}</td>
                <td>
        """

        for key, value in data_dict.items():
            kw1 = f"Mount_Head_{mount_name}"
            kw2 = f"Mount_Body_{mount_name}"

            if kw1 in key or kw2 in key:
                if value.endswith('.png') or value.endswith('.jpg') or value.endswith('.gif'):
                    # 定义文件路径
                    file_name = os.path.basename(value)
                    local_path = os.path.join(base_path, file_name)
                    # 下载并保存图片
                    is_saved = download_image(value, local_path)
                    if not is_saved:
                        continue
                    # 更新HTML用本地路径
                    # img_src = local_path
                    img_src = local_path.replace("data/", "")
                else:
                    img_src = value  # 如果不是PNG，使用原始URL

                html_content += f"""
                    <img src="{img_src}" title="{key}" alt="{key}" style="width:100px; height:auto;">
                """

        html_content += """
                </td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"HTML file '{output_file}' has been created.")


if __name__ == '__main__':
    # 使用示例
    css_file_path = 'data/app.764222e3.css'
    # class_info = parse_css(css_file_path)
    # print(class_info)

    images_info = extract_background_images(css_file_path)
    # 打印所有key
    for key in images_info:
        print(key)
    # 保留3个key
    # images_info = {key: images_info[key] for key in list(images_info.keys())[:3]}
    # create_html_table(images_info, 'data/output.html', 'data/images')

    # 宠物
    pets = {}
    for key in images_info:
        if key.startswith("Pet-"):
            pet_name = key.split("-")[1]
            pets[pet_name] = 1
    pet_names = list(pets.keys())
    # pet_names = pet_names[:2]

    # print(pets)
    create_pet_table(images_info, 'data/pets.html', 'data/images', pet_names)

    # 坐骑
    mounts = {}
    for key in images_info:
        if key.startswith("Mount_Head"):
            mount_name = key.split("-")[0].split("_")[-1]
            mounts[mount_name] = 1
    mount_names = list(mounts.keys())
    # mount_names = mount_names[:2]
    create_mount_table(images_info, 'data/mounts.html', 'data/images', mount_names)

    # 背景
    backgrounds_info = {key: images_info[key] for key in images_info if key.startswith("background_")}
    create_html_table(backgrounds_info, 'data/backgrounds.html', 'data/images')
