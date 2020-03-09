from pybrain3.datasets import SupervisedDataSet,ClassificationDataSet
from pybrain3.supervised.trainers import RPropMinusTrainer
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.structure.modules import TanhLayer
from letter_combinations import read_all, analyse_2
import math
import numpy as np
import time
from pybrain3.tools.xml import NetworkWriter
from pybrain3.tools.xml import NetworkReader

def check(string, net_ = None):
      if net_ == None:
            global net
      else:
            net = net_
      global ds
      d = analyse_2(string, 3)
      arr = np.zeros(33*33*33)
      for j in d[0]:
            arr[int(j)] = d[0][j]
      all_ = math.e**(np.abs(net.activate(arr)-1))
      res = -1
      ind = -1
      for i in range(L):
          if all_[i]>res:
              res = all_[i]
              ind = i
      rounded = classes[ind]
      return rounded, res, list(zip(classes, all_))

if __name__ == "__main__":
      time1 = time.time()
      authors = read_all(3)
      time2 = time.time()
      print(time2-time1)
      max_ = max(map(lambda t: len(authors[t]), authors))
      max_len = max(map(lambda t: max(map(lambda t1:t1[1], authors[t])), authors))
      classes = [_ for _ in authors]
      L = len(classes)
      ds = SupervisedDataSet(33*33*33, L)
      for author in authors:
            for text in authors[author]:
                  arr = np.zeros(33*33*33)
                  for j in text[0]:
                        arr[int(j)] = text[0][j]
                  for _ in range(math.ceil(max_/len(authors[author])*10*(text[1]/max_len))):
                        arr2 = np.zeros(L)
                        arr2[classes.index(author)] = 1
                        ds.addSample(arr, arr2)


      net     = buildNetwork(33*33*33, 10, 10, L, bias=True)
      trainer = RPropMinusTrainer(net, dataset=ds)
      trainer.trainEpochs(100)
      print(trainer.testOnData())
      NetworkWriter.writeToFile(net, 'filename_3.xml')
      s = 0
      time3 = time.time()
      print(time3-time2)


      #for inp, tar in ds:
      #      print(tar[0], net.activate(inp)[0]-tar[0])
            #s+=(net.activate(inp)[0]-tar[0])**2

