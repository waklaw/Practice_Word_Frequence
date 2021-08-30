# Python code to find frequency of each word
def freq(text):
    #Splitting text into individual words
    words = text.split()
    words_set = set(words)

    #Creating a dictionary with words
    count = {a: 0 for a in words_set}

    #Counting frequencies
    for word in words:
        count[word] += 1

    #Printing results
    for word in words_set:
        print('Frequency of word "', word, '" is ', count[word])

def main():
    #Reading text from the file
    with open('text.txt', 'r', ) as f:
        text = f.read()
    print('Input text : ', text)
    freq(text)

if __name__ == "__main__":
    main()  # call main function