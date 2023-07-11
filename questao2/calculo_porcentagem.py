import csv

with open('data.csv', 'r') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    dados = list(leitor_csv)

# Pessoa com alto colesterol
pessoas_col = list(filter(lambda x: float(x['chol']) > 240, dados))

# Pessoa sem alto colesterol
pessoas_sem_col = list(filter(lambda x: float(x['chol']) < 240, dados))

# Pessoa com alto colesterol e idade acima de 40
pessoas_age_col = list(filter(lambda x: float(x['age']) > 40, pessoas_col))
percent = len(pessoas_age_col) / len(dados) * 100

print(f'A porcentagem de pessoas acima de 40 que está com colesterol alto é: {percent:.2f}%')

# Pessoa com alto colesterol, alto teor de açucar e idade acima de 40
pessoas_acucar_age_col = list(filter(lambda x: float(x['fbs']) == 1, pessoas_age_col))
percent = len(pessoas_acucar_age_col) / len(dados) * 100

print(f'A porcentagem de pessoas acima de 40 que está '
      f'com colesterol alto e alto teor de açucar no sangue é : {percent:.2f}%')

# Pessoa com alto colesterol e alto teor de açucar
pessoas_acucar_col = list(filter(lambda x: float(x['fbs']) == 1, pessoas_col))

# Pessoa sem alto colesterol e sem alto teor de açucar
pessoas_sem_acucar_col = list(filter(lambda x: float(x['fbs']) == 0, pessoas_sem_col))

# Pessoa com alto colesterol, alto teor de açucar e hipertrofia ventricular esquerda
pessoas_acucar_col_hip = list(filter(lambda x: float(x['restecg']) == 2, pessoas_acucar_col))

# Pessoa sem alto colesterol, sem alto teor de açucar e com hipertrofia ventricular esquerda
pessoas_sem_acucar_col_hip = list(filter(lambda x: float(x['restecg']) == 2, pessoas_sem_acucar_col))


p = len(pessoas_acucar_col_hip) / len(pessoas_acucar_col) * 100
psem = len(pessoas_sem_acucar_col_hip) / len(pessoas_sem_acucar_col) * 100

print(f'O numero de pessoas com alto colesterol e açucar é de {len(pessoas_acucar_col)} '
      f'e que também possuem hipertrofia ventricular é de {len(pessoas_acucar_col_hip)} '
      f'isso da em torno de {p:.2f}%')

print(f'Enquanto que as pessoas que não possuem nenhuma dessas 2 '
      f'características totalizam {len(pessoas_sem_acucar_col)} sendo as que possuem '
      f'hipertrofia {len(pessoas_sem_acucar_col_hip)} dando em torno de {psem:.2f}')

print(f'Logo foi concluído que o alto colesterol somado ao alto teor de açucar no sangue '
      f'auxilia sim no surgimento de hipertrofia ventricular esquerda!')


