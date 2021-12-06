import mypack   # 导入mypack包
import mypack.games # 导入mypack里的games子包
import mypack.menu  # 导入mypack里的menu模块
import mypack.games.contra  # 导入mypack/games子包的contra模块
from mypack.games.supermario import play   # 导入mypack/games子包的supermari模块中的play函数

play()
mypack.games.contra.play()  # 调用mypack/games子包的contra模块的play函数
mypack.menu.show_menu()   # 的menu.py中show_menu函数
print("程序结束")




