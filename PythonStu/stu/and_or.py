#! /usr/bin/python

def and_press():
	print 'a' and 'b'	 	#print 'b'
	
	print '' and 'b' 	 	#print ''

	print 'a' and 'b' and 'c' 	#print 'c'

def or_press():
	print 'a' or 'b'		#print 'a'

	print '' or 'b'			#print 'b'

	print '' or 0 or [] or ()	#print ()

def andor_press():			#= prexx?a:b
	a ="first"
	b ="second"

	print 1 and a or b		#print first
	print 0 and a or b		#print second

	#error at: a =false
	#so 
	a =""
	print "===>"+(1 and [a] or [b])[0]

if  __name__ == "__main__":
	and_press()
	or_press()
	andor_press()
