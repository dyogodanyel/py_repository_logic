#Faça um Programa que pergunte quanto você ganha por hora e o 
# número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas_trabalhadas = 0
ganhos_hora = 0

horas_trabalhadas = int(input("Digite quantas hora você trabalha: "))
ganhos_hora = float(input("Digite quanto você ganha por hora: "))

#travei um pouco aqui, nao pensei na solucao

salario_total = (horas_trabalhadas*ganhos_hora)*21

#ta certo? porem se ele trabalha de sabado como faz? e se o mês ter mais dias?

print(f"Trabalhando de segunda a sexta seu salário é R${salario_total}")