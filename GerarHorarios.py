for hora in range (24):
    for minuto in range(0,60,15):
        if len(str(minuto)) == 1:
            minuto = "00"
        print(str(hora) + ":" + str(minuto))