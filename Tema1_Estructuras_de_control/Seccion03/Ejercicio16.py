'''
16. Ejercicio. 
Dos  vehículos  viajan  a  diferentes  velocidades  (v1  y  v2)  y  están  distanciados  por  una 
distancia  d.  El  que  está  detrás  viaja  a  una  velocidad  mayor.  Se  pide  hacer  un  algoritmo  para 
ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto 
determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
'''
v1 = 80 #velocidad veiculo 1
v2 = 100 #velocidad veiculo 2
d = 30 #distancia
v_relativa = v2 - v1 #restamos para sacar la velocidad relativa
t = d/v_relativa #para conseguir el tiempo solo tenemos que calcular con esa velocidadrelativa cuanto tiempo tardara el veiculo 2 en recorrer esa distancia
tmin = t * 60 #comvertimos por ultimo de horas a minutos
print(f"tardara el veiculo 2 en alcanzar al veiculo 1: {tmin} minutos")