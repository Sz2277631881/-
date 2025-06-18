import os
import sys


def create_shortcut(target, shortcut_name):
    # 获取桌面路径
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    # 创建.bat文件路径
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.bat")

    # 写入.bat文件内容
    bat_content = f'@echo off\npython "{os.path.abspath(target)}"\npause'
    with open(shortcut_path, 'w') as f:
        f.write(bat_content)
    print(f"快捷方式已创建到桌面: {shortcut_path}")


# 使用示例 - 替换为您的实际文件路径
create_shortcut('jiance.py', 'YOLOv8检测器')