import zlib 
s  = 'ejemplo raul armasdfafafadfsadfsfdsfsfsfdsaffsdfsadfafsd'
print(len(s))

t = zlib.compress(s.encode('utf-8'))
print(len(t))

#tener cuidado con probar este test con cadenas muy cortas
#lo cual probablemente no proporciona suficiente repetición de patrones o redundancia para que el algoritmo de compresión de zlib sea efectivo