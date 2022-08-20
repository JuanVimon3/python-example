
def cambiar_divisAs(pesos_colombianos, eleccion)


    if eleccion== "US":
        dolares= round((pesos_colombianos/4200.89),2)
        print(str(dolares) + " " + eleccion)
    elif eleccion == "YEN":
        yenes= round((pesos_colombianos/4000.87),2)
        print(str(yenes)  + " " + eleccion)
    elif eleccion == "CHP":
        chilenos= round((pesos_colombianos/430.67),2)
        print(str(chilenos)  + " " + eleccion)
    else:
        print("SELECCION INVÁLIDA...")

cambiar_divisAs(2000000, "US")
