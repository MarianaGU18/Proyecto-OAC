def suma_negativos(U):
    SN = 0
    N  = 0x01
    
    for valor in U:
        if valor & 0x80 == 0:
            N = 0xFF
        else:
            SN += valor - 0x100
    
    return SN & 0xFFFF, N


# EJEMPLO
#U = [0xFF, 0xFF]
#U =  [0xFF, 0x05, 0xFC]
#U = [0xFE]
U = [0x02, 0x7F, 0xFE, 0xF8]
#U = [0xF0, 0xF0, 0xF0]
#U =  [0x01, 0x20, 0x7C]


def imprimir_resultados():

    print("\n=========== EJEMPLOS AUTOMÁTICOS ===========\n")
        
    dec = [(x-256 if x>127 else x) for x in U]
    SN, N = suma_negativos(U)

    print("Lista en HEX:      ", [hex(x) for x in U])
    print("Lista en Decimal:  ", dec)
    print("Suma en decimal:   ", SN if SN < 0x8000 else SN-0x10000)
    print("Suma en HEX:       ", hex(SN))
    print("Todos Negativos? (01=SI | FF=NO): ", hex(N))
    print("")


if __name__ == "__main__":
    imprimir_resultados()
