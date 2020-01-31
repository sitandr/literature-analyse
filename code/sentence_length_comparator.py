import data_worker as dt
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def funct(x, A, B, C, D, E):
       return A/(x + D) + (B/((x+E)**0.5)) + C


def sum_norm(x, A, B, C, D, E, F):
       return A*np.e**(B*(x+C)**2)+D*np.e**(E*(x+F)**2)

def alternative(x, A, B, C, D , E, F, G, H):
       return (A*x**5+B*x**4+C*x**3+D*x**2+E*x+F)*np.e**(x*H+G)

def norm(x, A, B, C):
       return A*np.e**(-B*(x+C)**2)

NUMBER = 700
D_L = 40

def comparator(name1, name2):
      a1, b1, c1 = book_descr(name1)
      a2, b2, c2 = book_descr(name2)
      return (((a1-a2)/(a1+a2))**2 +
              ((b1-b2)/(b1+b2))**2 +
              ((c1-c2)/(c1+c2))**2)**0.5
def book_descr(name):
       toConsider = dt.get_words(name,'sentenses')#[:NUMBER]
       C = sum(list(map(lambda t: t[1], dt.get_words(name))))
       #print(C)
       y = np.array(list(map(lambda t: t[1], toConsider)))
       
              
       x = np.array(list(map(lambda t: t[0], toConsider)))

       y_n = y.copy()
       for i in range(0,len(y)-D_L):
              for j in range(max(- D_L, -i), D_L + 1):
                     v = y[i]*np.e**(-(j/4)**2)
                     y_n[i-j] += v
                     y_n[i+j] += v
       #C = sum(y)
       y = y_n/C
       x = np.log(x)
       
       result, _ =curve_fit(norm , x, y,
                            maxfev = 10000)
       return result[0], result[1], result[2] 
##       
##       plt.plot(x,abs(norm(x, *result)), random.choice(styles), label = i)
##       plt.plot(x,y)
##       
##plt.legend(loc='upper right')
##plt.show()
###words = dt.get_words()

