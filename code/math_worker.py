import numpy as np
import math

def create_rasp(data, step = 0.001, smoothing = 0.1, sm_length = None, min_max = None):
      if min_max == None:
            min_v, max_v = min(data), max(data)
      else:
            min_v, max_v = min_max
      if min_v == max_v:
            return
      step =step*(max_v-min_v)
      if sm_length == None:
            smooth = int(smoothing * (max_v-min_v)/step)
      else:
            smooth = sm_length
      xs = np.arange(min_v - smooth*step, max_v + smooth*step, step)
      rasp = np.zeros(len(xs))
      for i in range(len(data)):
            ind = round(data[i]/step+smooth)
            for j in range(ind-smooth, min(ind+smooth, len(xs)-1)):
                  v = np.e**(-6*(float(j-ind)/smooth)**2)
                  
                  rasp[j]+=v

      C = sum(rasp)/step
      rasp /= C
      
      return xs, rasp

