import os
def rename_files():
	file_list = os.listdir("/media/anjan/Media/Mooc/Udacity-OOP/assests")
	print (file_list)
	saved_path = os.getcwd()
	os.chdir("/media/anjan/Media/Mooc/Udacity-OOP/assests")
	for file_name in file_list:
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))

	os.chdir(saved_path)
rename_files()