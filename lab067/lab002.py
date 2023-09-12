import json

if __name__ == '__main__':
    # 读取文件
    with open("temp/ocr_result.json", "r") as f:
        ocr_result = json.load(f)

    # 根据位置信息和宽度来添加换行符
    full_text = ""
    for i, word_info in enumerate(ocr_result["words_result"]):
        text = word_info["words"]
        if i > 0:
            # 如果不是第一个文本块，检查是否需要换行
            prev_top = ocr_result["words_result"][i - 1]["location"]["top"]
            current_top = word_info["location"]["top"]
            if current_top - prev_top > 10:
                full_text += "\n"
        full_text += text

    print(full_text)
