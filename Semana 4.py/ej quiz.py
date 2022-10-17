medications = {
        "prescription": {
            "antibiotics": {
                "skin": [
                    {
                        "id": 1,
                        "name": "Clindamicine",
                        "price": 300
                    },
                    {
                        "id": 2,
                        "name": "Cefadroxil",
                        "price": 350
                    },
                    {
                        "id": 3,
                        "name": "Amoxicillin",
                        "price": 320
                    }
                ],
                "respiratory-system":[
                    {
                        "id": 4,
                        "name": "Citromicine",
                        "price": 380
                    },
                    {
                        "id": 5,
                        "name": "Levofloxacine",
                        "price": 125
                    },
                    { "id": 6,
                        "name": "Azitromicine",
                        "price": 740
                    }
                ]
            },
            "analgesic": {
                "anti-inflammatories": [
                    {
                        "id": 7,
                        "name": "HYDROCODONE-IBUPROFEN",
                        "price": 150
                    },
                    {
                        "id": 8,
                        "name": "IBUDONE",
                        "price": 180
                    }
                ]
            }
        },
        "non-prescription": {
            "analgesic": {
                "general": [
                    {
                        "id": 9,
                        "name": "Acetaminophen",
                        "price": 15
                    },
                    {
                        "id": 10,
                        "name": "Ibuprofen",
                        "price": 20
                    }
                ]
            },
            "antihistamine": {
                "antiallergic": [
                    {
                        "id": 11,
                        "name": "Loratadine",
                        "price": 12
                    },
                    {
                        "id": 12,
                        "name": "Desler M",
                        "price": 8
                    },
                    {
                        "id": 13,
                        "name": "Allegra",
                        "price": 21
                    },
                    {
                        "id": 14,
                        "name": "Fexofenadine",
                        "price": 18
                    }
                ]
            }
        }
    }


print ("\n ***     Bienvenido a Saman-Labs      *** \n ")

while True:
    decisión = int(input("Por favor, escoge una opción válida \n 1- Ver inventario \n 2- Registrar compra \n 3- Salir"))
    if decisión == 1:
        print ("Muy bien, has decidido ver el inventario, este será mostrado a continuación \n ")
        decisión2 = int(input("Para continuar, por favor escoge una opción válida para el medicamento deseado \n 1- Con preescripción \n 2- Sin preescripción"))
        if decisión2 == 1:
            for prescription, types in medications.items():
                for antibiotics in prescription.items():
                    for skin in antibiotics.items():
                        print (skin)
