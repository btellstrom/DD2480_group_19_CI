## Assignment 2 of the DD2480 course - "Godly robot"
In this assignment we implemented our own CI server, "Godly robot".

## Tech/libraries
<b>Coded in:</b>
- Python3

<b>Libraries used:</b>
- [Python standard library (3.7.2)](https://docs.python.org/3/library/) - collections, math, numpy.
- Pymongo
- Flask
- Pdoc3 (for generating browsable docs)

## What it is
It's an implementation of a CI server using python

## What it does
Compilation is triggered as webhook, the CI server compiles the branch where the change has been made, as specified in the HTTP payload. Our CI server also supports notification of CI results.

## How to use
To enable notification of push events to Godly Robot, in your Github repository settings enable
a webhook for push events only with a URL pointing to where you want to host Godly Robot.

To set up a github repo for usage with out CI server, two files should be added: ci.sh and ci.ini.
ci.sh defines how to do static syntax check/compilation and run the tests for your project. A valid
ci.sh should exit with the following exit codes for the following scenarios:

* 0 - static syntax check/compilation and tests succeeded.
* 1 - static syntax check/compilation succeeds but tests fail.
* 2 - static syntax check/compilation fails.

If ci.sh returns any other exit code Godly Robot will automatically fail the tests. Below is an example
of a valid ci.sh.

```bash
static syntax check
cd DD2480_group_19_CI
python3 -m py_compile src/main/*.py
if [ $? -eq 1 ]
then
	exit 2
fi

# run tests
python3 -m unittest discover src/test/
if [ $? -eq 1 ]
then
	exit 1
fi

# everything is fine
exit 0
```

A minimal ci.ini should specify a github API token. A ci.ini complete with history should also
specify a mongoDB database, as in the example below:

```ini
[Notification]
# The api-token to be used by the CI-service
api_token =

[Database]
# The name of the database to be used dfault CI-History
name = CI-History
# The ip-address of the database
ip =
# The port number of the database, default mongodb is 27017
port = 27017
# The username to the database
user =
# The password to the database
password =
```

## Setting up mongoDB
For Godly Robot to create a history of past builds, it needs to
interact with a mongodb, and to do this one needs to create a database
as well as a user for the database.

Simply install mongoDB, create a database of your choice, for example
`ci-service` and in it create a user along with a password. The
database name, username and password must then be specified in the
`ci.ini` file along with the port number and ip-address of the
mongodb. Again, as shown in the example above.


## Running Godly Robot
To start Godly Robot, in the root folder run:
```Python
$ python3 src/main/app.py
```

To run tests:
```Python
$ python3 -m unittest discover src/test/
```
## Unittesting of compilation/syntax checking and testing
The actual compilation/syntax check and the execution of tests is itself not unittested, as this
is up to the user to define in their own ci.sh script. We do however test that the part of our code
reponsible for executing ci.sh, namely repo_tester.py, behaves consistently and correctly even for
malformed repos, and that the cloned repo is removed every time. For this, we have a collection of
example JSON push events for another repo, called `demo_repo`.

## Unittesting of notifications


## Browsable docs
To generate browsable documentation, simply run:
```
sh update_doc.sh
```
This generates the file:
```
doc/src/index.html
```

## Authors & Statement of contributions
The code architecture was a remarkable collaborative effort, of which we are proud.

**Benjamin Tellstrom** - config parser, history with mongoDB, setting up an actual machine for the ci service  
**Henrik Glass** - repotester, ci.sh, readme
**Florian Singer** - Front end for build history, browsable documentation  
**Ali Yassiry** - app.py skeleton, notifications  
**Peter Mastnak** - readme, html template  
