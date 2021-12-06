# 此示例示意with语句的用法

src_file = input('请输入源文件:')
dst_file = input('请输入目标文件:')
try:
    with open(src_file, 'rb') as src, open(dst_file, 'wb') as dst:
        while True:
            b = src.read(4096)
            if not b:
                print('复制完成')
                break
            dst.write(b)
            position = src.tell()
            print('当前长度为:', position)
except:
    print('复制失败')
# try:
#     src_file = input('请输入源文件:')
#     with open(src_file, 'rb') as src:
#         try:
#             dst_file = input('请输入目标文件:')
#             with open(dst_file, 'wb') as dst:
#                 # 读取源文件
#                 while True:
#                     b = src.read(4096)
#                     if not b:
#                         print('文件复制完成')
#                         break
#                     dst.write(b)
#                     position = src.tell()
#                     print('当前长度为:', position)
#         except OSError:
#             print('打开目标文件失败')
# except OSError:
#     print('打开源文件失败')

