from collections import defaultdict
import nltk
nltk.download('words')

from nltk.corpus import words
word_list = words.words()
# prints 236736
print (len(word_list))
words=set()
# print(f.readline())
for w in word_list:
    if len(w)==5:
        words.add(w)
print(len(words))
w2=set()
for w in words:
    w2.add(w.lower())
f=open('words.txt','w')
for i in w2:
    f.write(i+" ")
f.close()