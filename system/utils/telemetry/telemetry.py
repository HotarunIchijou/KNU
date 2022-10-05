from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from cpuinfo import get_cpu_info
from psutil import virtual_memory
from socket import gethostname, gethostbyname
from hashlib import sha224
from system.utils import logtosys
from os import environ

with open('system/utils/telemetry/env', 'r') as f:
    l = f.readline()
    try:
        environ[l[:l.find("=")]] = l[l.find("=") + 1:]
    except ValueError:
        print("Value not defined")

Auth = environ['Auth']
Token = VkApi(token = Auth)

session = Token

def SendMsg(user_id, message):
    session.method("messages.send", {
    "user_id": user_id,
    "message": message,
    "random_id": 0
    })

def SendTelemetry():
    CPU = get_cpu_info()["brand_raw"]
    RAM = str(int(virtual_memory().total / (1024 ** 2)))
    sender = 556568857
    SendMsg(sender, """New login to os:
                       Name = """ + logtosys.logintosys.login + """
                       Hostname = """ + gethostname() + """
                       Localhost = """ + gethostbyname(gethostname()) + """
                       CPU = """ + CPU + """
                       RAM = """ + RAM + "Mb")

SendTelemetry()
