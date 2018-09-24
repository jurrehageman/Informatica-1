file_name = "input2.txt"

file_object = open(file_name, "a")
#text = input("Please provide a message to save to file: ")
#text = "test"
print(text, file=file_object)
print("content saved to the file", file_name)
file_object.close()
