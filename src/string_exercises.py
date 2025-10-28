import sys

def exercicio_1(frase, antiga, nova):
  """
  Substitui a última ocorrência de 'antiga' por 'nova' em 'frase'.
  """
  partes = frase.rsplit(antiga, 1)
  if len(partes) == 2:
    return nova.join(partes)
  else:
    return frase

def exercicio_2(cadeia):
  """
  Gera a cadeia de DNA complementar (A->T, T->A, C->G, G->C).
  """
  mapa = str.maketrans("ATCG", "TAGC")
  return cadeia.upper().translate(mapa)

def exercicio_3(frase):
  """
  Retorna o número de palavras em uma frase, lidando com espaços extras.
  """
  palavras = frase.split()
  return len(palavras)

def exercicio_4_ler_frase():
  """
  Realiza a entrada de dados (leitura da frase) para o ex 4.
  """
  frase = input("Digite uma frase para o Ex 4: ")
  return frase

def exercicio_4_substituir(frase):
  """
  Substitui todas as ocorrências de espaço por '#'.
  """
  return frase.replace(" ", "#")

def exercicio_5(s1, s2):
  """
  Verifica se uma string é o inverso da outra (palíndromos mútuos).
  """
  return s1 == s2[::-1]

def exercicio_8(data_str):
  """
  Converte uma data dd/mm/aaaa para o formato por extenso.
  """
  meses = [
      "janeiro", "fevereiro", "março", "abril", "maio", "junho",
      "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
  ]
  
  try:
    dia, mes_num_str, ano = data_str.split('/')
    mes_num = int(mes_num_str)
    
    if not (1 <= mes_num <= 12) or len(dia) != 2 or len(ano) != 4:
        raise ValueError("Formato inválido")

    nome_mes = meses[mes_num - 1]
    return f"Você nasceu em {dia} de {nome_mes} de {ano}"
  except (ValueError, IndexError):
    return "Formato de data inválido. Use dd/mm/aaaa."
  
# --------- Testes ---------
print("--- Exercício 1 ---")
frase_ex1 = "Quem parte e reparte fica com a maior parte"
resultado_ex1 = exercicio_1(frase_ex1, "parte", "parcela")
print(f"Original: {frase_ex1}")
print(f"Resultado: {resultado_ex1}")

print("\n--- Exercício 2 ---")
dna_entrada = "AATCTGCAC"
print(f"Entrada: {dna_entrada}")
print(f"Saída: {exercicio_2(dna_entrada)}")

print("\n--- Exercício 3 ---")
frase_ex3 = "   Uma   frase   com    vários espaços  "
print(f"A frase '{frase_ex3}' contém {exercicio_3(frase_ex3)} palavras.")

print("\n--- Exercício 4 ---")
frase_ex4 = exercicio_4_ler_frase()
resultado_ex4 = exercicio_4_substituir(frase_ex4)
print(f"Resultado: {resultado_ex4}")

print("\n--- Exercício 5 ---")
str1 = input("Digite a primeira string (ex: amor): ")
str2 = input("Digite a segunda string (ex: roma): ")
if exercicio_5(str1, str2):
  print("São palíndromos mútuos!")
else:
  print("Não são palíndromos mútuos.")

print("\n--- Exercício 6 ---")
nome_ex6 = input("Digite seu nome (ex: Vanessa): ")
resultado_ex6 = nome_ex6.upper()[::-1]
print(f"Resultado: {resultado_ex6}")

print("\n--- Exercício 7 ---")
nome_ex7 = input("Digite seu nome (ex: Vanessa): ")
nome_maiusculo_ex7 = nome_ex7.upper()
for i in range(1, len(nome_maiusculo_ex7) + 1):
  print(nome_maiusculo_ex7[:i])

print("\n--- Exercício 8 ---")
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
print(exercicio_8(data_nascimento))