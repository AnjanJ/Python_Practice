#Write a program to use any built in function, I choose list.
def read_text():
	quotes = open("/media/anjan/Media/KodeWork/Python/Moocs/Udacity_036_OOP/assests/movie_quotes.txt")
	contents_of_file = quotes.read()
	print (contents_of_file)
	var=list((contents_of_file)) 
	quotes.close()
	count = 0
	for i in var:
		if i in 'AEIOUaeiou':
			count += 1
	print("No of vowels in given text file is " +str(count))
read_text()
