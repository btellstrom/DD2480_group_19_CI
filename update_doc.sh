#!/bin/bash

# Requires the pdoc3 package (NOT pdoc, which is an old version !)
# pip install pdoc3

# Generates the documentation in HTML, inside the doc directory.
pdoc --html --overwrite --html-dir doc src
