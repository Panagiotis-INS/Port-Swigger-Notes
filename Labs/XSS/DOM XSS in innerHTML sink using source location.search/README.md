# Lab: DOM XSS in innerHTML sink using source location.search

URL: https://0a8f00620393d837801f0d2000c00055.web-security-academy.net/

![](./Images/img1.png)

## Testing the fields:

![](./Images/img2.png)

## Exploitation:

![](./Images/img3.png)

![](./Images/img4.png)

Payload:

```
<img src=X onerror=alert("XSS")>
```