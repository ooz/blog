---
title: P. De Ryck: Common API Security Pitfalls
date: 2022-06-07T20:33:04Z
---

This list is a compiled from the [Devoxx Belgium 2017 talk](https://www.youtube.com/watch?v=YQzU8xEBiPg).

## Pitfalls

(read: don't do this!)

### 1. "Allowing access to your API over HTTP"

* don't support redirect from HTTP to HTTPS, use HSTS
* Configure **HTTP Strict Transport Security (HSTS)** to prevent falling back to HTTP (this will tell the browser to use HTTPS for every request)
* Strict-Transport-Security: max-age=31536000

### 2. "Not rate limiting calls to your API"

Possible strategies:

* Limit per connection (IP address)
* Limit per user (account, token, key)
* Limit per application property (account, resource)
* Limit based on context (region, app type)

Use HTTP 429 Too Many Requests
and Retry-After: 3600

### 3. "Using insecure direct object references"

-> always combine basic authentication check with authorization checks (resource ownership)

### 4. "Mishandling client-side session data"

* Server-side sessions share an ID with the client and store data on the server
  -> Attacks on session management (guessing or stealing the ID)
  -> The data stored with the server-side session can be considered trusted
* Client-side sessions are a completely different paradigm
  * Data is stored on the client, so it can easily be accessed
  * Data comes from the client, so it is untrusted by default
* Client-side sessions require additional data protection measures
  * Mandatory integrity checks to detect data tempering
  * Optional confidentiality mechanisms to prevent information disclosure

-> Client-side session data can be read and manipulated, so you need to ensure confidentiality and integrity

### 5. "Not verifying the integrity of your JWTs"

* JWT spec supports signing and encryption. Default mode is signing

-> Only use JWT libraries that verify its integrity (esp. in the backend)

### 6. "Using the wrong signature scheme on JWTs"

* Sign tokens with a private key, distribute the public key for verification by clients

-> Use shared secrets for verifying JWTs only within your app boundaries. Otherwise use a public/private key pair

### 7. "Not propagating identity information"

Pass all relevant identity information to downstream services to enable them to do authorization decisions and to create an audit trail!

### 8. "Minimizing the impact of the transport mechanism"

* Cookies enable CSRF, but are attached to all requests
* Authorization header seems easier at first, but you need to be sure where to store the data in the client
* Cookies are hard to get right for non-web apps, authorization header is easier to use there

-> understand pros/cons of cookies vs. authorization header for your app

### 9. "Underestimating the importance of CSRF"

* Again, only a problem if you use cookies, because browser automatically attaches them to outgoing requests
* Traditional defense: hidden form tokens, not applicable in API context. Can be replicated with a custom header
* CSRF is less relevant for JSON APIs, since GET/form POST will have a different content type
* APIs using other mechanism than form POST/GET, CORS security policy applies

### 10. "Insecure CORS configuration / implementation"

Common misconfigurations:

* Partial match against origin header
* Allowing `null` origin
* Only checking domain, not entire origin (incl. HTTPS)
* Reflecting back `Origin` header (= API is wide open for anyone)

-> don't allow more access than necessary!

### 11. "Lack of input validation"

Best practices:

* Only accept content types you expect, reject everything else
* Validate each input field against its expected data type
* Have length validation in place, set upper bounds
* Use a secure parser for inputs

### 12. "Relying on input validation"

## Question Everything

* How is this different from what we used to do?
* Do we really understand what we are doing?
* Have we validated the integrity and format of that data?

