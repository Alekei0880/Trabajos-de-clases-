#CLASE 4
#e = ["Nombre", "Est Dt", "Prog Func", "Ingles"]
#alumnos = ["Alex", "Paola", "Sergio","Kai"]
#m_e_d = [8,7,5,9]
#m_p_f = [5,10,9,7]
#m_i = [6,5,9,10]
#
#def reporte (fmt:int):
#    print(f"{e[0]:^{fmt}}{e[1]:^{fmt}}{e[2]:^{fmt}}{e[3]:^{fmt}}")
#    for i in range(len(alumnos)):
##        print(f"{alumnos[i]:^{fmt}}{m_e_d[i]:^{fmt}}{m_p_f[i]:^{fmt}}{m_i[i]:^{fmt}}")
##    
##if __name__=="__main__":
##    reporte(12)
#
##SEPARACION CON COMAS
#numeroBig=12345678900987654321
#print(f"{numeroBig:,d}")
#
##FIJAR CANTIDAD DE DECIMALES
#numeroPI=3.141578765468765447
#print(f"{numeroPI:.3f}")
#
##NOTACION CIENTIFICA
#numeroPI= 314.1243
#print(f"{numeroPI:e}")
#print(f"{numeroPI:.2e}")
#
##PORCENTAJE
#numeroPorciento = 0.2582354235
#print(f"{numeroPorciento:%}")
#print(f"{numeroPorciento:.2%}")
#
##NUMEROS BINARIOS
#print(f"{25:b}")
#
##UNICODES
#print(f"{65:c}")
#
##HEXADECIMAL
#print(f"{255:x}")
#
##OCTAL
#print(f"{255:o}")
#
#
"""
Escriba una función que genere una tabla de multiplicar 
recibiendo la cantidad de números y la tabla a generar
"""
#from __future__ import print_function
#
#def tablas (m:int,n:int,t:int):
#    for i in range(1,m+1):
#        tabla(n,i)
#
#def tabla(n:int,t:int):
#    for i in range(1,n+1):
#        print(i,"x",t, "=", i*t)
#    print("\n")
#
#
#if __name__== "__main__":
#    tablas(3,10,10)
