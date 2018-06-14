#!/usr/bin/python  
# -*- coding: utf-8 -*-  

import os, sys
import paramiko
import threading
import platform

curr_ssh = None
curr_prompt = ">>"


# 使用说明
def printUsage():
    print("    !ls                     :list sessions.")
    print("    !session id             :connect session.")
    print("    !conn host user password:connect host with user.")
    print("    !exit                   :exit.")


# 连接
def conn(ip, username, passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        print("Connect to ", ip, " with ", username)
        global curr_prompt
        curr_prompt = username + "@" + ip + ">>"
        return ssh
    except:
        return None

    # 加载以前的连接信息


sessions = []


def loadSessions():
    global sessions
    try:
        f = open("sessions")
        sessions = f.readlines()
        f.close()
    except:
        pass

    # 执行本地命令,ssh.py的命令


def exe_cmd_local(cmd):
    if (cmd == "!ls"):
        loadSessions()
        global sessions
        i = 0
        print("Sessions:")
        for s in sessions:
            print("[%d] %s" % (i, s))
            i += 1
    else:
        vals = cmd.split(' ')
        if (vals[0] == "!session"):
            id = (int)(vals[1])
            if (id < len(sessions)):
                os_name = platform.system()

                new_console_cmd = ""
                if (os_name == "Linux"):
                    new_console_cmd = "gnome-terminal -e \"./ssh.py " + sessions[id] + "\""
                elif (os_name == "Windows"):
                    new_console_cmd = "start ssh.py " + sessions[id]
                os.system(new_console_cmd)
            else:
                print("Didn't hava sessoin ", vals[1])

        elif (vals[0] == "!conn"):
            global curr_ssh
            curr_ssh = conn(vals[1], vals[2], vals[3])
            f = open("sessions", "a")
            line = vals[1] + " " + vals[2] + " " + vals[3] + "\n"
            f.write(line)
            f.close()

        # 在ssh连接的主机上执行命令


def exe_cmd_ssh(ssh, cmd):
    if (ssh == None):
        print("Didn't connect to a server. Use '!conn' to connect please.")
        return
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdin.write("Y")   #简单交互，输入 ‘Y’
    # 屏幕输出
    # data.decode('utf-8').strip()
    # print((stdout.read().decode('gbk').strip()))
    # print((stderr.read().decode('gbk').strip()))
    print((stdout.read().decode('utf-8').strip()))
    print((stderr.read().decode('utf-8').strip()))


# 入口函数
if __name__ == '__main__':
    loadSessions()
    if (len(sys.argv) == 4):
        curr_ssh = conn(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        printUsage()
    while True:
        cmd = input(curr_prompt)
        if (len(cmd) == 0):
            continue

        if (cmd == "!exit"):
            if (curr_ssh != None):
                curr_ssh.close();
            break
        else:
            if (cmd[0] == '!'):
                exe_cmd_local(cmd)
            else:
                exe_cmd_ssh(curr_ssh, cmd)