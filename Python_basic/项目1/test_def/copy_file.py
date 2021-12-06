# -*- coding: utf-8 -*-

# 请输入源文件:
# 请输入目录文件:
# 已复制文件，文件长度是:
def copy_file():
    s = input("请输入源文件:")
    d = input("请输入目标文件:")
    try:
        # 打开文件
        # 打开源文件并读取二进制文件
        open_s = open(s, 'rb')
        try:
            try:
                # 打开目标文件并写入二进制文件
                open_d = open(d, 'wb')

                # 每次复制4kb字节，直到复制完为止
                # 4096 = 4k
                try:
                    while True:
                        # 源文件每次读取x个字节
                        par = open_s.read(4096)
                        if not par:
                            print("文件复制完成")
                            break
                        # 读取x个字节写入目标文件
                        open_d.write(par)
                        # 获取当前文件长度
                        position = open_s.tell()
                        print("已复制文件，文件长度是:", position)
                finally:
                    open_d.close()
            except OSError:
                print('打开', d, '文件失败')
        finally:
            open_s.close()
    except OSError:
        print("打开", s, "文件失败")

if __name__ == '__main__':
    copy_file()