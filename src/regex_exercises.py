import re

def exercicio_regex_1_1(cpf_str):
  """
  Valida CPF 1.1: Pontuação opcional
  Ex: 772.843.809-34 ou 77284380934
  """
  regex_cpf_1_1 = r"^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$"
  return bool(re.fullmatch(regex_cpf_1_1, cpf_str))

def exercicio_regex_1_2(cpf_str):
  """
  Valida CPF 1.2: Pontuação variada (ponto, espaço, barra, hífen) ou opcional
  Ex: 772 843 809/34
  """
  regex_cpf_1_2 = r"^\d{3}[\.\s]?\d{3}[\.\s]?\d{3}[/\-]?\d{2}$"
  return bool(re.fullmatch(regex_cpf_1_2, cpf_str))

def exercicio_regex_2_1(texto):
  """
  Encontra todas as palavras que terminam com a letra 'o'.
  """
  regex_palavra_o = r"\b\w+o\b"
  # re.IGNORECASE (ou re.I) garante que pegamos 'o' e 'O'
  return re.findall(regex_palavra_o, texto, re.IGNORECASE)

def exercicio_regex_2_2(texto):
  """
  Encontra todas as palavras que começam E terminam com vogais.
  """
  regex_vogais = r"\b[aeiou]\w*[aeiou]\b"
  return re.findall(regex_vogais, texto, re.IGNORECASE)

def exercicio_regex_3_1(hora_str):
  """
  Valida hora no formato HH:MM (de 00:00 até 23:59).
  """
  regex_hora = r"^([01]\d|2[0-3]):[0-5]\d$"
  return bool(re.fullmatch(regex_hora, hora_str))

def exercicio_regex_3_2(octeto_str):
  """
  Valida um octeto de IPv4 (número entre 0 e 255).
  """
  regex_octeto = r"^(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})$"
  return bool(re.fullmatch(regex_octeto, octeto_str))

def exercicio_regex_3_3(ip_str):
  """
  Valida um endereço IPv4 completo (Ex: 192.168.1.1).
  """
  octeto_regex = r"(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})"
  regex_ip = rf"^{octeto_regex}\.{octeto_regex}\.{octeto_regex}\.{octeto_regex}$"
  return bool(re.fullmatch(regex_ip, ip_str))

def exercicio_regex_4(num_str):
  """
  Verifica se a string representa um número (inteiro ou real) válido.
  Ex: 10, +5, -3, -10.3, 0.80
  """
  regex_numero = r"^[+\-]?\d+(\.\d+)?$"
  return bool(re.fullmatch(regex_numero, num_str))

def exercicio_regex_5_e_6(telefone_str):
  """
  Exercícios 5 e 6: Valida e formata número de telefone.
  Se inválido, retorna None.
  Se válido, retorna (XX) XXXX-XXXX (fixo) ou (XX) XXXXX-XXXX (celular).
  """
  telefone_limpo = re.sub(r"[\(\)\s\-]", "", telefone_str)
  
  # Grupo 1 (DDD): (0?\d{2}) -> 019 ou 19
  # Grupo 2 (Prefixo): (9\d{4}) -> 9xxxx
  # Grupo 3 (Sufixo): (\d{4}) -> xxxx
  regex_celular = r"^(0?\d{2})(9\d{4})(\d{4})$"
  
  # (?!9) -> Lookahead negativo (garante que o prefixo não começa com 9)
  regex_fixo = r"^(0?\d{2})((?!9)\d{4})(\d{4})$"

  match_cel = re.match(regex_celular, telefone_limpo)
  match_fixo = re.match(regex_fixo, telefone_limpo)

  if match_cel:
    partes = match_cel.groups()
    ddd = partes[0][-2:] # Pega apenas os 2 dígitos do DDD (ex: '019' vira '19')
    return f"({ddd}) {partes[1]}-{partes[2]}"
  
  elif match_fixo:
    partes = match_fixo.groups()
    ddd = partes[0][-2:]
    return f"({ddd}) {partes[1]}-{partes[2]}"
    
  else:
    return None
  
# --------- Testes ---------
print("--- Exercício 1.1 (CPF com pontuação opcional) ---")
cpfs_1_1 = ["772.843.809-34", "77284380934", "772.843.80934", "123.456.789-AB"]
for cpf in cpfs_1_1:
  print(f"Testando '{cpf}': {exercicio_regex_1_1(cpf)}")

print("\n--- Exercício 1.2 (CPF com pontuação variada) ---")
cpfs_1_2 = ["772.843.809-34", "77284380934", "772 843 809/34", "772.843.809/34", "772 843 809-34"]
for cpf in cpfs_1_2:
  print(f"Testando '{cpf}': {exercicio_regex_1_2(cpf)}")

print("\n--- Exercício 2.1 (Palavras terminadas em 'o') ---")
texto_ex_2_1 = "Escreva uma regex capaz de encontrar no texto deste parágrafo todas as palavras."
print(f"Texto: '{texto_ex_2_1}'")
print(f"Palavras encontradas: {exercicio_regex_2_1(texto_ex_2_1)}")

print("\n--- Exercício 2.2 (Palavras começam/terminam com vogal) ---")
texto_ex_2_2 = "Escreva uma regex capaz de encontrar em um texto todas as palavras."
print(f"Texto: '{texto_ex_2_2}'")
print(f"Palavras encontradas: {exercicio_regex_2_2(texto_ex_2_2)}")

print("\n--- Exercício 3.1 (Validar Hora HH:MM) ---")
horas_3_1 = ["14:30", "23:59", "00:00", "23:99", "14:60", "14 30"]
for h in horas_3_1:
  print(f"Testando '{h}': {exercicio_regex_3_1(h)}")
  
print("\n--- Exercício 3.2 (Validar Octeto IPv4) ---")
octetos_3_2 = ["192", "255", "0", "256", "-1", "1.2"]
for o in octetos_3_2:
  print(f"Testando '{o}': {exercicio_regex_3_2(o)}")

print("\n--- Exercício 3.3 (Validar IP Completo) ---")
ips_3_3 = ["192.168.1.1", "255.0.0.0", "0.0.0.0", "255.256.0.1", "192.168.1"]
for ip in ips_3_3:
  print(f"Testando '{ip}': {exercicio_regex_3_3(ip)}")

print("\n--- Exercício 4 (Validar Número Inteiro/Real) ---")
nums_4 = ["10", "+5", "-3", "-10.3", "0.80", "2.8033", "10.", ".80", "abc", "+10.a"]
for n in nums_4:
  print(f"Testando '{n}': {exercicio_regex_4(n)}")

print("\n--- Exercícios 5 e 6 (Validar e Formatar Telefone) ---")
telefones_teste = [
    "(19) 3123-4567",
    "193123-4567",
    "(019)3123-4567",
    "(19)31234567",
    "1931234567",
    "(019) 91234 5678",
    "(019)912345678",
    "019912345678",
    "19 91234 5678",
    "1991234 5678",
    "12345678",
    "9912345678"
]

for tel in telefones_teste:
  formatado = exercicio_regex_5_e_6(tel)
  if formatado:
    print(f"'{tel}': VÁLIDO. Formato: {formatado}")
  else:
    print(f"'{tel}': INVÁLIDO.")