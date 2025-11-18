'''
17. Ejercicio. 
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.  El tiempo de 
viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora 
de llegada a la ciudad B.º
'''
hh_salida = 13
mm_salida = 30
ss_salida = 45
t_viaje = 808069

# Convertimos la hora de salida a segundos
total_segundos_salida = hh_salida * 3600 + mm_salida * 60 + ss_salida

# Sumamos el tiempo de viaje
segundos_llegada = total_segundos_salida + t_viaje

# Convertimos de nuevo a HH:MM:SS
hora_llegada = (segundos_llegada // 3600) % 24
mm_llegada = (segundos_llegada % 3600) // 60
ss_llegada = segundos_llegada % 60

print(f"Hora de llegada: {hora_llegada:02d}:{mm_llegada:02d}:{ss_llegada:02d}")
