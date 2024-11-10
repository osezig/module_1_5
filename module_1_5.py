from tuple import tuple_

immutable_var = (13, True, 'some text')
print(immutable_var)
# Кортежи (тип tuple) — это неизменяемый тип данных в Python,
# который используется для хранения упорядоченной последовательности элементов

mutable_list = [1, 2, 17], 'sergey', 77
mutable_list[0][2] = 111
print(mutable_list)