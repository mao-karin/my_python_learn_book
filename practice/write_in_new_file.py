#prints "hello World" in a text file
new_file= open("new_file_created.txt","w")
new_file.write("Hello World")
new_file.close()