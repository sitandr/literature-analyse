import data_worker as dt
import json
import pymorphy2
import regex
import string
import re
from collections import OrderedDict


def array_in(arr, arr2) -> bool:
       for i in arr:
              if i in arr2:
                     return True
       return False



#MIN_LENGTH = 5
#MAX_LENGTH = 25

#POSTFIXES = ['ся', "сь"]



data_dir = dt.get_data_dir()
endings = dt.get_endings()
morph = pymorphy2.MorphAnalyzer()

#t_l = 0
#t_g = 0
#t_w = 0
#t_s = 0

LETTERS = True #False


GRAMMATICS = True#False
DENIALS = True



SIMPLE_COUNT = True#False
SENTENSES = True#False
UNKNOWN_WORDS = True
COMBINATIONS = True
NAMES = True
CREATE_LANG_FILE = False#True

l_range = range(1072, 1104)
names_lemmes = ['Geox', 'Name', 'Surn', 'Patr']
last_word = None
def write_word(word):
       global denials, p, tag

       toReturn = None
       
       if not word.isalpha():
              return toReturn
       for i in word:
              if not ord(i.lower()) in l_range:
                     return toReturn
       
       p = morph.parse(word)[0]
       tag = p.tag
       toReturn = word
       if 'UNKN' in tag:
                    return toReturn
       if 'LATN' in tag or 'ROMN' in tag:
              return #toReturn
       fakeFlag = str(p.methods_stack[0][0]) == '<FakeDictionary>'
       isName = (not word.islower()) and (fakeFlag or array_in(names_lemmes, tag))

       word = p.normal_form
       toReturn = word
       if not isName:
              global last_word
              #if len(word)>MAX_LENGTH or len(word)<MIN_LENGTH:
                     #print(word)
              #       return
              
              

              #if word[-2:] in POSTFIXES:
              #       word = word[:-2]
              
              #if word[-3:] in endings:
              #       word = word[:-3]
              #elif word[-2:] in endings:
              #       word = word[:-2]
              #elif word[-1:] in endings:
              #       word = word[:-1]


              if(UNKNOWN_WORDS):
                     if fakeFlag:
                            dt.safe_add(unknown, word)
                            return toReturn
              

              

              if(LETTERS):
                     for i in word:
                            if ord(i.lower()) in l_range:
                                   letters[i.lower()] += 1

              if(DENIALS):
                     if word in ['ни', 'не']:
                            denials += 1
                     if word[:2] in ['ни', 'не']:
                            denials += 1

              if(GRAMMATICS):
                     if ('NPRO' in tag or 'PREP' in tag
                         or 'CONJ' in tag or 'PRCL' in tag
                         or 'INTJ' in tag or 'NUMR' in tag):
                            
                            gramm['not counted'] = dt.get(gramm, 'not counted') + 1
                            particals[word] = dt.get(particals, word) + 1
                            return toReturn

                     for i in str(tag).replace(' ', ',').split(','):
                            if i!= '': 
                                  gramm[i] = dt.get(gramm, i) + 1

              if(COMBINATIONS):
                     if(last_word):
                            dt.safe_add(combinations, last_word + '+' + tag.POS)
                     last_word = tag.POS
              
              
              
              if(SIMPLE_COUNT):
                     words[word] = dt.get(words, word) + 1
              
       else:
              if(NAMES):
                     for i in names_lemmes:
                            if i in tag:
                                   dt.safe_add(names, i) 
                     if fakeFlag:
                            dt.safe_add(names, 'Fake') 
                            return toReturn
       return toReturn
                     
def read(book):
       global last_word
       
       f = open(dt.get_file(book), 'r')

       text = ''

       last_word = None

       text = f.read().replace('ё', "е").replace('\n',' ').replace('\t',' ').replace('p','р')
       text = text.replace('e', 'е').replace('o','о').replace('a','а').replace('c', 'с').replace('x', 'х')
       text = regex.sub('['+'\Q"#$%&\'()*+,/:;<=>@[\\]^_`{|}~\E'+']', ' ', text)
       text = regex.sub('['+'!\?'+']', '.', text)
       for sentence in text.split('.'):
              if(SENTENSES):
                     l = len(sentence)
                     if l<5 or l>700:
                            continue
                     if l in sent:
                            sent[l] += 1
                     else:
                            sent[l] = 1

              text += sentence
              words = sentence.split()
              for i in words:
                     word = write_word(i)
                     if CREATE_LANG_FILE:
                            if word!=None:
                                   multi_text.append(word.lower())
              if CREATE_LANG_FILE:
                            multi_text.append('\n')
       f.close()

def save_read(i):
       global words, sent, gramm, letters, particals
       if(SIMPLE_COUNT):
              out = sorted(words.items(), key = lambda t: -t[1])
              dt.save_words_as(out,i)
       
       if(SENTENSES):
              out = sorted(sent.items(), key = lambda t: t[0])
              dt.save_words_as(out, i, 'sentenses')

       if(GRAMMATICS):
              dt.save_words_as(gramm, i, 'grammatics')
              dt.save_words_as(letters, i, 'particals')
              
       if(LETTERS):
              dt.save_words_as(letters, i, 'letters')
       
       if(UNKNOWN_WORDS):
              dt.save_words_as(unknown, i, 'unknown')
       if(COMBINATIONS):
              dt.save_words_as(combinations, i, 'combinations')
       if(NAMES):
              dt.save_words_as(names, i, 'names')
       if CREATE_LANG_FILE:
              dt.add_file_as(' '.join(multi_text), 'multi_text.txt')
       
       

def read_all(reread = False):
       global words, sent, gramm, letters, unknown,combinations
       global denials, names, multi_text
       for i in dt.get_all_books():
              if dt.no_description(i) or reread:
                     words = {}
                     sent = {}
                     gramm = {}
                     particals = {}
                     unknown = {}
                     combinations = {}
                     names = {'Name':0, 'Surn':0, 'Patr':0, 'Fake':0, 'Geox':0}
                     denials = 0
                     letters = dict([(chr(j), 0) for j in range(1072, 1104)])
                     letters['ё']=0
                     multi_text = [] 
                     read(i)
                     gramm['denials'] = denials
                     save_read(i)

                     print(i+ ' read.')

words = {}
sent = {}
gramm = {}
letters = {}
particals = {}
comb = {}
unknown = {}
combinations = {}
names = {}
multi_text = [] 
denials = 0
if __name__ == '__main__':
       if CREATE_LANG_FILE:
              dt.add_file_as('', 'multi_text.txt', True)
       read_all()
       
