from chardet.universaldetector import UniversalDetector


import os




def opener(file):
      detector = UniversalDetector()
      detector.feed(open('texts/'+file, 'rb').read())
      detector.close()
      return open('texts/'+file, encoding = detector.result['encoding']).read()

import regex
def analyse(text):
      distances = dict([(chr(_), 0) for _ in range(1072, 1104)])
      numbers = dict([(chr(_), 0) for _ in range(1072, 1104)])
      indexes = dict([(chr(_), 0) for _ in range(1072, 1104)])
      for i in range(len(text)):
            l = text[i]
            if not l in distances:
                  continue
            
            distances[l] = i - indexes[l]
            numbers[l]+=1
            indexes[l] = i
      return [(distances[_],numbers[_]) for _ in distances]
def safe_add(d, k, default = 1):
      if k in d:
            d[k]+=default
      else:
            d[k] = default
def analyse_2(text):
      global text_
      text_=text
      pairs = {}
      triples = {}

      last = None
      #last_2 = None
      c = len(text)
      text = regex.sub('[^а-я]', '', text.lower())
      for i in text:
            if last:
                  safe_add(pairs, encoder((last+i).lower()), 1.0/c)
                  #if last_2:
                  #      safe_add(triples, (last_2+last+i).lower(), 1.0/c)
            #last_2 = last
            last = i
      return pairs, len(text)
def encoder(s):
      return (ord(s[0])-1072)*33+(ord(s[1])-1072)
def read_all():
      all_ = os.listdir('texts')
      authors = {}
      for file in all_:
            author = file[:file.find('_')]
            text = opener(file)
            #print('!',file)
            #print(text[:100])
            #print('####')
            #print(open('texts/'+file, encoding = 'ansi').read()[:50])
            if author in authors:
                  authors[author].append(analyse_2(text))
            else:
                  authors[author] = [analyse_2(text)]
      return authors
