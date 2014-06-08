import time
import webbrowser


count = 1
while (count < 4):
	time.sleep(10)
	webbrowser.open("http://www.google.com")
	count += 1