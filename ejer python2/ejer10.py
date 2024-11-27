edad = int(input("ingrese su edad:"))
sexo = input("ingrese su sexo (femenino o  masculino): ")
estadoCivil = input("ingrese su estado civil (casado(a), soltero(a), separado(a) o otro.): ")
if edad < 17 :
    print("Usted no puede votar ")
elif edad > 17 and estadoCivil == "casada"   and sexo =="femenino":
    print("usted puede votar en la mesa N1")
elif edad > 17 and estadoCivil == "soltera"  and sexo =="femenino":
    print("usted puede votar en la mesa N2")
elif edad > 17 and estadoCivil == "separada" and sexo =="femenino":
    print("usted puede votar en la mesa N3")
elif edad > 17 and estadoCivil == "otro" and sexo =="femenino":
    print("usted puede votar en la mesa N4")
elif edad > 17 and estadoCivil == "casado"   and sexo =="masculino":
    print("usted puede votar en la mesa N5")
elif edad > 17 and estadoCivil == "soltero"  and sexo =="masculino":
    print("usted puede votar en la mesa N6")
elif edad > 17 and estadoCivil == "separado" and sexo =="masculino":
    print("usted puede votar en la mesa N7")
elif edad > 17 and estadoCivil == "otro" and sexo =="masculino":
    print("usted puede votar en la mesa N8")