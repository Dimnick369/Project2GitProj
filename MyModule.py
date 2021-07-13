def CheckImport():
    print('CheckImport')

def Again():
    print('Again')

def Test1():
    print('Test1')


ModVar='Base'
# b=f'Test temple {ModVar}'
_a=[1,2,3,4,5,6,7,8,9]
# #
# #
__all__=['CheckImport','Again']
# # # __all__=['CheckImport','Again','Test1']
# # __all__=['CheckImport','Again','ModVar','b','_a']
# #
# #

print(__name__)

if __name__ == "__main__":
    print('I am personal module')
    print(__name__)

