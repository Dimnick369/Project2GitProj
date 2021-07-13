# region byte strings

# print('Hello')
# print(b'Hello')
# #
# print('Мама')
# print(b'Мама')
############################################
# a=list(b'Hello  ')
# print(a)
############################################
# print( 'I am a string'.encode('ASCII') )
# print(b'I am a string'.decode('ASCII') )
############################################
# a= b'Hello'
# print(a)
# for i in a:
#     print(i)
############################################
# a= 'мама       привет'.encode('utf-8')
# print(a,type(a))
# for i in a:
#     print(i)
############################################
# a='Мамо'
# b=a.encode('utf-8')  #rus
# c=a.encode('cp1125') #ukr
# print(b)
# print(c)
############################################
# c=bytes(range(256))
# print(c)
# for i in c :
#     print(i,chr(i))
# # endregion
##################################################
#################
# region files

############################ Write
f = open('text.txt', 'w')
f.write('    Hello')
f.write('Имя')
f.write('1234\t5     67890')
f.write('Hello\n')
f.write('Имя\n')
f.write('1234567890\n')
f.close()

##################### print in file
# f = open('text1.txt', 'w')
# print('str1','str2',file=f,sep='ZZZZ',end='\n')
# print('str3','str4',file=f)
# f.close()
############################ Read
# f = open('text.txt', 'r')
# g=f.read()
# print(g,type(g), end='')
# f.close()
######################
# f = open('text.txt', 'r')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# f.close()
######################
# f = open('text.txt', 'r')
# print(f.readlines(), end='')
# f.close()
######################
# f = open('text.txt', 'r')
# for i in f:
#     # print(i)
#     print(i, end='') #!!!!!
# f.close()
############################ Context Manager

# with open('text.txt', 'r') as f:
#     print(f.readline(),end='')
#
############################ Read only ones
# with open('text.txt', 'r') as f:
#     print(f.readlines(),end='')
#     print(f.readlines(), end='') #!!!!!!!!!
#

############################ Read bytes
# with open('1.png', 'r') as f:
#     z=f.read()
#
# with open('1.png', 'rb') as f:
#     z=f.read()
#     print(z)

# with open('1b.txt', 'r') as f:
#     z=f.read()

####################################
#
# a='Мамо'
# b=a.encode('utf-8')  #rus
# c=a.encode('cp1125') #ukr
# print(b)
# print(c)
# #
# with open('text2.txt', 'wb') as f:
#     f.write(b)
#     # f.write(c)
# # #
# # # print('ZZZZZZZZZ')
# # #
# with open('text2.txt', 'rb') as f:
#     print(f.read())
#
# with open('text2.txt', 'r') as f:
#     print(f.read())
#############################    Useful command
#
with open('text.txt', 'r') as f:
    for i in f:
        print(i,type(i))
        i=i.strip('lo\n H')
        print(i,type(i))
#
# with open('text.txt', 'r') as f:
# # with open('text1.txt', 'r') as f:
#     i=f.readlines()
# #
# print(i)
# for k in range(len(i)):
#     i[k]=i[k].strip()
# print(i)
###################################### os.path
import os
# print(os.path.join('Disk','dir1','filename.type'))
# print(os.getcwd())
# print(os.listdir())
#
# print(os.path.exists(os.path.join(os.getcwd(),'main.py')))
# print(os.path.exists(os.path.join(os.getcwd(),'main1.py')))
#
# print(os.path.isfile(os.path.join(os.getcwd(),'main.py')))
# print(os.path.isdir(os.path.join(os.getcwd(),'main.py')))

# print(os.path.abspath('main.py'))

########################## walk
# print(os.getcwd())
# os.chdir('Venv')
# print(os.getcwd())
#
# for cur_dir,dirs,files in os.walk(('.')):
#     print(cur_dir,dirs,files,sep='')
#     print('Next Level')
########################## copy

# import shutil
#
# shutil.copy('src','dst')

# endregion
