import nltk
from nltk.corpus import wordnet

print("Welcome to sentence comprassion")
print(" ")
Phrase1 = input("Type the first sentence here:")
Phrase2 = input("Type the second sentence here:")

print("Plz wait...")
#'JJR','JJS','VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS'
# ta eidh twn rhmatwn, epithetwn, ousiastikwn pou prepei na krathsoume
# h item1 kai h item2 ousiastika krataei ta parapanw eidh pou anefera

Array = [Phrase1]
for item1 in Array:
    tokenized = nltk.word_tokenize(item1)
    tagged = nltk.pos_tag(tokenized)
    item1 = ([(word, tag) for word, tag in tagged if tag in ('JJ','JJR','JJS','VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS')])
  

Array = [Phrase2]
for item2 in Array:
    tokenized = nltk.word_tokenize(item2)
    tagged = nltk.pos_tag(tokenized)
    item2 = ([(word, tag) for word, tag in tagged if tag in ('JJ','JJR','JJS','VB','VBD','VBG','VBN','VBP','VBZ','NN','NNS','NNP','NNPS')])
    

#Omws sthn item1 opws kai sthn item2 oi le3eis kratiountai me ta tag tous
#sunepws gia na ta sugkrinw tha xreiastw na afairesw ta tags kai na meinoun
#mono oi le3eis wste na tis sugkrinw :
item1N = [item[0] for item in item1]
item2N = [item[0] for item in item2]
list = []
for word1 in item1N:
    for word2 in item2N:
        wordFromitem1N = wordnet.synsets(word1)
        wordFromitem2N = wordnet.synsets(word2)
        if wordFromitem1N and wordFromitem2N: 
            s = wordFromitem1N[0].wup_similarity(wordFromitem2N[0])
            list.append(s)
print("The sentence are matches:",max(list)*100,"%")



