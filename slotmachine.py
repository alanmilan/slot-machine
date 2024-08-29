import random

def spin_row():
    symbols = ["🐯", "🍉", "🍍", "⭐", "🔔"]

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row [0] == row[1] == row [2]:
        if row[0] == "🐯":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍍":
            return bet * 5
        elif row[0] == "⭐":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 12
    return 0 



def main():
    balance = 100
    
    print("*********************")
    print("Bem vindo ao Jogo do Tigrinho!")
    print("*********************")
    print("Symbols: 🐯 🍉 🍍 ⭐ 🔔 ")

    while balance > 0:
        print(f"Valor atual: ${balance}")

        bet = input("Coloque o número para apostar: ")
        
        if not bet.isdigit():
            print("Por favor, digite um número válido!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Você não tem créditos suficientes!")
            continue

        if bet <= 0:
            print("Apostas precisam ser maiores que 0!")
            continue

        balance -= bet

        row = spin_row()

        print("Rodando...")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"Você ganhou ${payout}")
        else:
            print("Você perdeu essa rodada!")

        balance += payout

        play_again = input("Você gostaria de girar novamente? (S/N): ").upper()

        if play_again != "S":
            break

        print(f"Game over! Seu saldo é {balance}")

if __name__ == "__main__":
    main()