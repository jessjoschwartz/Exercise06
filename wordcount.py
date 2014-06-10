from sys import argv

my_file = argv[1]

def main():
    #Open the file
    document = open(my_file)

    #Read the file
    document_text = document.read()
    all_the_words = {}

    #Define what a word is in the file
    for word in document_text.split():
        word = word.strip([".", ",", "?"])
        if all_the_words.get(word, 0):
            all_the_words[word] += 1
        else:
            all_the_words[word] = 1
    print all_the_words

    for key, value in all_the_words.iteritems():
        print "%r %r" % (key, value)

    #Exclude non-words (punctuation, numbers, symbols, etc.)
    
    #Print results

if __name__ == "__main__":
    main()