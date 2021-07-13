# region func2
################################ lambda
# numbers=[1,6,2,5,3,4,-3,-2,-7]
# sorted_numbers = sorted(numbers, key=lambda x:abs(x))
# sorted_numbers = sorted(numbers, key=abs)

################################ map filter

# def ert(x):
#     return x%3==0
#
# a=[i for i in range(20)]
# b=list(filter(lambda x: x%3==0,a))
# b=list(filter(ert,a))
# c=list(map(lambda x: f'Check {x}',a))
# print(a)
# print(b)
# print(c)
# c=[f'Check {i}' for i in a]
# print(c)
################################ zip

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP','asdasd','asdasda','asdasdasd']
# d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']
#
#
# k=zip(d_keys,d_values)
# print(k)
# print('ZZZZZZZZZZ')
# r1 = dict(k)
# print(r1)
# print('ZZZZZZZZZZ')# один проход может быть только
# r1 = list(k)
# print(r1)

########################################

# def transpose_list(list_of_lists):
#     return [list(row) for row in zip(*list_of_lists)]
#
# print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))

######################################## first class func


# def test1():
#     print(123)
#
# a=test1
# a()


# endregion
#####################################################
# region  sort

# a=[
#     [123,234,345],   #1
#     [1,2,3],         #0
#     [5,5,5,5,5,5,5], #7
#     [12345,12345,123456] #3
# ]
#
# a.sort(key=lambda x:' '.join( map(str,x)).count('5') )
# print(a)

# endregion
##################################################
# region decor

# def f():
#     print('Usual func')
#
# def decor(infunc):
#
#     def decorated():
#         print('Begin')
#         infunc()
#         print('End')
#
#     return decorated
#
# f()
# print('###########')
# b=decor(f)
# b()
# print('###########')
# f=decor(f)
# f()

######################################################### deco sugar

# def decor(infunc):
#     def decorated():
#         print('Begin')
#         infunc()
#         print('End')
#
#     return decorated
#
# @decor
# def f():
#     print('Usual func')
#
# f()

######################################################### attrs to deco

# def decor(infunc):
#
#     def decorated(a):
#         print('Begin')
#         if len(a)>6:
#             print('Add ' + a)
#         infunc('wertyujhgfd')
#         # infunc(a)
#         print('End')
#
#     return decorated
#
# @decor2
# @decor1
# @decor
# def f(a):
#     print('Usual func: ' + a)
#
# f('New block')
# print('ZZZZZZZZZZ')
# f('New')

######################################################### universal deco (with stars)
#
# def decor(infunc):
#     def decorated(*a):
#         print('Begin')
#         if len(a)>0:
#             print('Add ' + a[0])
#         infunc(*a)
#         print('End')
#
#     return decorated
#
# @decor
# def f():
#     print('Usual func: ')
#
# @decor
# def f1(a):
#     print('Usual func: '+a)
#
# f()
# print('ZZZZZZZZZZZZZZZZZ')
# f1('New Block')

# endregion
##################################################
# region func

# print(dir())
# a=[1,2,3,4,5]
# b=14
# c='asdf'
# print(dir())
# ########################### Local
# t=18
# tmp='OK'
#
# def f(t):
#     t+=23
#     tmp='NO'
#     print(t,tmp)
#     return t
#
# print(f(t))
# print(t,tmp)
# ########################### NS + Область видимости
# def b():
#     print(2,dir())
#     x=31
#     print(3,dir())
#     def a():
#         print(6,dir())
#         print(x)
#         print(7,dir())
#
#     print(4,dir())
#     a()
#     print(5,dir())
#
# print(1,dir())
# b()
# print(8,dir())
########################### NS2+ Область видимости
# def a():
#     print(3, dir())
#     print(x)
#     print(4, dir())
#
# def b():
#     print(2,dir())
#     x=31
#     a()
#     print(5,dir())
#
# print(1,dir())
# b()
# print(6,dir())


########################### global + nonlocal mode
# x=64
# def b():
#     x=31
#     def a():
#         print(x)
#     a()
# b()
# ############################# global
# x=64
# def b():
#     x=31
#     def a():
#         global x
#         print(x)
#     a()
# b()
############################# nonlocal
# x=64
# def b():
#     x=31
#     def a():
#         nonlocal x
#         x=21
#         print(x)
#     a()
#     print(x)
#
# b()
# print(x)
############################# if+for

# a=10
# if a>5:
#     y=0
# print(y)

# ##############################
# for i in [1,2,3,4]:
#     print(i)
# print(i)
# ##############################
# for i in []:
#     y=0
# print(y)
########################### FacePalm
# print(dir())
#
# def a(c=[2]):
#     c.append(2)
#     print(c)
#
# print(dir())
# a()
# print(dir())
# a()
# print(dir())
# a()
# print(dir())
# a()
# endregion