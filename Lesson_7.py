# region  stars

# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# # print(more_numbers[0], sep=',ZZ ')
# print(more_numbers, sep=',ZZ ')
# print(*more_numbers, sep=',ZZ ')

########################################
#
# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# numbers = [2, 1, 3, 4, 7]
# print(numbers, fruits ,sep=' Z ')

########################################
#
# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
#
# first, second, *remaining = fruits
#
# print(first, second, remaining)
# first, *middle, last = fruits
# print(first, middle, last)

########################################

# date_info = {'year': "2020", 'month': "01", 'day': "01"}
# filename = "{year}-{month}-{day}.txt".format(**date_info)
# print(filename)
# print(date_info.items())
# print(*date_info.items())
# ########################################
#
# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# first, second, *remaining = fruits
#
# first_word, *other_fruits = fruits
# print(first_word,other_fruits)
#
# first_letter, *remaining=first_word
# print(first_letter,remaining)
#
# (first_letter, *remaining), *other_fruits = fruits
# print(first_letter,remaining,other_fruits)
#
# # (first_letter, *remaining, last_letter ), *other_fruits = fruits
# # print(first_letter,remaining,last_letter,other_fruits)
#
# (first_letter, *remaining),(), *other_fruits = fruits
# print(first_letter,remaining,first_letter2,remaining2,other_fruits)

########################################

# def palindromify(sequence):
#     return list(sequence) + list(reversed(sequence)[])
#
# def palindromify1(sequence):
#     return [*sequence, *reversed(sequence)]
#
# print(palindromify([1,2,3,4,5]))
# print(palindromify1([1,2,3,4,5]))

########################################

# def rotate_first_item(sequence):
#     return [*sequence[1:], sequence[0]]


# endregion
# region func
#
# def min2(a,b):
#     if a<b:
#         return a
#     else:
#         return b
#
# res=min2(5,10)
#
# print(min2(12,8))
# print(min2(min2(3,2),1))

################################ Без возврата

# def mess(a):
#     print(f'Hello gdfsewrethyrt efger {a}')
#     # return
#
# mess('Dima')

################################ Произвольное число параметров

# def min2(*a):
#     m=a[0]
#
#     for i in a:
#         if i <m:
#             m=i
#
#     return m
#
# # print(min2(12,8,7))
# print(min2([12,3,7,4,2,7,9,1])) #!!!!!!!!!!!!!

################################ Cо значением по умочанию

# def steps(st,end=10,step=1):
#     for i in range(st,end,step):
#         print(i,end=' ')
#
#
# steps(6)
# print('ZZZZZZZZ')
# steps(2,5)
# print('ZZZZZZZZ')
# steps(2,8,2)


################################ Именованные переменные

# def steps(st,end=10,step=1):
#     for i in range(st,end,step):
#         print(i,end=' ')
#
# steps(end = 20, st= 5)
# print('ZZZZZZZZ')

# f(1,2,3,4,5)
# def (a,b=10,*f,g)
#
# f (1,2,3,4,5,6,g=10)
#
# def f (	[positional_args,
# 	[positional_args_with_default,
# 	[*args,
# 	[keyword_only_args+default,
# 	[**args_kw]]]]])

################################ Локальность
# d=100
#
# def init_values():
#     print(d)
#
# init_values()



# def init_values():
#     a=100
#
#
# a=10
# init_values()
# print(a)


# def init_values(b):
#     b.append(100)
#
# a=[10,20]
# init_values(a)
# print(a)


# def init_values(b):
#     b.append(100)
#     b=[200,300,400]
#
# a=[10,20]
# init_values(a)
# print(a)

################################ Глобальность

# def printc():
#     print(a)
#
# a=15
# printc()


# def printc():
#     print(a)
#     a=10
#     print(a)
#
# a=15
# printc()

# endregion