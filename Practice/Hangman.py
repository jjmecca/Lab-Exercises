import random

filename="wordlist.txt"
f=open(filename,"r")
words=f.readlines()
word=random.choice(words)
length=len(word)
guess=""
incorrect_guesses=[""]
correct_guesses=[""]
won=False
tries=0

while True:
    tries+=1
    fail=0
    guess=input("\nEnter a character or guess: ")
    if guess==word:
        won=True
        break
    for i in word:
        if i in correct_guesses:
            print(i,end="")
        elif i==guess:
            print(i,end="")
            correct_guesses.append(i);
        else:
            fail+=1
            print("_",end="")
            incorrect_guesses.append(i);
    print("\nTry: ")
    print(tries)
    if fail==0:
        won=True
        break
    if tries==11:
        break
if won:
    print("\nCongrats!")
else:
    print("\nYou lost :(")