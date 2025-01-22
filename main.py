
def main():
    path = "books/frankenstein.txt"
    text = getbook(path) 
    numwords = count_words(text)
    print(numwords)
    
def getbook(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents
    
def count_words(file_contents):
        words = file_contents.split()
        numwords = len(words)
        return numwords

    
main()