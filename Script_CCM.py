from datetime import datetime
saludo = datetime.now().hour
if 5 <= saludo < 12:
    print ("Hola, buenos días")
elif 12 <= saludo < 18:
    print ("Hola, buenas tardes")
else:
    print ("Hola, buenas noches")
print("Bienvenido al sistema de gestión para cálculo de instalaciones eléctricas.")
print("Por favor, seleccione una opción del menú:")