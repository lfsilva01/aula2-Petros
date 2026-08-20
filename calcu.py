def calculadora():
	print("Calculadora")
	print("Digite 'sair' para encerrar.")

	while True:
		operacao = input("\nEscolha uma operação (+, -, *, /): ").strip().lower()

		if operacao == "sair":
			print("Calculadora encerrada.")
			break

		if operacao not in ("+", "-", "*", "/"):
			print("Operação inválida.")
			continue

		try:
			primeiro = float(input("Digite o primeiro número: "))
			segundo = float(input("Digite o segundo número: "))

		  if operacao == "+":
				resultado = primeiro + segundo
		  elif operacao == "-":
				resultado = primeiro - segundo
		  elif operacao == "*":
				resultado = primeiro * segundo
		  else:
				if segundo == 0:
					print("Não é possível dividir por zero.")
					continue
				resultado = primeiro / segundo

			print(f"Resultado: {resultado:g}")
		except ValueError:
			print("Digite números válidos.")


if __name__ == "__main__":
	calculadora()
