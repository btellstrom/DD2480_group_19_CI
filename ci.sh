# static syntax check
python3 -m py_compile src/main/*.py
if [ $? -eq 1 ]
then
	exit 2
fi

# run tests
cd src
python3 -m unittest discover test/
if [ $? -eq 1 ]
then
	exit 1
fi

# everything is fine
exit 0

