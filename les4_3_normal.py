# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random


file = open(r'd:\digit.txt', 'w')

file.close

i = 0

file = ''

while i <= 20 - 1:
    
    i += 1
    
    num = str(random.randint(0,9))
            
    file = open(r'd:\digit.txt', 'a')
        
    file.write(num)

file.close


    




   
