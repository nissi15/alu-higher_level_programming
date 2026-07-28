#!/bin/bash
# Sends a GET request with a user id header and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" -H "X-ALU-User-Id: 98" "$1"
