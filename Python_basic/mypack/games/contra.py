# mypack/games/contra.py

def play():
    print("正在玩魂斗罗.....")

import mypack.menu  # 绝对导入

from ..menu import show_menu    # 相对导入

def gameover():
    # mypack.menu.show_menu()     # 绝对调用
    show_menu()                 # 相对调用

print("魂斗罗模块被加载")