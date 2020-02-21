def testFunc(**kwargs):
	for key, value in kwargs.items():
		print(f"{key} == {value}")

testFunc(firstKey = 'Hi', secondKey = 'I am', thirdKey = 'Happy')
