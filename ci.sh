# static syntax check
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

