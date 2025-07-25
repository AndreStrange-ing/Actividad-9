coleccion = []

def agregar_libros(*nombres):
    for n in nombres:
        libro = {
            "titulo": n,
            "autor": None,
            "genero": None,
            "año": None
        }
        coleccion.append(libro)

def asignar_detalles(nombre, autor, genero, año):
    for l in coleccion:
        if l["titulo"] == nombre:
            l["autor"] = autor
            l["genero"] = genero
            l["año"] = año
            break

def mostrar_biblioteca():
    if not coleccion:
        print("no hay libros en la coleccion")
    else:
        for l in coleccion:
            print("-" * 30)
            print("titulo:", l["titulo"])
            print("autor:", l["autor"])
            print("genero:", l["genero"])
            print("año:", l["año"])
        print("-" * 30)

def buscar_libros(**filtros):
    resultado = coleccion
    if "genero" in filtros:
        resultado = [l for l in resultado if l["genero"] == filtros["genero"]]
    if "autor" in filtros:
        resultado = [l for l in resultado if l["autor"] == filtros["autor"]]
    if "año_max" in filtros:
        resultado = [l for l in resultado if l["año"] is not None and l["año"] <= filtros["año_max"]]

    if not resultado:
        print("no se encontraron libros con esos filtros")
    else:
        for l in resultado:
            print(">>", l["titulo"], "-", l["autor"], "-", l["genero"], "-", l["año"])

agregar_libros("cien años de soledad", "el principito", "don quijote")
asignar_detalles("el principito", "antoine de saint-exupery", "ficcion", 1943)
asignar_detalles("cien años de soledad", "gabriel garcia marquez", "realismo magico", 1967)
asignar_detalles("don quijote", "miguel de cervantes", "clasico", 1605)

mostrar_biblioteca()
buscar_libros(genero="ficcion", año_max=2000)