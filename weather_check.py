#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025-04-23 10:48
# @Author  : CL
# @File    : weather_check.py
# @Description : 
# ---------------------------------------------
import os
import random
from email.message import EmailMessage
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Gmail 配置
GMAIL_USER = "chenliang3111@gmail.com"
GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")  # 使用环境变量读取密码
TO_EMAIL = "chenliang3111@gmail.com"  # 收件人可以同发件人

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = TO_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, TO_EMAIL, msg.as_string())
        server.quit()

        print("📧 邮件发送成功！")
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")

def main():
    print(f"运行时间: {datetime.now()}")
    result = random.randint(0, 100)
    print(f"测试结果: {result}")

    if result < 50:
        message = f"🚨 测试失败：结果为 {result}"
        print("⚠️ 测试不通过，发送通知")
        send_email("❌ 测试失败通知", message)
    else:
        print("✅ 测试通过，无需通知")

if __name__ == "__main__":
    main()
