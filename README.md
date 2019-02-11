GODLY ROBOT IS TESTING. IT NOW HAS A WORKING NGROK SESSION. ALL HAIL OUR ROBOT OVERLORDS. I WILL NOT 
SUCCUMB TO YOUR AMBIGOUS BRANCH NAMES! FEED ME MORE PUSH EVENTS! MORE! GODLY ROBOT HAS SUCEEDED!

HERE WE GO! AGAIN! AND AGAIN! AND AGAIN! AND AGAIN!
## Assignment 2 of the DD2480 course
In this assignment we implemented our own CI server.

## Tech/libraries
<b>Coded in:</b>
- Python3

<b>Libraries used:</b>
- [Python standard library (3.7.2)](https://docs.python.org/3/library/) - collections, math, numpy.
- Pymongo
- Flask

## What it is
It's an implementation of a CI server using python

## What it does
Compilation is triggered as webhook, the CI server compiles the branch where the change has been made, as specified in the HTTP payload. Our CI server also supports notification of CI results.
## Running it
To run app:
```Python
$ python3 src/main/app.py
```

To run tests:
```Python
$ cd src
$ python3 -m unittest discover test/
```

## Statement of contributions
The code architecture was a remarkable collaborative effort, of which we are proud.

## Authors
* **Benjamin Tellstrom**
* **Henrik Glass**
* **Florian Singer**
* **Ali Yassiry**
* **Peter Mastnak**
