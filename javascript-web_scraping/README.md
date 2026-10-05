# JavaScript - Web Scraping

This project covers the basics of web scraping and working with APIs in JavaScript using Node.js. I learned how to read/write files, make HTTP requests, and parse JSON responses from REST APIs.

## What I learned

- How to read and write files using the `fs` module
- How to make HTTP requests with the `request` module
- How to work with JSON data from APIs
- How to use command line arguments in Node.js scripts
- How to handle errors with callbacks

## Files

| File | Description |
|------|-------------|
| `0-readme.js` | Reads and prints the content of a file |
| `1-writeme.js` | Writes a string to a file |
| `2-statuscode.js` | Prints the status code of a GET request |
| `3-starwars_title.js` | Prints a Star Wars movie title by episode number |
| `4-starwars_count.js` | Counts movies where Wedge Antilles appears |
| `5-request_store.js` | Downloads a webpage and saves it to a file |
| `6-completed_tasks.js` | Counts completed tasks per user from an API |

## Requirements

- Ubuntu 14.04 LTS, Node.js 10.14.x
- Code follows semistandard style
- Uses the `request` module for HTTP calls
- No use of `var`

## How to run

```bash
./0-readme.js myfile.txt
./2-statuscode.js https://example.com
./3-starwars_title.js 1
```
