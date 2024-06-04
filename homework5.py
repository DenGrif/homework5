immutable_var = 1, 2, 'a', 'b'
print(immutable_var)

print(immutable_var[0])
# immutable_var[0] = 5 При такой команде выходит сообщение:
# TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, 'a', 'b', 'Modified']
print(mutable_list)
mutable_list[0] = 4
print(mutable_list)
mutable_list[2] = 'Z'
print(mutable_list) # в квадратных скобках спиcок, а он изменяемый