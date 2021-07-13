# region class
#
# class Cat:
#     pass
#
# MyCat=Cat()
# print(MyCat,type(MyCat))


###################################
#

# class MyError(Exception):
#     pass
#
#
# try:
#     raise MyError
# except MyError:
#     print('ert')


# class Cat:
#
#     def __init__(self,a,b=4):
#         self.EyeColor=a
#         self.LegsCount=b
#
#     def GetEyeColor(self):
#         return self.EyeColor
#
#     def GetLegsCount(self):
#         return self.LegsCount
# #
# MyCat=Cat('Blue')
# print(MyCat.EyeColor,MyCat.LegsCount)
# YourCat=Cat('Green',3)
# print(YourCat.EyeColor,YourCat.LegsCount)
#
# a='123456789'
# print(a,type(a))

#
# print(MyCat.GetLegsCount())
# print(YourCat.GetLegsCount())
#
# def f():
#     return 56
#
# print(dir(MyCat))
# MyCat.New=f
# print(dir(MyCat))
# print(dir(YourCat))
# print(MyCat.New())
# print(YourCat.New())
################################### inc
#
# class Cat:
#
#     def PrintEyeColor(self):
#         print('Green')
#
#     def _PrintEyeColor1(self):
#         print('Blue')
#
#     def __PrintEyeColor2(self):
#         print('Grey')
#
# a=Cat()
# a.PrintEyeColor()
# a._PrintEyeColor1()
# # a.__PrintEyeColor2()
# a._Cat__PrintEyeColor2()


################################### set/get

# class Cat:
#      def __init__(self, a):
#          self.__age=0
#          self.set_age(a)
#
#      def get_age(self):
#          return self.__age
#
#      def set_age(self, a):
#          if a > self.__age:
#              self.__age = a
#
# p = Cat(5)
# print(p.get_age())
# p.set_age(-35)
# print(p.get_age())
# p.set_age(3)
# print(p.get_age())
# p.set_age(10)
# print(p.get_age())


##################################### Method + Var
#
# class Cat:
#     EyeColor='Green'
#
#     def Test(self):
#         print('123')
#         self.TestVar=100
#
# MyCat=Cat()
# print(MyCat,type(MyCat))
# #
# print(dir(Cat))
# print(dir(MyCat))
# MyCat.Test()
# print(dir(Cat))
# print(dir(MyCat))

##################################### init
#
# class Cat:
#
#     def __init__(self):
#         self.EyeColor='NoColor'
#
#     def GetEyeColor(self):
#         return self.EyeColor
#
#     def SetEyeColor(self,a):
#         self.EyeColor=a
#
# MyCat=Cat()
# print(MyCat,type(MyCat))
#
#
# print(dir(Cat))
# print(dir(MyCat))
#
# print(1,MyCat.EyeColor)
# print(2,MyCat.GetEyeColor())
# MyCat.SetEyeColor('Blue')
# print(3,MyCat.EyeColor)
# print(4,MyCat.GetEyeColor())
# MyCat.EyeColor='Red'
# print(5,MyCat.EyeColor)
# print(6,MyCat.GetEyeColor())
# Cat.EyeColor='Grey'
# print(7,MyCat.EyeColor)
# print(8,MyCat.GetEyeColor())
# print(9,Cat.EyeColor)
#
# print(dir(Cat))
# print(dir(MyCat))

##################################### Bound Method

# class Cat:
#
#     def __init__(self):
#         self.Age=0
#
#     def AddAge(self,a):
#         self.Age+=a
#
#     def GetAge(self):
#         return self.Age
#
# MyCat=Cat()
# print(MyCat,type(MyCat))
#
# print(MyCat.GetAge())
# MyCat.AddAge(10)
# print(MyCat.GetAge())
# Cat.AddAge(MyCat,20)
# print(MyCat.GetAge())

##################################### no global var
#
# class Cat:
#
#     def GetEyeColor(self):
#         return self.EyeColor
#
#     def SetEyeColor(self,a):
#         self.EyeColor=a
#
# MyCat=Cat()
# # print(MyCat,type(MyCat))
# #
# print(dir(Cat))
# print(dir(MyCat))
# # # print(1,MyCat.EyeColor)
# # # print(2,MyCat.GetEyeColor())
# MyCat.SetEyeColor('Blue')
# print(dir(Cat))
# print(dir(MyCat))
# print(3,MyCat.EyeColor)
# print(4,MyCat.GetEyeColor())
# MyCat.EyeColor='Red'
# print(5,MyCat.EyeColor)
# print(6,MyCat.GetEyeColor())
# Cat.EyeColor123='Grey'
# print(7,MyCat.EyeColor)
# print(8,MyCat.GetEyeColor())
# print(9,Cat.EyeColor123)
# #
# print(dir(Cat))
# print(dir(MyCat))

##################################### global var
#
# class Cat:
#     EyeColor='Windows'
#
#     def GetEyeColor(self):
#         return self.EyeColor
#
#     def SetEyeColor(self,a):
#         self.EyeColor=a
#
# MyCat=Cat()
# print(MyCat,type(MyCat))
#
# # print(Cat.EyeColor)
# # print(Cat.GetEyeColor()) #!!!!!!
#
# print(dir(Cat))
# print(dir(MyCat))
#
# print(1,MyCat.EyeColor)
# print(2,MyCat.GetEyeColor())
# print(3,Cat.EyeColor)
# MyCat.SetEyeColor('Blue')
# print(4,MyCat.EyeColor)
# print(5,MyCat.GetEyeColor())
# print(6,Cat.EyeColor)
# MyCat.EyeColor='Red'
# print(7,MyCat.EyeColor)
# print(8,MyCat.GetEyeColor())
# print(9,Cat.EyeColor)
# Cat.EyeColor='Grey'
# print(10,MyCat.EyeColor)
# print(11,MyCat.GetEyeColor())
# print(12,Cat.EyeColor)
#
# print(dir(Cat))
# print(dir(MyCat))

##################################### 2 classes + eq
#
# class Cat:
#
#     def __init__(self):
#         self.EyeColor='NoColor'
#
#     def GetEyeColor(self):
#         return self.EyeColor
#
#     def SetEyeColor(self,a):
#         self.EyeColor=a
#
#     def __eq__(self, other):
#         if self.EyeColor==other.EyeColor:
#             return True
#         else:
#             return False
#
#     # def __add__(self,other):
#     #     return 123
#
#
# print('Cat',dir(Cat),sep='\n')
# MyCat=Cat()
# YourCat=Cat()
# print('Cat',dir(Cat),sep='\n')
# print('MyCat',dir(MyCat),sep='\n')
# print('YourCat',dir(YourCat),sep='\n')
# MyCat.SetEyeColor('Blue')
# YourCat.SetEyeColor('Blue')
# Cat.EyeColor='Red'
# print('Cat',dir(Cat),sep='\n')
# print('MyCat',dir(MyCat),sep='\n')
# print('YourCat',dir(YourCat),sep='\n')
# print(MyCat.EyeColor,MyCat.GetEyeColor())
# print(YourCat.EyeColor,YourCat.GetEyeColor())
# print(Cat.EyeColor)
#
# print(MyCat==YourCat)
# print(1==2)
# print('123'=='123')
# # print(123>20)

##################################### legacy 1

# class MyList(list):
#
#     def isEvenLength(self):
#         return len(self)%2==0
#
#     # def __repr__(self):
#     #     return 'TEWGSFD'
#     #
#
#     def __
#
# a=MyList()
# print(a,type(a))
# [a.append(i) for i in range(10)]
# print(a,type(a))
#
# b=MyList()
# print(b,type(b))
# [b.append(i) for i in range(20)]
# print(b,type(b))
#
# print(a==b)

# print(a.isEvenLength())


# # # print(MyList.mro())

##################################### legacy 2
#
# class A: pass
# class B: pass
# class C: pass
# class D (A,B): pass
# class E(C): pass
# class F(D,E): pass
# class G: pass
#
# print(issubclass(F,A))
# # print(issubclass(F,G))
# a=A()
# f=F()
# d=D()
# print(isinstance(f,A))
# print(isinstance(f,D))
# print(isinstance(f,G))
#
# print(F.mro())


##################################### legacy 3
#
# class Animal:
#     def __init__(self):
#         self.__FurColor='NoColor'
#
#     def SetFurColor(self,a):
#         self.__FurColor=a
#
#     def GetFurColor(self):
#         return self.__FurColor
#
# class Cat(Animal):
#
#     def __init__(self):
#         self.__EyeColor='NoColor'
#         super(Cat,self).__init__()
#
#     def SetEyeColor(self,a):
#         self.__EyeColor=a
#
#     def GetEyeColor(self):
#         return self.__EyeColor
#
# a=Cat()
# print(a.GetEyeColor())
# a.SetEyeColor('Green')
# print(a.GetEyeColor())
#
# print(a.GetFurColor())
# a.SetFurColor('Blue')
# print(a.GetFurColor())

##################################### error
#
# class BadSituation(Exception):
#     pass
#
#
# try:
#     a=10
#     print(10 / 0)
#     if a<100:
#         raise BadSituation('Ooops')
#
#
# except BadSituation as e:
#     print(123)
# except ZeroDivisionError as r:
#     print(234)

# endregion
##########
# region import



#
# print(dir())
# import MyModule as m
# print(dir())
# m.CheckImport()
# m.Again()
# # # print(ModVar)#!!!!!!
# print(m.ModVar)

# print(dir())
# from MyModule import Again as A
# print(dir())
# A()

# print(dir())
# from MyModule import *
# print(dir())
# Again()
# print(ModVar)
# print(_a)

print(dir())
import MyModule as ert
print(dir())
# print(ert._a)

##########################################
#
# print(dir())
# import TestPackage as t
# print(dir())
# print(t.a)
# t.GoodFunc.f1()
# t.AnotherFunc.g1() #!!!!!!!

# print(dir())
# import TestPackage.AnotherFunc as t
# print(dir())
# t.g1()
# t.g2()
#
# print(dir())
# from TestPackage import *
# print(dir())

# print(dir())
# from TestPackage import MoreFunc
# print(dir())
# MoreFunc.k1()

# print(dir())
# from TestPackage.MoreFunc import *
# print(dir())

print(dir())
from TestPackage.MoreFunc import k1 as NewF
print(dir())
NewF()

# endregion