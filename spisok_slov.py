import string

def count_word_frequency(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    words = sentence.lower().split()
    
    word_frequency = {}
    
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    sorted_word_frequency = sorted(word_frequency.items())
    
    for word, count in sorted_word_frequency:
        print(f"{word}: {count}")
    

sentence = input("Enter a sentence or a paragraph: ")

count_word_frequency(sentence)
