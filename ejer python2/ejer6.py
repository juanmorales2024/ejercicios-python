bonificacion = float(input("Ingrese el valor de su bonificacion: "))
if bonificacion < 50.000:
    print("su bonificacion le alcanza para  una camara web")
elif bonificacion > 50.000 and bonificacion <= 200.000:
    print("su bonificacion le alcanza para  un subwoofer")
elif bonificacion > 200.000 and bonificacion <= 500.000:
    print("su bonificacion le alcanza para  un DD externo")
elif bonificacion > 500.000 and bonificacion <= 1.000000 :
    print("su bonificacion le alcanza para  una impresora multifuncional")
elif bonificacion >= 1.000000:
    print("su bonificacion le alcanza para  una proyector")
        