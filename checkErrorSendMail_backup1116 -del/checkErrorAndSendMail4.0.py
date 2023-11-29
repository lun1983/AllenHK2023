# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : checkErrorAndSendMail4.0.py
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
import subprocess
import shutil
import sys

# 全局变量

CHECKWORDINGSFILE = './checkwordings.txt'
# LOGFILE = './logfile.txt'
RESULTFILE = './result.txt'
WORK_PATH = ''

ERR_FLG_ALL = ''

MAIL_USER_NAME = 'allenwang'
MAIL_PASS_WORD = 'china_003'


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
    subject = '批量備份 [' + str(datetime.now().strftime("%Y%m%d")) + ']結果'

    mymessage = ('Dear IT-teams:\n\n\tCongratulations! Succesffully Backup ! Details in attachment.\n\n\t'
                 + "All Logs : \\\\nas-2012\\Share\\Backup_log\\" + '\n\n'
                 + str(datetime.now().strftime("%Y%m%d")))
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
    subject = '批量備份 [' + str(datetime.now().strftime("%Y%m%d")) + ']結果'

    mymessage = ('Dear IT-teams:\n\n\tWarnings! Errors found during Backup ! Details in attachment.\n\n\t'
                 + "All Logs : \\\\nas-2012\\Share\\Backup_log\\" + '\n\n'
                 + str(datetime.now().strftime("%Y%m%d")))

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
    print('CHECK: [ ' + myfilepath.ljust(80) + ']')
    error_flg = ''  # 初始化没有错误
    checkword_cnts = {checkword: 0 for checkword in checkwordings}

    WRITE_CONTENTS.append('\n' + 'CHECK: [' + myfilepath.ljust(80) + ' ]\n')

    # with open(myfilepath, 'r', encoding='ISO-8859-1') as file:
    with open(myfilepath, 'r', encoding='utf-16') as file:
        # content = file.read()
        content_lines = file.readlines()
        sum_flg = 'n'
        for content_line in content_lines:
            words = content_line.split()  # 将文件内容以空格分开，存到words列表中
            # 如果关键字中有#则不进行检查
            for word in words:
                if word.lower() in checkword_cnts and '#' not in str(
                        checkword_cnts[word.lower()]) and '0x00000000' not in content_line:
                    # if word.lower() in checkword_cnts and '#' not in str(checkword_cnts[word.lower()]) :
                    checkword_cnts[word.lower()] += 1
                    error_flg = 'y'
            if ('Total' in content_line
                    and 'Copied' in content_line
                    and 'Extras' in content_line
                    and 'Skipped' in content_line
                    and 'Mismatch' in content_line):
                sum_flg = 'y'
            # if 'Times' in content_line:
            #     WRITE_CONTENTS.append(content_line)
            #     sum_flg = 'n'
            if sum_flg == 'y':
                WRITE_CONTENTS.append(content_line.rstrip('\n'))

    for key, cnt in checkword_cnts.items():
        print('KEY_WORD:[' + key.ljust(10) + '],TIMES: ' + str(cnt))
        WRITE_CONTENTS.append('KEY_WORD:[' + key.ljust(10) + '],TIMES: ' + str(cnt))

    return error_flg, WRITE_CONTENTS


def write_result_file(WRITE_CONTENTS):
    with open(RESULTFILE, 'w') as file:
        file.writelines(line + '\n' for line in WRITE_CONTENTS)

    return


def read_config(conf_file):
    tDate = datetime.now().strftime("%Y%m%d")
    with open(conf_file, 'r') as config_file:
        conf_data = json.load(config_file)

        # 取出所有关键字
        CHECKWORDINGS = [d1['checkword'] for d1 in conf_data['checkwordings']]

        # 取出所有的notification的值，这个用法值得学习
        RECEIVER_ADDRS = [d2['email'] for d2 in conf_data['notification']]

        # 取出所有的文件路径
        MYFILE_DIR = conf_data['myfilepaths']

        # txtfile_list = os.listdir(os.getcwd()+'\\'+MYFILE_DIR+'\\'+tDate)
        txtfile_list = os.listdir('./' + MYFILE_DIR + '/' + tDate)
        MYFILE_PATHS = [ifile for ifile in txtfile_list if ifile.endswith('txt')]

        #  取出是否发送邮件标志

        EMAIL_FLAG = conf_data['email_flg']

        # 取出source 和 targt log file路径
        SOURCELOGFILEPATH = conf_data['sourcelogfilepath']
        TARGETLOGFILEPATH = conf_data['targetlogfilepath']

    return CHECKWORDINGS, RECEIVER_ADDRS, MYFILE_PATHS, EMAIL_FLAG, SOURCELOGFILEPATH, TARGETLOGFILEPATH


def main(conf_file):
    sDate = datetime.now().strftime("%Y%m%d")

    # 检查log文件
    CHECKWORDINGS, RECEIVER_ADDRS, MYFILE_PATHS, EMAIL_FLG, SOURCELOGFILEPATH, TARGETLOGFILEPATH = read_config(
        conf_file)
    ERR_FLG_ALL = ''

    # 检查每个在MYFILE_PATHS中的文件，将所有需要写入结果的内容，保存到WRITE_CONTENTS
    WRITE_CONTENTS = ['[START:' + str(datetime.now()) + ' ]']
    for MYFILE_PATH in MYFILE_PATHS:
        prefix_MYFILE_PATH = f'./log/{sDate}/' + MYFILE_PATH
        if not os.path.exists(prefix_MYFILE_PATH):
            print('FILE NOT FOUND: ' + prefix_MYFILE_PATH)
            ERR_FLG_ALL = 'y'
            WRITE_CONTENTS.append('\n' + 'FILE NOT FOUND: ' + MYFILE_PATH + '')
        else:
            error_flg, WRITE_CONTENTS = check_logfile(CHECKWORDINGS, prefix_MYFILE_PATH, WRITE_CONTENTS)
            if error_flg in ('y', 'Y'):
                ERR_FLG_ALL = 'y'

    # 打印汇总信息
    print('EMAIL_FLG : ' + EMAIL_FLG + ' and ERR_FLG : ' + ERR_FLG_ALL)

    if ERR_FLG_ALL == 'y':
        Infox = '\n>>> RESULT:Backup Failed. <<<\n'
    else:
        Infox = '\n>>> RESULT:Backup Successfully. <<<'
    print(Infox)

    # 产生报告
    WRITE_CONTENTS.append(Infox + '[END:' + str(datetime.now()) + ' ]' + '.\n')
    write_result_file(WRITE_CONTENTS)

    # 如果失败，则发送失败邮件；否则发送成功邮件
    if EMAIL_FLG in ('Y', 'y'):
        if ERR_FLG_ALL == 'y':
            send_fail_mail(WRITE_CONTENTS, RECEIVER_ADDRS)
        else:
            send_succ_mail(WRITE_CONTENTS, RECEIVER_ADDRS)

    # 拷贝文件到NAS
    SOURCELOGFILEPATH = SOURCELOGFILEPATH + f'/{sDate}'
    TARGETLOGFILEPATH = TARGETLOGFILEPATH + f'\\{sDate}'
    print(SOURCELOGFILEPATH)
    print(TARGETLOGFILEPATH)
    dosresult = subprocess.run(f'robocopy {SOURCELOGFILEPATH} {TARGETLOGFILEPATH} /E /NP',capture_output=True, text=True, shell=True)
    print(dosresult.stdout)

    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        conf_file = './/' + sys.argv[1]
    else:
        conf_file = './conf.json'

    main(conf_file)
