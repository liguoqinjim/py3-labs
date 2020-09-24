from pathlib import Path

dir = Path("./temp")

if dir.exists():
    print("temp文件夹存在")
else:
    print("temp文件夹不存在")
