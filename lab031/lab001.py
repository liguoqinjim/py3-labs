from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

# Create MP3File instance.
mp3 = MP3File("data/lab001.mp3")

# Get all tags.
tags = mp3.get_tags()
print(tags)

# Get/set/del tags value.
alb = mp3.album
print("album=", alb)

mp3.album = '你好'
mp3.artist = '上海'
mp3.song = "第一个Lesson"

# save tag
mp3.save()

# 删除tag
# del mp3.band
