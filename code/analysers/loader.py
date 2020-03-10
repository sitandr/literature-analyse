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
      global ds, all__
      d = analyse_2(string)
      arr = np.zeros(33*33)
      for j in d[0]:
            arr[int(j)] = d[0][j]
      
      all_ = np.round(math.e**(np.abs(net.activate(arr)-1)), 3)
      all_ = all_/sum(all_)
      res = -1
      ind = -1
      for i in range(L):
          if all_[i]>res:
              res = all_[i]
              ind = i
      rounded = classes[ind]
      return rounded, res, list(zip(classes, all_))


time1 = time.time()
authors = read_all()
time2 = time.time()
print(time2-time1)
max_ = max(map(lambda t: len(authors[t]), authors))
max_len = max(map(lambda t: max(map(lambda t1:t1[1], authors[t])), authors))
classes = [_ for _ in authors]
L = len(classes)

net = NetworkReader.readFrom('filename_2.xml') 
