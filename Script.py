nombre = list(range(101))
multi_3 = list(range(0, 101, 3))
multi_5 = list(range(0, 101, 5))


for i in nombre :
    if i in multi_3 and i in multi_5 :
        nombre[i] = "FizzBuzz"
    elif i in multi_3 :
        nombre[i] = "Buzz"
    elif i in multi_5 :
        nombre[i] = "Fizz"
    else:
        nombre[i] = i

print(nombre)