#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""
import requests
import sys


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
