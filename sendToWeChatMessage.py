# -*- coding: UTF-8 -*-
import requests


def send_message(epoch, name, message):
    content = f"实验 {name} 进行到 epochs:{epoch}, 当前结果:\n{message}"
    headers = {
        "Authorization":
            "Your Token"  # 这里填写你的Token
    }

    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/send",
                         json={
                             "title": "实验进度提醒",
                             "name": f"{name}实验",
                             "content": content
                         }, headers=headers)
    print(resp.content.decode())


def send_error(name):
    headers = {
        "Authorization":
            "Your Token"  # 这里填写你的Token
    }

    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/send",
                         json={
                             "title": "实验异常提醒",
                             "name": f"{name}实验",
                             "content": "实验出现错误"
                         }, headers=headers)
    print(resp.content.decode())


def send_stop(name, message):
    content = f"实验 {name} 结束, best结果为:{message}"
    headers = {
        "Authorization":
            "Your Token"  # 这里填写你的Token
    }

    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/send",
                         json={
                             "title": "实验结束提醒",
                             "name": f"{name}实验",
                             "content": content
                         }, headers=headers)
    print(resp.content.decode())
