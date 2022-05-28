import string
file = 'story.txt'

def read_file_content(filename):
    # [assignment] Add your code here 
    in_file = open(filename, "r")
    text = ""
    for line in in_file:
        text += line
    return text
    
    # return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.translate(text.maketrans(" ", " ", string.punctuation))
    text_array = text.split(" ")
    my_dict = {}
    for word in text_array:
        if word not in my_dict:
            my_dict[word] = 1 
        else:
            my_dict[word] += 1
    return my_dict
    

k =count_words()
print(k)