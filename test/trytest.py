def test():
	try:
		i = 1/0
		print "before throw exception"
	except Exception, e:
		print Exception, e
	print "after throw exception...."

test()