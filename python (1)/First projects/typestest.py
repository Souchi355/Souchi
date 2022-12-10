import time
import english_words
import random

while True:
    play=input("start ? y/n : ")
    if play =="y":
        t=10
        l=0
        start = time.time()
        while t!=0:
            word=random.choice(list(english_words.english_words_set))
            print(f"type this n{t}: {word}")
            wordp=input("time is start ! :")
            
            if wordp==word:
                t-=1
                l+=len(word)
                print("-------------")
        end = time.time()
        print(f"your time {(end - start)//1} s\nnomber of letters {l}")