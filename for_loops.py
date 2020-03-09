#PYTHON-FOR-LOOP (SECUENCIAS-CICLOS)

# -> Los ciclos For-loop son un aspecto esencial de cualquier lenguaje de programación.

# -> La declaración "for" de Python itera sobre los elementos de cualquier secuencia 
#   (una lista o un cadena), en el orden en que aparecen en la secuencia.
#
#   esto lo hace asignando valores a la variable iteradora, que puede ser "i" o "x" o lo que sea, desde una secuencia. 

# -> <-

for {variable} in {some-sequence}:

	{python-statements}
	
else:

	{python-statements}
	
# -> <-	

#Ejercicios. realice una descripcion de los siguientes fragmentos de codigo: teniendo en cuenta lo siguiente:

#a)¿que valores asume la variable iteradora?
#b) ¿que tipo de dato es la secuencia sobre la que se itera?
#c) ¿como es flujo que lleva a cabo el fragmento de codigo, ejemplo:
#la variable i asume el valor x,contenido en la secuencia [x,y,z] luego se le suma un valor de 1, 
#luego se almacena en una variable "Total", luego la variable i asume el valor y.  

#1.

for i in [1, 2, 3, 4, 5]:
	print(i)
  
#2
  
 names = ["john", "raj", "lisa"]
for i in names:
	print(i)
  
  
#3

for i in range(5):
	print(i)
	
#4

for i in range(1,6):
  print(i)
  
#5

for i in range(1,6,2):
  print(i)
 
 
#6

for i in range(4,-5,-2):
  print(i)
  
 
 #7
 
 names = ["john", "lisa", "raj", "lisa"]
 
for i in names:

  if i != "lisa":
  
    continue
	
  print(i)
  
print("--end--")

#8

names = ["john", "lisa", "raj", "lisa"]

for i in names:

  if i == "raj":
  
    break
	
  print(i)
  
print("--end--")

#9

names = ["john", "raj", "lisa"]

for i in names:

  print(i) 
else:

  print("for loop condition failed!")
  
 #10
 
 names = ["john", "lisa", "raj", "lisa"]
 
for i in names:

  if i == "raj":
  
    break
	
  print(i)
else:

  print("for loop condition failed!")
  
print("--end--")

#11

distros = ["centos", "redhat", "ubuntu"]

arch = ["32-bit", "64-bit"]

for i in distros:

  for j in arch:
  
    print(i + " " + j)
	
  print("-----------")

#12

multiple_state_lists = [ ["CA","NV","UT"], ["NJ","NY","DE"]]

for state_list in multiple_state_lists:

  for state in state_list:
  
    print state
