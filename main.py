def main():
    path = "books/frankenstein.txt"
    text = getbook(path) 
    numwords = count_words(text)
    print(numwords)
    print(count_characters(text))
    
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