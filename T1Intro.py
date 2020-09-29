import sys


def hexToBin(Str):
    hexScale = 16
    num_of_bits = 4 * len(Str)
    return bin(int(Str, hexScale))[2:].zfill(num_of_bits)


def binToHex(Str):
    decimal_representation = int(Str, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string[2:]


def codificador_nrzi(hex):
    dadoBinario = hexToBin(hex)
    resultado = ""
    referencia = "-"
    for elem in range(0, len(dadoBinario)):
        if dadoBinario[elem] == "0":
            resultado = resultado + referencia
        if dadoBinario[elem] == "1":
            if referencia == "-":
                referencia = "+"
                resultado = resultado + referencia
            else:
                referencia = "-"
                resultado = resultado + referencia
    return resultado


def decodificador_nrzi(sinal):
    sinalBinario = ""
    for elem in range(0, len(sinal)):
        if sinal[elem] == "-":
            sinalBinario = sinalBinario + "0"
        else:
            sinalBinario = sinalBinario + "1"
    lastSignal = "0"
    sinalDecodificado = ""
    for elem in range(0, len(sinalBinario)):
        if sinalBinario[elem] == lastSignal:
            sinalDecodificado = sinalDecodificado + "0"
        else:
            if lastSignal == "0":
                sinalDecodificado = sinalDecodificado + "1"
                lastSignal = "1"
            elif lastSignal == "1":
                sinalDecodificado = sinalDecodificado + "1"
                lastSignal = "0"
    return binToHex(sinalDecodificado)

def codificador_HDB3(hex):
    dadoBinario = hexToBin(hex)
    print(dadoBinario)
    resultado = ""
    alternador = 1
    contadorDeZeros = 0
    for elem in range(0, len(dadoBinario)):
        if dadoBinario[elem] == "0" and contadorDeZeros < 4:
            contadorDeZeros = contadorDeZeros + 1
        elif dadoBinario[elem] == "0" and contadorDeZeros >= 4:
            contadorDeZeros = 0
            resultado = resultado + "B00V"
        elif dadoBinario[elem] == "1":
            resultado = resultado + ("0" * contadorDeZeros)
            contadorDeZeros = 0
            if alternador:
                resultado = resultado + "+"
                alternador = 0
            else:
                resultado = resultado + "-"
                alternador = 1
    if contadorDeZeros > 0:
        resultado = resultado + ("0" * contadorDeZeros)
    return resultado




#print(codificador_nrzi("1234"))
#print(decodificador_nrzi("---+++----+--+++"))
print("Teste:\n")
print(codificador_HDB3("60016263"))
print("\n")
print("0+-+00+-0+-000+00-+000-+")
