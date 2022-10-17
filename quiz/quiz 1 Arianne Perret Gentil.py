juegos = {
    "Shooter": [
        {
            "id": 1,
            "name": "Overwatch2",
            "price": 60  
        },
        {
            "id": 2,
            "name": "Valorant",
            "price": 0
        },
        {
            "id": 3,
            "name": "Pixel Gun 3D",
            "price": 10
        }
    ],
    "RPG": [
        {
            "id": 4,
            "name": "Pokemon",
            "price": 50  
        },
        {
            "id": 5,
            "name": "Final Fantasy Exvius",
            "price": 0
        }
    ],
    "Open World": [
        {
            "id": 6,
            "name": "Minecraft",
            "price": 60  
        },
        {
            "id": 7,
            "name": "Cyberpunk 2077",
            "price": 60
        },
        {
            "id": 8,
            "name": "GTA V",
            "price": 40
        }
    ],  
}

print ("\n ***     Bienvenido a Metro Team      *** \n ")

while True:
    decisión = int(input("Por favor, escoge una opción válida \n 1- Ver inventario de juegos \n 2- Registrar compra \n 3- Salir"))
    if decisión == 1:
        for opciones in juegos.items():
            print (opciones [1])
            








    if decisión == 2:
        print ("Vamos a proceder a la compra")
        datos = []
        nombre = (str(input("Introduce tu nombre")))
        cédula =(int(input("Introduce tu cédula")))
        id_a_comprar = (int(input("Introduce el ID del juego que deseas comprar")))



    if decisión == 3:
        break 