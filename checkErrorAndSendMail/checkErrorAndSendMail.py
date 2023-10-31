# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : checkErrorAndSendMail.py
# Time       ：29/9/2023 13:26
# Author     ：Allen Wong
# version    ：python 3.10
# Description：
"""

import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# 全局变量

CHECKWORDINGSFILE = './checkwordings.txt'
# LOGFILE = './logfile.txt'
RESULTFILE = './result.txt'
WORK_PATH=''
conf_file = './conf.json'
ERR_FLG_ALL = ''

MAIL_USER_NAME=''
MAIL_PASS_WORD=''


def send_mail(sender_mail, receiver_mail, subject, mymessage, smtp_server, smtp_port, user, pswd):
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_mail
    msg['To'] = ';'.join(receiver_mail)
    # 正文
    part = MIMEText(mymessage, "plain", 'UTF-8')
    msg.attach(part)

    # 附件处理
    attachment_file = RESULTFILE
    msg["Accept-Charset"] = 'utf-8'
    att = MIMEApplication(open(attachment_file, 'rb').read(), 'utf-8')  # 读取附件
    att.add_header('Content-Disposition', 'attachment', filename=' check_result.txt')
    msg.attach(att)

    # 建立SMTP链接
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(user=user, password=pswd)

        # send mail
        server.send_message(msg)

    return


def send_succ_mail(WRITE_CONTENTS, RECEIVER_ADDRS):
    # mail sender and receivers info
    sender_mail = 'it-info@cbic.hk'
    receiver_mail = RECEIVER_ADDRS
    subject = 'BACKUP SUCCESFFULY AT:' + str(datetime.now())

    # mymessage = '***** Successful Message *****\n'

    mymessage = '\n'.join(WRITE_CONTENTS)

    # mail server info
    smtp_server = 'mail.cbic.hk'
    smtp_port = 587

    # user and pswd
    user = MAIL_USER_NAME
    pswd = MAIL_PASS_WORD

    send_mail(sender_mail, receiver_mail, subject, mymessage, smtp_server, smtp_port, user, pswd)

    return


def send_fail_mail(WRITE_CONTENTS, RECEIVER_ADDRS):
    # mail sender and receivers info
    sender_mail = 'it-info@cbic.hk'
    receiver_mail = RECEIVER_ADDRS
    subject = 'BACKUP FAILED AT:' + str(datetime.now())
    # mymessage = '***** Failed Message *****\n'

    mymessage = '\n'.join(WRITE_CONTENTS)

    # mail server info
    smtp_server = 'mail.cbic.hk'
    smtp_port = 587

    # user and pswd
    user = MAIL_USER_NAME
    pswd = MAIL_PASS_WORD

    send_mail(sender_mail, receiver_mail, subject, mymessage, smtp_server, smtp_port, user, pswd)

    return


# 检查logfile文件中是否有关键字
def check_logfile(checkwordings, myfilepath, WRITE_CONTENTS):
    print('***** NOW CHECKING *****' + myfilepath + ' ENCODING: ISO-8859-1')
    error_flg = ''  # 初始化没有错误
    checkword_cnts = {checkword: 0 for checkword in checkwordings}

    WRITE_CONTENTS.append('\n' + '***** NOW CHECKING :' + myfilepath + '***** \n')

    with open(myfilepath, 'r', encoding='ISO-8859-1') as file:
        content = file.read()

        words = content.split()  # 将文件内容以空格分开，存到words列表中

        # 如果关键字中有#则不进行检查
        for word in words:
            if word.lower() in checkword_cnts and '#' not in word:
                checkword_cnts[word.lower()] += 1
                error_flg = 'y'

    for key, cnt in checkword_cnts.items():
        print(f'{key}:{cnt} times')
        WRITE_CONTENTS.append(key + ' : ' + str(cnt))
    # return checkword_cnts, error_flg, WRITE_CONTENTS
    return error_flg, WRITE_CONTENTS


def write_result_file(WRITE_CONTENTS):
    with open(RESULTFILE, 'w') as file:
        file.writelines(line + '\n' for line in WRITE_CONTENTS)

    return


def read_config():
    
    with open(conf_file, 'r') as config_file:
        conf_data = json.load(config_file)

        # 取出所有关键字
        CHECKWORDINGS = [d1['checkword'] for d1 in conf_data['checkwordings']]

        # 取出所有的notification的值，这个用法值得学习
        RECEIVER_ADDRS = [d2['email'] for d2 in conf_data['notification']]

        # 取出所有的文件路径
        MYFILE_PATHS = [d3['myfilepath'] for d3 in conf_data['myfilepaths']]

        #  取出是否发送邮件标志

        EMAIL_FLAG = conf_data['email_flg']

        print(MYFILE_PATHS)

    return CHECKWORDINGS, RECEIVER_ADDRS, MYFILE_PATHS, EMAIL_FLAG


def main():
    print('START:' + str(datetime.now()))

    # 检查log文件
    CHECKWORDINGS, RECEIVER_ADDRS, MYFILE_PATHS, EMAIL_FLG = read_config()
    ERR_FLG_ALL = ''
    # 检查每个在MYFILE_PATHS中的文件，将所有需要写入结果的内容，保存到WRITE_CONTENTS
    WRITE_CONTENTS = ['START AT:' + str(datetime.now())]
    for MYFILE_PATH in MYFILE_PATHS:
        if not os.path.exists(MYFILE_PATH):
            print('FILE NOT FOUND: ' + MYFILE_PATH)
            ERR_FLG_ALL = 'y'
            WRITE_CONTENTS.append('\n' + '<<<<<FILE NOT FOUND: ' + MYFILE_PATH + '>>>>>')
        else:
            error_flg, WRITE_CONTENTS = check_logfile(CHECKWORDINGS, MYFILE_PATH, WRITE_CONTENTS)
            if error_flg in ('y', 'Y'):
                ERR_FLG_ALL = 'y'

    # 打印汇总信息
    print('EMAIL_FLG : ' + EMAIL_FLG + ' and ERR_FLG : ' + ERR_FLG_ALL)
    if ERR_FLG_ALL == 'y':
        Infox = '\n<<<<<Backup Failed.>>>>>'
    else:
        Infox = '\n<<<<<Backup Successfully.>>>>>'
    print(Infox)

    # 产生报告
    WRITE_CONTENTS.append(Infox + '\n' + 'END AT:' + str(datetime.now()) + '.\n')
    write_result_file(WRITE_CONTENTS)

    # 如果失败，则发送失败邮件；否则发送成功邮件
    if EMAIL_FLG in ('Y', 'y'):
        if ERR_FLG_ALL == 'y':
            send_fail_mail(WRITE_CONTENTS, RECEIVER_ADDRS)
        else:
            send_succ_mail(WRITE_CONTENTS, RECEIVER_ADDRS)

    print('END:' + str(datetime.now()))

    return


if __name__ == "__main__":
    main()
