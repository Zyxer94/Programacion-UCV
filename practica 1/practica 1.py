Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###======== Practica 1 ========###

###=== Datos tipo numericos ===###

### int ###

entero_1 = 20
type(entero_1)
<class 'int'>

### float ###

float_1, float_2, float_3 = 0.348, 10.5, 1.5e2
print(float_1)
0.348
print(float_2)
10.5
print(float_3)
150.0
type(float_1)
<class 'float'>

### complex ###

complejo_1 = 2.1 +7.8j
type(complejo_1)
<class 'complex'>
print(complejo_1.imag)
7.8
print(complejo_1.real)
2.1
abs(complejo_1)
8.077747210701755

###=== Datos tipo booleano ===###
False
False
False == False
True
0 == False
True
"" == False
False
None = False
SyntaxError: cannot assign to None
None == False
False
[] == False
False
() == False
False
{} == False
False
['' , ''] == False
False
int(False)
0
int(True)
1
type (True)
<class 'bool'>
str(True)
'True'
type(str(True))
<class 'str'>
type(False)
<class 'bool'>
type(str(False))
<class 'str'>

###=== Datos tipo arreglo ===###

### list ###

factura = ['pan', 'huevos', 100, 1234]
factura
['pan', 'huevos', 100, 1234]
factura[0]
'pan'
factura[3]
1234
len(factura)
4
len(factura) -
SyntaxError: incomplete input
len(factura) - 1
3
factura[-1]
1234
factura[-len(factura)]
'pan'
factura[1] = "carne"
factura
['pan', 'carne', 100, 1234]



versiones_plone = [2.5, 3.6, 4, 5]
print(versiones_plone)
[2.5, 3.6, 4, 5]
versiones_plone.append(6)
print(versiones_plone)
[2.5, 3.6, 4, 5, 6]



versiones_plone = [2.1, 2.5, 3.6, 4, 5, 5, 6]
print(versiones_plone.count(6))
1
print(versiones_plone.count(5))
2



versiones_plone = [2.1, 2.5, 3.6]
print(versiones_plone)
[2.1, 2.5, 3.6]
versiones_plone.extend([4])
print(versiones_plone)
[2.1, 2.5, 3.6, 4]
[2.1, 2.5, 3.6, 4]
[2.1, 2.5, 3.6, 4]

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
versiones_plone.index(4)
3
print(versiones_plone.index(4))
3
>>> 
>>> 
>>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
>>> versiones_plone.insert(2, 3.47)
>>> print (versiones_plone)
[2.1, 2.5, 3.47, 3.6, 4, 5, 6]
>>> print(versiones_plone)
[2.1, 2.5, 3.47, 3.6, 4, 5, 6]
>>> versiones_plone.insert(2, 3.7)
>>> print(versiones_plone)
[2.1, 2.5, 3.7, 3.47, 3.6, 4, 5, 6]
>>> 
>>> 
>>> versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6]
>>> print(versiones_plone)
[4, 2.5, 5, 3.6, 2.1, 6]
>>> versiones_plone.sort()
>>> print(versiones_plone)
[2.1, 2.5, 3.6, 4, 5, 6]
>>> 
>>> ###=== Datos de tipo String ===###
>>> 
>>> ### str ###
>>> 
>>> 'Hola Mundo'
'Hola Mundo'
>>> hla_mnd = 'Hola Mundo'
>>> a, b = "uno", "dos"
>>> a + b
'unodos'
>>> c = "tres"
>>> c*3
'trestrestres'
>>> tipo_calculo = "raiz cuadrada de dos"
>>> valor = 2**0.5
>>> print("el resultado de {} es {}".format(tipo_calculo,, valor))
SyntaxError: invalid syntax
>>> print("el resultado de {} es {}".format(tipo_calculo, valor))
el resultado de raiz cuadrada de dos es 1.4142135623730951
