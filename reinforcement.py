def words_in_string(string):
    return len(string.split())

og_string = "Hello world this is a test string"
r=words_in_string(og_string)

print("The number of words in the string is {}".format(r))