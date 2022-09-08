x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
def cambia_valor(x):
    x[1][0] = 15
    return x
print(cambia_valor(x))
#2.Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
def cambia_apellido(estudiantes):
    estudiantes[0]['last_name'] = 'Bryant'
    return estudiantes

print(cambia_apellido(estudiantes))
#3.En el directorio_deportes, cambia "Messi" por "Andrés".
def cambia_directorio_deportes(directorio_deportes):
    directorio_deportes['fútbol'][0] = 'Andrés'
    return directorio_deportes

print(cambia_directorio_deportes(directorio_deportes))

#4.Cambia el valor 20 en z a 30.
def cambia_valor4(z):
    z[0]['y'] = 30
    return z

print(cambia_valor4(z))

# -------------------------------------------------

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(estudiantes):
    for x in range(0,len(estudiantes)):
        output = ""
        for key, value in estudiantes[x].items():
            output += f"{key}-{value},"
        print(output)
iterateDictionary(estudiantes)

# -------------------------------------------------

def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        for key, value in some_list[x].items():
            if key == key_name:
                print(value)
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes) 

# -------------------------------------------------

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key, value in dojo.items():
        print(f"{len(value)}{key}")
        for x in range(0, len(value)):
            print(value[x])

printInfo(dojo)