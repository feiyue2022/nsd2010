#cp命令
import sys
def copy(src_fname,dst_fname):
    #创建两个变量，src_fname 存储源文件路径；dst_fname 存储目标文件路径
    # src_fname = 'D:\2.JPG'
    # dst_fname = 'D:\3.JPG'
    #创建两个对象变量，src_fobj为打开原文件；src_fobj为打开目标文件
    #因为是二进制文件，以字节的方式进行读写
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')
    while 1:          #不确定读取次数，采用while循环
        data = src_fobj.read(4096)     #每次从元文件中读取4k
        #if len(data) == 0:            #data为0,代表指针指向末尾，数据读完
        #if data == b'':               #b''空字节，代表指针指向末尾
        if not data:                   #data为非空值，中断循环
            break                      #退出整个while循环
        dst_fobj.write(data)        #将data数据写入list2文件中

    src_fobj.close()     #关闭原文件/usr/bin/ls
    dst_fobj.close()     #关闭目标文件 /tmp/lists
copy(sys.argv[1],sys.argv[2])