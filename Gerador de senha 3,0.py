import random

def generate_password(length, special_characters):
  if special_characters:
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+'
  else:
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

  password = ''
  for i in range(length):
    password += random.choice(characters)
  return password

if __name__ == '__main__':
  length = int(input("Digite o número de caracteres da senha: "))
  special_characters = input("Deseja incluir caracteres especiais? (s/n): ") == 's'
  password = generate_password(length, special_characters)
  print(f"Sua senha gerada é: {password}")