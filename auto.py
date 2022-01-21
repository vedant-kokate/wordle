from collections import defaultdict

def freq(words):
    fr=defaultdict(int)
    for w in words:
        for ch in w:
            fr[ch]+=1
    return fr

def best_words(words,fr):
    bword=[]
    m=-1
    for w in words:
        score = getscore(w,fr)
        bword.append((score,w))
    bword.sort(reverse=True)
    ans=[]
    for i in range(min(7,len(bword))):
        ans.append(bword[i][1])
    return ans

def getscore(w,fr):
    sc=0
    for l in set(w):
        if l not in g and l not in y:
            sc+=fr[l]
    return sc

f=open('words.txt','r')
words=set(f.readline().split())
r=set()
g=['']*5
y=defaultdict(list)
guesswords=list(words)
while True:
    print('Total possible words =',len(guesswords))
    # print(guesswords[:20])
    fr = freq(guesswords)
    myguess=best_words(guesswords, fr)
    print('Best guesses -',*myguess,sep=",")
    # print("=========")
    guesswords=[]
    print("your guess?",sep=" ")
    guess=input().strip()
    print('result?')
    s=input().strip()
    if s=="ggggg":
        break
    # print("taken input")

    for i in range(5):
        if s[i]=='b':
            r.add(guess[i])
        elif s[i]=='g':
            g[i]=guess[i]
        else:
            y[i].append(guess[i])
    # print(r,g,y)
    
    rcount=0
    for w in words:
        flag=True
        for i in range(5):
            if w[i] in r:
                # print('r')
                rcount+=1
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


                



