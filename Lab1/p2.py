# a = [10,9,12,15,18]
# b = [21,8,15,3,12]
a = [10,9,12,15,18]
b = [21,8,15,3,12]
c = [4,5,6]
total = a+b
print(total)
total.insert(1,20)
print(total)
print(set(total))
total2 =total+c
print(total2)
suma = 10+9+12+15+18+21+8+15+3+12+20+4+5+6
print("la suma es" , suma)
import statistics
print("la media es ", statistics.mean(total2))
print("la mediana es ", statistics.median(total2))

