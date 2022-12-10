def search(text, word):    
    if word in text:
       print(' word found  ', text.count(word), ' times')
    else:
       print("word not found")
    

text=str("''")
word=str(input('word : '))
search(text,word)