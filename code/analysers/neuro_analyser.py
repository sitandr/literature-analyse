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

def check(string):
      global net, ds
      d = analyse_2(string)
      arr = np.zeros(33*33)
      for j in d[0]:
            arr[j] = d[0][j]
      res = float(net.activate(arr)[0])
      rounded = min(max(int(round(res)), 0), len(classes)-1)
      return ds.getClass(rounded), abs(res-rounded)

time1 = time.time()
authors = read_all()
time2 = time.time()
print(time2-time1)
max_ = max(map(lambda t: len(authors[t]), authors))
max_len = max(map(lambda t: max(map(lambda t1:t1[1], authors[t])), authors))
classes = [_ for _ in authors]
ds = ClassificationDataSet(33*33, nb_classes = len(classes), class_labels = classes)
for author in authors:
      for text in authors[author]:
            arr = np.zeros(33*33)
            for j in text[0]:
                  arr[j] = text[0][j]
            for _ in range(math.ceil(max_/len(authors[author])*10*(text[1]/max_len))):
                  ds.addSample(arr, classes.index(author))


net     = buildNetwork(33*33, 10, 3, 1, bias=True)
trainer = RPropMinusTrainer(net, dataset=ds)
trainer.trainEpochs(100)
print(trainer.testOnClassData())
NetworkWriter.writeToFile(net, 'filename.xml')
s = 0
time3 = time.time()
print(time3-time2)


#for inp, tar in ds:
#      print(tar[0], net.activate(inp)[0]-tar[0])
      #s+=(net.activate(inp)[0]-tar[0])**2

