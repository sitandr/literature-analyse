from diff_counter import*
import data_worker as dt
import sentence_length_comparator
SQUARE_FUNCTION = lambda l1, l2: (l2 - l1)**2
SQUARE_FUNCTION.__name__ = 'SQUARE_FUNCTION'
##ABS_FUNCTION = lambda l1, l2: abs(l2 - l1)
##ABS_FUNCTION.__name__ = 'ABS_FUNCTION'
##POW_FUNCTION = lambda l1, l2: 2**(l2 - l1) - 1
##POW_FUNCTION.__name__ = 'POW_FUNCTION'
##LOG_FUNCTION = lambda l1, l2: abs(math.log(l1+1)-math.log(l2+1))
##LOG_FUNCTION.__name__ = 'LOG_FUNCTION'
##

all_data = dt.get_all_books()


prop_stack = ['grammatics', 'combinations', 'letters',
              'sentences', 'unknown']

f_aviable = [SQUARE_FUNCTION]

##for p in range(1,10):
##      for i in range(1,10):
##            f = lambda l1, l2: (abs(l1-l2)**p)
##            f.__name__ = str(p) + '#' + str(i)
##            f_aviable.append(f)

methods = {}
rating = {}
while prop_stack:
      prop_name = prop_stack[-1]
      if dt.get_type_of_data(prop_name) in ['dict', 'list']:
            pass
      elif dt.get_type_of_data(prop_name) == 'sentence_comparator':
            sentence_length_comparator.separator
      elif dt.get_type_of_data(prop_name) == 'separate':
            key_list = set()
            for i in all_data:
                  key_list=key_list.union(set(keys(i, prop_name)))

            key_list = list(key_list)
            print(prop_name, set(keys(i, prop_name)), 'Left:' , len(prop_stack))
            rating[prop_name] = {}
            for key in key_list:
                  
                  values = {}
                  for i in all_data:
                        values[i] = get_value_of(i, prop_name, key)/words_num(i)
                  
                  for function in f_aviable:

                        sum1 = 0
                        n1 = 0
                        sum2 = 0
                        n2 =0

                        for i in all_data:
                              for j in all_data:
                                    if i!=j:
            
                                          c = function(values[i],
                                                       values[j])
                                          #print(i, j, 'Error:', c, 'monoauthor = ', dt.get_val(i) == dt.get_val(j))
                                          if dt.get_val(i) == dt.get_val(j):
                                                sum1 += c
                                                n1 += 1
                                          else:
                                                sum2 += c
                                                n2 += 1
                        sum1 = (sum1/n1) ** (1.0/2)
                        sum2 = (sum2/n2) ** (1.0/2)

                        
                        
                        if(n1>0 and n2>0 and sum1>0 and sum2>0):
                              ans = ((sum1)/(sum2))
                              print(prop_name, key, function.__name__, '(should be minimum):', ans)
                              dt.safe_add(rating,function.__name__, ans)
      prop_stack.pop()
                              
                                                                  
                  


