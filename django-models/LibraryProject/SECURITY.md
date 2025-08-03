## Security Measures

- DEBUG set to False for production safety.
- CSRF and session cookies secured with HTTPS only.
- CSP headers configured to block unwanted external scripts.
- Views validated with Django ORM and forms to avoid SQL injection.
- CSRF tokens added to all form templates.
