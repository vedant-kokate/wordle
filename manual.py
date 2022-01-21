from collections import defaultdict
# import nltk
# nltk.download('words')

# from nltk.corpus import words
# word_list = words.words()
# # prints 236736
# print (len(word_list))

def freq(words):
    fr=defaultdict(int)
    for w in words:
        for ch in w:
            fr[ch]+=1
    return fr

def best_word(words,fr):
    bword=""
    m=-1
    for w in words:
        score = getscore(w,fr)
        if score>m:
            m=score
            bword=w
    return bword

def getscore(w,fr):
    sc=0
    for l in set(w):
        if l not in g and l not in y:
            sc+=fr[l]
    return sc

f=open('words.txt','r')
words=set(f.readline().split())
# print(len(words))


# print(sorted(fr.values()))

guesswords=[]
# guess 1
r=['o','s','e','h','y','k','f']
y=defaultdict(list)
y[1].append('r')
y[0].append('a')
y[2].append('i')
# y[2].append('r')
y[3].append('r')
# y[4].append('a')
# y[0]='i'
# y[1]='n'
# y[2]='m'
# y[2]='s'
# y[3]='l'
y[4].append('r')
g=['']*5
g[0]='r'
g[1]='a'
# g[2]='u'
g[3]='i'
g[4]='d'
# print(words)
for w in words:
        flag=True
        for i in range(5):
            if w[i] in r:
                # print('r')
                # rcount+=1
                flag=False
                break
            if g[i]!='' and w[i]!=g[i]:
                # print('g')
                flag=False
                break
            if w[i] in y[i]:
                # print("here")
                flag=False
                break
        for v in y.values():
            if v!=[]:
                for val in v:
                    if val not in w:
                        flag=False
                        break
        if flag:
            guesswords.append(w)

print(len(guesswords))
print(guesswords)
fr = freq(guesswords)

m=-1
word2=""
for w in guesswords:
    score = getscore(w,fr)
    if score>m:
        m=score
        word2=w

print("=======")
print(word2)
#
                



