from chardet.universaldetector import UniversalDetector
import os
import json



def opener(file, prefix = 'texts/'):
      detector = UniversalDetector()
      detector.feed(open(prefix+file, 'rb').read())
      detector.close()
      return open(prefix+file, encoding = detector.result['encoding']).read()

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
def analyse_2(text, f=2):
      global text_
      text_=text
      pairs = {}
      triples = {}

      last = None
      last_2 = None
      c = len(text)
      text = regex.sub('[^а-я]', '', text.lower())
      for i in text:
            if last:
                  safe_add(pairs, encoder((last+i).lower()), 1.0/c)
                  if f>2 and last_2:
                        safe_add(triples, encoder((last_2+last+i).lower()), 1.0/c)
            last_2 = last
            last = i
      return pairs if f==2 else triples, len(text)
def cutter(text, step = 300):
      arr = [text[_*step:(_+1)*step] for _ in range(len(text)//300)]+[(len(text)//300)*300:-1]+text[-1]
def cashed_analyse(file, f = 2):
    try:
        return json.loads(opener('cash_'+str(f)+'_'+file, prefix = 'cashes/'))
    except:
        text = analyse_2(opener(file), f)
        file = open( 'cashes/cash_'+str(f)+'_'+file, 'w')
        json.dump(text, file)
        file.close()
        return text
def encoder(s):
      summ = 0
      for i in range(len(s)):
            summ+=(ord(s[i])-1072)*(33**(len(s)-1-i))
      return summ
def read_all(f = 2):
      all_ = os.listdir('texts')
      authors = {}
      for file in all_:
            if 'cash' in file or 'ignore' in file:
                pass
            author = file[:file.find('_')]
            analysed = cashed_analyse(file, f)
            if author in authors:
                  authors[author].append(analysed)
            else:
                  authors[author] = [analysed]
      return authors
