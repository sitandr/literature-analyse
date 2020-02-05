import os#, sys
import json

cash = {}

def add_book(name, author = 'Unknown', year = 0):
       descriptor[name] = {'author':author, 'year':year, 'read_bytes': 0}
def del_book(name):
       del descriptor[name]
def get_books_by(val, prop='author'):

       to_return = []
       
       for i in descriptor:
              if descriptor[i] [prop] == val:
                     to_return.append(i)
       return to_return
def get_book_of(val, prop = 'author'):
       for i in descriptor:
              if descriptor[i] [prop] == val:
                     return i
def get_val(name, prop='author'):
       return descriptor[name][prop]
def set_val(name, val, prop = 'author'):
       descriptor[name][prop] = val
def get_descriptor():
       return descriptor
def get_file(name):
       return main + '/data/literature/' + name + '/text.txt'
def get_data_dir():
       return main + '/data'
def get_book():
       for i in descriptor:
              return i
def get_all_books():
       r=[]
       for i in descriptor:
              r.append(i)
       return r

def get_endings():
       r=[]
       for i in endings:
              r+=endings[i]
       return r
def flush():
       json_descriptor = open(main + '/data/descriptors/main.json', 'w')
       json.dump(descriptor, json_descriptor)
       json_descriptor.close()

def get_words_file(name,type_='words'):
       return main + '/data/literature/' + name + '/'+type_+'.json'

def save_words_as(words,name, type_='words'):
       json_words = open(get_words_file(name, type_), 'w') 
       json.dump(words,json_words)
       json_words.close()
def add_file_as(data, name, restart = False):
       f = open(main +'/data/descriptors/' + name, 'w' if restart else 'a') 
       f.write(data)
       f.close()
def get_file_as(name):
       f = open(main +'/data/descriptors/' + name) 
       d = f.read(data)
       f.close()
       return d
def get_words(name, type_='words'):
       if name in cash:
              return cash[(name, type_)]
       json_words = open(get_words_file(name, type_), 'r')
       words = json.load(json_words)
       json_words.close()
       cash[(name, type_)] = words
       return words


def no_description(name):
       return not os.path.isfile(get_words_file(name))


def get(dict1,i,default=0):
       return dict1[i] if i in dict1 else default

def devide_dict(dict1,m):
       for i in dict1:
              dict1[i]/=m
       return dict1
def sum_dicts(dict1, dict2, minus = False):
       dict_ = {}
       for i in set(list(dict1.keys())+list(dict2.keys())):
              dict_[i] = get(dict1,i)+ (-get(dict2,i) if minus else get(dict2,i))
       return dict_

def dict_diff(dict1, dict2, funct = lambda l1, l2: (l1-l2)**2):
      all_y = sum_dicts(dict1, dict2)
      all_y = list(all_y.items())
      y = list(map(lambda t: funct(get(dict1, t[0]), get(dict2, t[0])),
                   all_y))
      return sum(y)

def safe_add(dict1, name, num = 1):
       if name in dict1:
              dict1[name] += num
       else:
              dict1[name] = num


def save_data_piece(name, data):
       json_descriptor = open(main + '/data/descriptors/' + name + '.json', 'w')
       json.dump(descriptor, json_descriptor)
       json_descriptor.close()


data_types = {'grammatics':'separate', 'combinations':'separate', 'letters':'separate',
              'sentences':'sentence_comparator', 'unknown': 'dict'}
def get_type_of_data(name):
       return data_types[name]

def data_const(name)-> int: 
      "returns the length of data of"
      "the FIRST book in descriptor"
      b = get_book()
      data = get_words(b, name)
      return len(data)

main = os.path.dirname(os.getcwd())
#sys.path.append(main)

json_descriptor = open(main + '/data/descriptors/main.json', 'r')
descriptor = json.load(json_descriptor)
json_descriptor.close()

json_endings = open(main + '/data/special/endings.json', 'r')
endings = json.load(json_endings)
json_endings.close()

if __name__ == '__main__':
       #console mode
       while True:
              comm = input().strip().split('|')
              print(comm)
              if(len(comm) == 2):
                     if comm[0] == 'del':
                            del_book(comm[1])
                            print(comm[1]+' deleted')
                     if comm[0] == 'add':
                            add_book(comm[1])
                            print(comm[1]+' added')
              flush()
