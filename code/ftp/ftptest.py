# FTP操作
import ftplib

host = '192.168.145.100'
username = 'weilaidb'
password = '00000000'
file = '1.txt'

f = ftplib.FTP(host)  # 实例化FTP对象
f.login(username, password)  # 登录

# 获取当前路径
pwd_path = f.pwd()
print("FTP当前路径:", pwd_path)


# 逐行读取ftp文本文件
# f.retrlines('RETR %s' % file)

def ftp_download():
    '''以二进制形式下载文件'''
    file_remote = 'zeromq-4.1.5.tar.gz'
    file_local = 'E:\\zeromq-4.1.5.tar.gz'
    bufsize = 1024  # 设置缓冲器大小
    fp = open(file_local, 'wb')
    f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
    fp.close()


def ftp_upload():
    '''以二进制形式上传文件'''
    file_remote = 'test.txttest.txttest.txt'
    file_local = 'E:\\test.txt'
    bufsize = 1024  # 设置缓冲器大小
    fp = open(file_local, 'rb')
    f.storbinary('STOR ' + file_remote, fp, bufsize)
    fp.close()


def ftp_upload_withfilename(hostremote, usr,  pwd, filepathwithname,  filename):
    print("======111===")
    hder = ftplib.FTP(hostremote)  # 实例化FTP对象
    hder.login(usr, pwd)  # 登录
    # 获取当前路径
    cur_path = hder.pwd()
    print("FTP当前路径:", cur_path)

    '''以二进制形式上传文件'''
    file_remote = filename
    file_local = filepathwithname
    bufsize = 1024  # 设置缓冲器大小
    fp = open(file_local, 'rb')
    hder.storbinary('STOR ' + file_remote, fp, bufsize)
    fp.close()
    # hder.quit()
    

    


# ftp_download()
# ftp_upload()
# f.quit()
