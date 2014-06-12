def read_text():
	quotes = open("/media/anjan/Media/KodeWork/Python/Moocs/Udacity_036_OOP/assests/movie_quotes.txt")
	contents_of_file = quotes.read()
	print (contents_of_file)
	quotes.close()
	
read_text()
