from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import RPropMinusTrainer
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.structure.modules import TanhLayer

ds = SupervisedDataSet(33*33, 1)
for _ in range(1):
      ds.addSample([0]*33*33, (0,))
      ds.addSample([0]*(33*33//2)+[1]*(33*33//2+1), (1,))
      ds.addSample([1]*(33*33//2)+[0]*(33*33//2+1), (1,))
      ds.addSample([1]*(33*33//2)+[1]*(33*33//2+1), (0,))

fail = 0
sucess = 0

for i in range(100):
      net     = buildNetwork(33*33, 5, 1, bias=True)
      trainer = RPropMinusTrainer(net, dataset=ds)
      trainer.trainEpochs(200)
      s = 0
      for inp, tar in ds:
            #print(net.activate(inp)[0]-tar[0])
           s+=(net.activate(inp)[0]-tar[0])**2
      #print(s)
      
      if s>0.2:
            print('Fail')
            fail+=1
      else:
            sucess+=1
            print('Sucess')
      
      print(i)
print(fail, sucess)
