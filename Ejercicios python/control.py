pin = int(input())
verificador = int(input())
segundo_digito = pin%10
pin=pin//10
primer_digito = pin%10
suma=0
suma=suma+primer_digito*verificador
verificador=verificador+1
suma=suma+segundo_digito*verificador
print(suma)
