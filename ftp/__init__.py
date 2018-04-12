# FTP操作
import ftplib

host = '192.168.20.191'
username = 'ftpuser'
password = 'ftp123'
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
    file_remote = '1.txt'
    file_local = 'D:\\test_data\\ftp_download.txt'
    bufsize = 1024  # 设置缓冲器大小
    fp = open(file_local, 'wb')
    f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
    fp.close()


def ftp_upload():
    '''以二进制形式上传文件'''
    file_remote = 'ftp_upload.txt'
    file_local = 'D:\\test_data\\ftp_upload.txt'
    bufsize = 1024  # 设置缓冲器大小
    fp = open(file_local, 'rb')
    f.storbinary('STOR ' + file_remote, fp, bufsize)
    fp.close()


ftp_download()
ftp_upload()
f.quit()
