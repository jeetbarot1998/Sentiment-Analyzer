
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(wor):
    for i in wor:
        if i in punctuation_chars:
            wor=wor.replace(i,"")
    return wor

def get_neg(n_strin):
    stri=strip_punctuation(n_strin)
    n_word=0
    b=stri.lower()
    c=b.split()
    for i in c:
        if i in negative_words:
            n_word=n_word+1
    return n_word
    
def get_pos(p_strin):
    stri=strip_punctuation(p_strin)
    p_word=0
    b=stri.lower()
    c=b.split()
    for i in c:
        if i in positive_words:
            p_word=p_word+1
    return p_word
    
positive_words = []
with open(r"C:\Users\barot\OneDrive\Desktop\Python\Emotion classifier project\positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open(r"C:\Users\barot\OneDrive\Desktop\Python\Emotion classifier project\negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

t=open(r"C:\Users\barot\OneDrive\Desktop\Python\Emotion classifier project\project_twitter_data.txt")
f=t.read()
file=f.split('\n')
f=[]
for i in file[1:]:
    j=i.split(",")
    posit=get_pos(j[0])
    negat=get_neg(j[0])
    retweet=j[1]
    reply=j[2]
    score= posit + negat
    f.append(str(retweet))
    f.append(str(reply))
    f.append(str(posit))
    f.append(str(negat))
    f.append(str(score))

   
    
print(f)
t.close()
result=open(r"resulting_data1.csv","w")            
result.write('No. of re-tweets,No. of repies,positive repies, negative replies,net score \n')
b=0
for i in f:
    result.write(i)
    result.write(',')
    b=b+1
    if b%5 ==0:
        result.write('\n')


result.close()

print("done")
