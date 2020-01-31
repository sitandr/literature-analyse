import data_worker as dt
import math


SQUARE_FUNCTION = lambda l1, l2: (l2 - l1)**2
ABS_FUNCTION = lambda l1, l2: abs(l2 - l1)
POW_FUNCTION = lambda l1, l2: 2**(l2 - l1) - 1
LOG_FUNCTION = lambda l1, l2: abs(math.log(l1+1)-math.log(l2+1))

data1 = []
data2 = []


##def gramm_dif(name1, name2, names, ks, fs):
##       by = 'grammatics'
##       data1 = dt.get_words(i[0], by)
##       data2 = dt.get_words(i[1], by)
##
##       for i in range(len(names)):
##             y += ks[i] * fs[i](data1[names[i]], data2[names[i]])
##       return y

def diff(*i, by = 'words',
         function = LOG_FUNCTION):
       global data1, data2, y
       data1 = dt.get_words(i[0], by)
       data2 = dt.get_words(i[1], by)

       if(type(data1)== dict):
             data1 = data1. items()
       if(type(data2)== dict):
             data2 = data2. items()
      
       d_data1 = dict(data1)
       d_data2 = dict(data2)

       C0 = sum(list(map(lambda t: t[1], data1)))
       C1 = sum(list(map(lambda t: t[1], data2)))

       y = dt.dict_diff(dt.devide_dict(d_data1, C0),
                        dt.devide_dict(d_data2, C1),
                        function)
       return y


def get_value_of(name, data_name, key):
       dict_ = dt.get_words(name, data_name)
       return dt.get(dict_,key)

def get_key(dict_, num):
       return list(dict_.keys())[num]
def keys(name, data_name):
       dict_ = dt.get_words(name, data_name)
       return list(dict_.keys())
#books = dt.get_all_books()
#books = dt.get_books_by("Толстой Лев Николаевич", prop='author')
#books = ["Толстой Лев Николаевич#Война и мир#1",# "Толстой Лев Николаевич#Война и мир#2",
         #"Толстой Лев Николаевич#Война и мир#3", "Толстой Лев Николаевич#Война и мир#4",
         #"Толстой Лев Николаевич#Анна Каренина", "Тургенев Иван Сергеевич#Отцы и дети",
#         "Достоевский Федор Михайлович#Преступление и наказание", "Неизвестный автор#Война и мир"]



def words_num(name):
       return len(dt.get_words(name))

































if __name__ == '__main__':
      book_pairs=[("Толстой Лев Николаевич#Война и мир#1", "Достоевский Федор Михайлович#Преступление и наказание"),
            ("Толстой Лев Николаевич#Война и мир#2", "Толстой Лев Николаевич#Война и мир#1"),
            ("Толстой Лев Николаевич#Война и мир#1", "Толстой Лев Николаевич#Анна Каренина"),
            ('Толстой Лев Николаевич#Война и мир#1', 'Стругацкие#Сборник-1'),
            ("Толстой Лев Николаевич#Анна Каренина",'Стругацкие#Сборник-1'),
            ("Достоевский Федор Михайлович#Преступление и наказание",'Стругацкие#Сборник-1'),
            ("Достоевский Федор Михайлович#Преступление и наказание", "Тургенев Иван Сергеевич#Отцы и дети"),
            ('Толстой Лев Николаевич#Война и мир#1',"Тургенев Иван Сергеевич#Отцы и дети")]
      book_pairs=[('Пушкин Александр Сергеевич#Евгений Онегин', 'Ершов#Конек-горбунок'),
                  ('Пушкин Александр Сергеевич#Сказка о царе Салтане', 'Ершов#Конек-горбунок'),
                  ('Пушкин Александр Сергеевич#Сказка о попе и о работнике его Балде', 'Ершов#Конек-горбунок'),
                  ('Пушкин Александр Сергеевич#Руслан и Людмила', 'Ершов#Конек-горбунок'),
                  ('Пушкин Александр Сергеевич#Евгений Онегин', 'Пушкин Александр Сергеевич#Сказка о царе Салтане'),
                  ('Пушкин Александр Сергеевич#Руслан и Людмила', 'Пушкин Александр Сергеевич#Евгений Онегин'),
                  ('Ершов#Конек-горбунок', 'Гомер#Одиссея'),
                  ('Ершов#Конек-горбунок', "Толстой Лев Николаевич#Война и мир#1"),
                  ('Пушкин Александр Сергеевич#Сказка о царе Салтане', "Толстой Лев Николаевич#Война и мир#1"),
                  ('Стругацкие#Сборник-1', "Тургенев Иван Сергеевич#Отцы и дети")]
      all_y = {}
      for i in book_pairs:
             
             print(i[0], i[1], diff(i[0], i[1], by = 'grammatics', function = SQUARE_FUNCTION))


