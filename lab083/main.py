from StarCC import PresetConversion
convert = PresetConversion(src='cn', dst='hk', with_phrase=False)  # change to `dst='tw'` for Taiwan mode
print(convert('阴天，山容便黯澹无聊，半隐入米家的水墨里去。'))
# 陰天，山容便黯澹無聊，半隱入米家的水墨裏去。