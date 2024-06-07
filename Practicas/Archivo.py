#LECTURA
#absoluta= "C:\\Users\\Carlos\\Desktop\\PROYECTOS-PRACTICAS\\Practicas\\Hola.txt"
#relativa="Practicas\\Hola.txt"
#archivo=open(relativa, "r")
#print(archivo.read())
#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readlines())
#for line in archivo.readlines():
#   print (line)
#ESCRITURA
#relativa2="Practicas\\Hola2.txt"
#archivo2=open(relativa2,"w")
#archivo2.write("C#\nVB.NER\nASP.NET")
#LECTO-ESCRITURA
relativa3="Practicas\\Hola3.txt"
archivo3=open(relativa3,"r+")
archivo3.write("Hola\nComo\nEstas")
archivo3.seek(0)
print(archivo3.read())
#CARACTERES DE AUTORIZACIONES 
#"x" crea un archivo para escritura, si el archivo existe marca error
#"a" crea un archivo para escritura, si el archivo existe marca el puntero se ubica al final del contenido