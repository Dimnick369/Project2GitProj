# region format
# name='Hello,' + 'Test'
# print('Hello, %s' % name)
# exec ('print(1)')
# errno = 50159747054
# name = 'Bob'
# print('Hey %s, there is a 0x%x error!' % (name, errno))
#
# print(
#     'Hey %(name)s, there is a 0x%(errno)x error!' % {
#         "name": name, "errno": errno
#     }
# )

##############################
# errno1 = 50159747054
# name1 = 'Bob'
# print(
#     'Hey {name}, there is a 0x{errno:x} error!'.format(
#         name=name1, errno=errno1
#     )
# )
##############################
#
# a = 5
# b = 10
# print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')
##############################
# from string import Template
# name='Test'
# t = Template('Hey, $name!')
# print(t.substitute(name=name))

#Examples
# a=3
# b='3'
# c='centered'
# #
# print('{:*^30}'.format(c))
# print(c.center(30,'*'))
# endregion
#####################################################
# region regexp
import re as r

# patt=r'a[ac]c'
# st='acc acc adc a2c'
# match_ob=r.match(patt,st)
# print(match_ob)
#
# patt=r'a[cb]c'
# st='abc acc adc acc a2c'
# match_ob2=r.search(patt,st)
# print(match_ob2)


patt=r'YY\(\w*\)YY'
st='12345YYYYadfsdf 12345YY(1)YYadfsdf 12345YYfgjhfgYYadfsdf'
match_ob3=r.findall(patt,st)
print(match_ob3)
#
# patt=r'a[a-zA-Z]c'
# st='abc acc adc a2c'
# match_ob4=r.sub(patt,'123',st)
# print(match_ob4,type(match_ob3))
################################

# patt='a[ab]+a'
# patt='a[ab]+?a' #не жадный способ
# st='abaaba'
# match_ob=r.match(patt,st)
# print(match_ob)
# match_ob=r.findall(patt,st)
# print(match_ob)
################################

# patt=r'(a(test)+c)'
# st='atestc ac atesttestc a2c'
# match_ob3=r.findall(patt,st)
# print(match_ob3)

################################
#
# x=r.match(r'text','TEXT',r.DEBUG)
# print(x)
################################

# # (\w+)-\1
# str='test-test chow-chow ft-rtr'
# pat=r'(\w+)-\1'
# print(r.sub(pat,r'\1',str))

# endregion
