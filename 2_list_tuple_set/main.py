# lista - modyfikowalna
x: list[int] = [1, 2, 3,]
x.append(3)
x = x + [4]
x.remove(2)
print(sum(x))
print(type(x))
print(x)

# touple - niemodyfikowalne
tuple: tuple = (1, 2, 'asd')
print(type(tuple))
print(tuple)

# set - kolejność nie jest zapewniona, unikalne wartości
set = {1, 2, 'asd', 2}
set.add('ssss')
set.update(['onion', 'carrot'])
print(type(set))
print(set)