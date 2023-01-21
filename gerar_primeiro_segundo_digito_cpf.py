import re
import sys


#PRIMEIRO DIGITO
#cpf_enviado_usuario = "49891681866".replace(".","") #replace troca o que esta em primeiro ali e substitui pelo segundo ali
entrada = input("CPF: ")
cpf_enviado_usuario = re.sub(
    r"[^0-9]",
    "",
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada) # o 0 ali é porque é o primeiro caractere

if entrada_e_sequencial:
    print("Voce enviou dados sequenciais")
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1 # coloquei o int ali, pois o cpf era uma string, ai nao ia ter multiplicaçao
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10 % 11)

digito_1 = digito_1 if digito_1 <=9 else 0
#print(digito_1)


#SEGUNDO DIGITO

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito_dez in dez_digitos:
    resultado_digito_2 += int(digito_dez) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10 % 11)

digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado_pelo_calculo = f"{nove_digitos}{digito_1}{digito_2}"

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f"{cpf_enviado_usuario} é valido")
else:
    print("Cpf invalido")
