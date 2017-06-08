# Tony Richardson
# Colin Casey
# TCSS 456
# Spring 2017
# Final Project

import re
import nltk
from nltk import tokenize
from nltk.corpus import brown
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk


# splits sentisynset object into list of its parts
#    <place.v.12: PosScore=0.0 NegScore=0.0>
# to ['place.v.12', 0.0, 0.0]
def splitScore (score):
    my_senti_list = [None, 0.0, 0.0]
    if score != None:
        score = str(score)
        my_senti_list = re.split(' ', score)
        #remove '  just get wordnet tag
        my_senti_list[0] = my_senti_list[0][1:]
        my_senti_list[0] = my_senti_list[0][:-1]
        #get number
        my_senti_list[1] = my_senti_list[1][len('PosScore='):]
        my_senti_list[1] = float(my_senti_list[1])
        #get number
        my_senti_list[2] = my_senti_list[2][len('NegScore='):]
        my_senti_list[2] = my_senti_list[2][:-1]
        my_senti_list[2] = float(my_senti_list[2])
    return my_senti_list


#word dictionary for all words
#{word, [positive, negative, count]}
word_dict = {}
#stores positve and negative scores for each sentence
#position in list matches position in sentences list
# [[positive, negative], [positive, negative], ...]
sent_vals = []
#creates a list with lists of words in each sentence
# [['I', 'am', 'a', 'dog', '.'], ['Hello', there', '.']]
sentences = brown.sents()
#[positive, negative] for article
article_pos_val = [0,0]
#find the polarity for words, sentences and the whole article
#keep counts of positive and negative scores and count for each word
for i in range(len(sentences)):
    #[positive, negative] for each sentence
    sent_pos_val = [0,0]
    #j is a word
    for j in sentences[i]:
        #get wordnet tag and positive and negative scores for each word
        lesked = str(lesk(sentences[i], j))
        leskword = lesked[len("Synset('"):]
        leskword = leskword[:-len("')")]
        try:
            #word was in wordnet
            posvalue = swn.senti_synset(leskword)
        except:
            #word was not in wordnet
            posvalue = None
        #convert lesk value into a list so I can do stuff with it
        split = splitScore(posvalue)
        #append the word to the front of the list
        split.insert(0, j)
        # make list [word, positive, negative, count]
        # put list in dictionary of all words
        if j in word_dict:
            #update values in dictionary
            tmp = word_dict[j]
            tmp[0] += split[2]
            tmp[1] += split[3]
            tmp[2] += 1
            tmp[3].append(i)
            word_dict[j] = tmp
        else:
            #put new entry in dictionary
            word_dict.update({j: [split[2],split[3],1,[i]]})
        #add sentence values to list of sentence values
        sent_vals.append(sent_pos_val)
        # add word values to sentence value
        sent_pos_val[0] += split[2]
        sent_pos_val[1] += split[3]
    #avaerage positive and negative scores for sentences
    count = len(sentences[i])
    sent_pos_val[0] /= count
    sent_pos_val[1] /= count
    #add sentence scores to article total
    article_pos_val[0] += sent_pos_val[0]
    article_pos_val[1] += sent_pos_val[1]



#write output to file and print to console

# Clear file
outfile = open('projectout.txt', 'w')
outfile.close()
# Open file to write
outfile = open('projectout.txt', 'a')

print('for article')
print('score: ' + str(article_pos_val[0] - article_pos_val[1]))

# get the score for the whole article
outfile.write('for article\n')
outfile.write('score: ' + str(article_pos_val[0] - article_pos_val[1]) + '\n')    

print()

#combine the positive and negative values for each sentence
combined_sent_vals = []
for i in sent_vals:
    combined_sent_vals.append(i[0] - i[1])


word_dict_calc = {}
for e in word_dict:
    tmp = word_dict[e]
    word_dict_calc.update({e:(tmp[0]-tmp[1])/tmp[2]})
vals = sorted(word_dict_calc.values())
keys = sorted(word_dict_calc, key = word_dict_calc.get)
neg_list = []

# print the 5 most positive words and sentences
print('positive words')
outfile.write('\npositive words\n')
for i in range(-1, -6, -1):
    #list of indexes for sentences the word appears in
    #indexes are for the list of sentences called `sentences`
    sents = word_dict[keys[i]][3]
    minval = 0
    sent_idx = 0
    for j in range(len(sents)):
        if combined_sent_vals[sents[j]] < minval:
            sent_idx = sents[j]
            minval = combined_sent_vals[sents[j]]
    
    print(str(keys[i]) + ': ' + str(vals[i]))
    outfile.write(str(keys[i]) + ': ' + str(vals[i]) + '\n')
    the_sentence = ''
    for i in sentences[sent_idx]:
        the_sentence += i + ' '
    print(the_sentence)
    outfile.write(the_sentence + '\n')
print()
# print the 5 most negative words and sentences
print('negative words')
outfile.write('\nnegative words\n')
for i in range(5):
    #list of indexes for sentences the word appears in
    #indexes are for the list of sentences called `sentences`
    sents = word_dict[keys[i]][3]
    maxval = 0
    sent_idx = 0
    for j in range(len(sents)):
        if combined_sent_vals[sents[j]] > maxval:
            sent_idx = sents[j]
            minval = combined_sent_vals[sents[j]]
    
    print(str(keys[i]) + ': ' + str(vals[i]))
    outfile.write(str(keys[i]) + ': ' + str(vals[i]) + '\n')
    the_sentence = ''
    for i in sentences[sent_idx]:
        the_sentence += i + ' '
    print(the_sentence)
    outfile.write(the_sentence + '\n')

outfile.close()


