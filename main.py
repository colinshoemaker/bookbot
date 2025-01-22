def main():
    path = "books/frankenstein.txt"
    text = getbook(path) 
    numwords = count_words(text)
    numlets = count_characters(text)
    numletlst =[]
    for let, num in numlets.items():
        if let.isalpha() == True:
            char_dict = {"letter": let, "number": num}
            numletlst.append(char_dict)
    numletlst.sort(reverse = True, key = sort_on)
    for k in numletlst:
        letter = k["letter"]
        number = k["number"]
        print(f"The '{letter}' character was found {number} times")

def sort_on(dict):
    return dict["number"]
    
def getbook(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
    
def count_words(file_contents):
    words = file_contents.split() 
    return len(words)

def count_characters(text):
    lowtext = text.lower()
    lettd ={}
    for let in lowtext:
        if let in lettd:
            lettd[let] += 1
        else:
            lettd[let]=1
    return lettd
    



main()