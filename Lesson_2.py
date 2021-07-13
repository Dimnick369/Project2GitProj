# import keyword
# print(keyword.kwlist)
#
a,b = 3,4
# a=b=3
c='10'
d='20'
e=6.5
k=12.9

# region add
# print(a+b,type(a+b)) #OK
# print(b+a,type(b+a)) #OK
# print('____________')
# print(a+c,type(a+c)) #Mistake
# print(c+a,type(c+a)) #Mistake
# print('____________')
# print(a+e,type(a+e)) #OK
# print(e+a,type(e+a)) #OK
# print('____________')
# print(c+d,type(c+d)) #OK
# print(d+c,type(d+c)) #OK
# print('____________')
# print(c+e,type(c+e)) #Mistake
# print(e+c,type(e+c)) #Mistake
# print('____________')
# print(k+e,type(k+e)) #OK
# print(e+k,type(e+k)) #OK
# # print('____________')
# print(0.3+0.3+0.3) # !!!!!!!
# endregion
#############################################################################################
# region subtr
# print(a-b,type(a-b)) #OK
# print(b-a,type(b-a)) #OK
# print('____________')
# print(a-c,type(a-c)) #Mistake
# print(c-a,type(c-a)) #Mistake
# print('____________')
# print(a-e,type(a-e)) #OK
# print(e-a,type(e-a)) #OK
# print('____________')
# print(c-d,type(c-d)) #Mistake
# print(d-c,type(d-c)) #Mistake
# print('____________')
# print(c-e,type(c-e)) #Mistake
# print(e-c,type(e-c)) #Mistake
# print('____________')
# print(k-e,type(k-e)) #OK
# print(e-k,type(e-k)) #OK
# print('____________')
# print (9**19-int(float(9**19))) # !!!!!
# endregion
#############################################################################################
# region mul
# print(a*b,type(a*b)) #OK
# print(b*a,type(b*a)) #OK
# print('____________')
# print(a*c,type(a*c)) #OK
# print(c*a,type(c*a)) #OK
# print('____________')
# print(a*e,type(a*e)) #OK
# print(e*a,type(e*a)) #OK
# print('____________')
# print(c*d,type(c*d)) #Mistake
# print(d*c,type(d*c)) #Mistake
# print('____________')
# print(c*e,type(c*e)) #Mistake
# print(e*c,type(e*c)) #Mistake
# print('____________')
# print(k*e,typee(k*e)) #OK
# print(e*k,type(e*k)) #OK
# print('____________')
# print (0.3*3) # !!!!!
# endregion
#############################################################################################
# region div
# print(a/b,type(a/b)) #OK
# print(b/a,type(b/a)) #OK. Amount after dot !
# print('____________')
# print(a/c,type(a/c)) #Mistake
# print(c/a,type(c/a)) #Mistake
# print('____________')
# print(a/e,type(a/e)) #OK
# print(e/a,type(e/a)) #OK
# print('____________')
# print(c/d,type(c/d)) #Mistake
# print(d/c,type(d/c)) #Mistake
# print('____________')
# print(c/e,type(c/e)) #Mistake
# print(e/c,type(e/c)) #Mistake
# print('____________')
# print(k/e,type(k/e)) #OK
# print('{:.15f}'.format(k/e),type(k/e)) #OK
# print('{:.20f}'.format(k/e),type(k/e)) #OK
# print(e/k,type(e/k)) #OK
# print('____________')
# endregion
#############################################################################################
# region div 2
# print(a//b,type(a//b)) #OK
# print(b//a,type(b//a)) #OK
# print('____________')
# print(a//c,type(a//c)) #Mistake
# print(c//a,type(c//a)) #Mistake
# print('____________')
# print(a//e,type(a//e)) #OK
# print(e//a,type(e//a)) #OK
# print('____________')
# print(c//d,type(c//d)) #Mistake
# print(d//c,type(d//c)) #Mistake
# print('____________')
# print(c//e,type(c//e)) #Mistake
# print(e//c,type(e//c)) #Mistake
# print('____________')
# print(k//e,type(k//e)) #OK
# print(e//k,type(e//k)) #OK
# print('____________')
# endregion
#############################################################################################
# region remainder
# print(a%b,type(a%b)) #OK
# print(b%a,type(b%a)) #OK
# print('____________')
# print(a%c,type(a%c)) #Mistake
# print(c%a,type(c%a)) #Mistake
# print('____________')
# print(a%e,type(a%e)) #OK
# print(e%a,type(e%a)) #OK
# print('____________')
# print(c%d,type(c%d)) #Mistake
# print(d%c,type(d%c)) #Mistake
# print('____________')
# print(c%e,type(c%e)) #Mistake
# print(e%c,type(e%c)) #Mistake
# print('____________')
# print(k%e,type(k%e)) #OK
# print(e%k,type(e%k)) #OK
# print('____________')


# a//b=q with remainder r

# endregion
#############################################################################################
# region complex
# print(5e-1)
# print(5e1)
# print((5e-1+5e1)*2)
# print((5e-1+0.5+1)*2)
# endregion
#############################################################################################
# region power
# print(-9**2) #!!!!
# endregion
#############################################################################################
# region unexpected minus !
# print(42/8,42//8,42%8)
# print(-42/-8,-42//-8,-42%-8)
# print(-42/8,-42//8,-42%8)
# print(42/-8,42//-8,42%-8)

# a//b=q with remainder r
# b*q+r=a

# endregion
#############################################################################################
# region dif base
# print(0b1101011)
# print(0o15)
# print(0xFB + 0b10)
# print(hex(12),oct(12),bin(12))
# endregion
#############################################################################################
# region id
# a=15**32
# b=15**32
# print(id(a),id(b),sep='\n')
# print(a)
# print('ZZZZZZZZZZZZZZZZZZZZ')
# a=8
# b=a
# a,b=a+1,b+1
# print(id(a),id(b),sep='\n')
# print(a)
# print('ZZZZZZZZZZZZZZZZZZZZ')
# a=1334
# b=a
# a,b=a+1,b+1
# print(id(a),id(b),sep='\n')
# print(a)
# endregion
