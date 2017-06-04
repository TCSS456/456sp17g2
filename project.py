


#nltk.download() #starts download wizard
import re
import nltk
from nltk import tokenize


from nltk.corpus import brown
from nltk.corpus import sentiwordnet as swn

from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
#from nltk.sentiment import sentiment_analyzer






# splits sentisynset object into list of its parts
# <place.v.12: PosScore=0.0 NegScore=0.0>
def splitScore (score):
    my_senti_list = [None, 0.0, 0.0]
    if score != None:
        score = str(score)
        my_senti_list = re.split(' ', score)
        my_senti_list[0] = my_senti_list[0][1:]
        my_senti_list[0] = my_senti_list[0][:-1]
        my_senti_list[1] = my_senti_list[1][len('PosScore='):]
        my_senti_list[1] = float(my_senti_list[1])
        my_senti_list[2] = my_senti_list[2][len('NegScore='):]
        my_senti_list[2] = my_senti_list[2][:-1]
        my_senti_list[2] = float(my_senti_list[2])
    return my_senti_list













##wordnet synset tags
##n    NOUN
##v    VERB
##a    ADJECTIVE
##s    ADJECTIVE SATELLITE
##r    ADVERB 
##
##format
##  1  2 3
##  v  v v
##'dog.n.01'
##1 = word
##2 = synset tag
##3 = 






##tagged_news = brown.tagged_words(categories = 'news')
##
##for i in range(20):
##    print(tagged_news[i])

##smash = swn.senti_synset('smash.v.05')
##print(smash)

#nltk.pos_tag(list_of_words)  #applies tags to a list of words (a sentence or sentences)


#sid = SentimentAnalyzer()




##lista = list(swn.senti_synsets('slow'))
##print(lista)
###print(SentiSyneset('slow.v'))
##for e in lista:
##    print(e)




##print(len(tagged_news))
##
##for i in range(100):
##    print(tagged_news[i])


#for i in tagged_news:
#    print(i)





# convert penn treebank tags to wordnet tags.

#penn_tags = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT','POS','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']
#penn_tags = {'CC':'','CD':'','DT':'','EX':'','FW':'','IN':'','JJ':'a','JJR':'a','JJS':'a','LS':'','MD':'','NN':'n','NNS':'n','NNP':'n','NNPS':'n','PDT':'','POS':'','PRP':'','PRP$':'','RB':'r','RBR':'r','RBS':'r','RP':'','SYM':'','TO':'','UH':'','VB':'v','VBD':'v','VBG':'v','VBN':'v','VBP':'v','VBZ':'v','WDT':'','WP':'','WP$':'','WRB':'r'}




##sent = ['John', 'loves', 'mary']
##print(lesk(sent,'loves'))


#list of sentences that are lists of words.
sentences = brown.sents()
##print(sentences[0])
meaning_lesk = lesk(sentences[0], sentences[0][5])

word= str(lesk(sentences[0], sentences[0][5]))
word = word[8:]
word = word[:-2]
##print(word)

##print(lesk(sentences[0], sentences[0][5]))

## standalone sentiment getter given word
##print(swn.senti_synset('fulton.n.01'))
##print(swn.senti_synset(word))

sentences = brown.sents()
print(len(sentences))
article_pos_val = [0,0]
for i in range(100):
    #[positive, negative]
    sent_pos_val = [0,0]
    count = 0;
    count = len(sentences[i])
    for j in sentences[i]:
        #print(j)
        lesked = str(lesk(sentences[i], j))
        #print(lesked)
        #if lesked is not None:
        leskword = lesked[8:]
        leskword = leskword[:-2]
        #print(leskword)
        try:
            posvalue = swn.senti_synset(leskword)
        except:
            posvalue = None
        #print(posvalue)
        #print(list([j]).insert(0, splitScore(posvalue)))
        #print(j)
        split = splitScore(posvalue)
        #print(split)
        split.insert(0, j)
        #print(split)
        
        sent_pos_val[0] += split[2]
        sent_pos_val[1] += split[3]
    #print(count)
    sent_pos_val[0] /= count
    sent_pos_val[1] /= count
    article_pos_val[0] += sent_pos_val[0]
    article_pos_val[1] += sent_pos_val[1]
    print(sent_pos_val)
print(article_pos_val)
        

sentiment_list = re.split(' ','<place.v.12: PosScore=0.0 NegScore=0.0>')

#print(sentiment_list)



# splits sentisynset object into list of its parts
# <place.v.12: PosScore=0.0 NegScore=0.0>
##def asplitScore (score):
##    my_senti_list = [None, 0.0, 0.0]
##    if score != None:
##        score = str(score)
##        my_senti_list = re.split(' ', score)
##        my_senti_list[0] = my_senti_list[0][1:]
##        my_senti_list[0] = my_senti_list[0][:-1]
##        my_senti_list[1] = my_senti_list[1][len('PosScore='):]
##        my_senti_list[1] = float(my_senti_list[1])
##        my_senti_list[2] = my_senti_list[2][len('NegScore='):]
##        my_senti_list[2] = my_senti_list[2][:-1]
##        my_senti_list[2] = float(my_senti_list[2])
##    return my_senti_list
    
    

#print(splitScore('<place.v.12: PosScore=0.0 NegScore=0.0>'))
#print(splitScore(None))
#print(splitScore('<place.v.12: PosScore=0.0 NegScore=0.0>'))











