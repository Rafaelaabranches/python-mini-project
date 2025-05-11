def pode_votar(idade):
    return idade >= 16

def main():
    idade = int(input("Digite sua idade: "))
    if pode_votar(idade):
        print("Você pode votar.")
    else:
        print("Você ainda não pode votar.")

if __name__ == "__main__":
    main()
