entrada = input("Digite as suas notas: ")
notas = [float(n) for n in entrada.split()]

print("Soma de todas as notas:", sum(notas))

print(f"Sua média de todas as notas:{ sum(notas) / len(notas):.2f}")

if sum(notas) / len(notas) >= 6: 

   print("aprovado")
else:
   print("reprovado")