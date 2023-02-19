


#1. 'with' makes sure the file is closed after we're done with it.
#2. 'open' opens the file and returns a file object.
#3. 'r' is a mode, which means we want to read the file.
#4. 'encoding' is optional and it's set to 'utf-8' because the input file is in utf-8.
#5. 'as f' is a variable that will store the file object.
#6. 'text = f.read()' reads the file and returns a string. 
with open('input.txt', 'r+w', encoding='utf-8') as f:
    text = f.read()



# this line prints the number of characters in the string
print(len(text));
# this line prints the number of characters in the first 1000 characters of the string
print(text[:1000]);



