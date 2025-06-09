transactions = []

def add_transaction(amount):
    print("Transaction added.")
def balance():
    return sum(t["amount"] for t in transactions)

def show_history():
    if not transactions:
        print("No transactions yet.")
        return
    for i, t in enumerate(transactions, 1):
        t_type = "Income" if t["amount"] > 0 else "Expense"
        print(f"{i}. {t_type} | {t['desc']} | {t['category']} | ${abs(t['amount']):.2f}")

def main():
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. Show Balance\n4. Show History\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            amt = float(input("Income amount: "))
            add_transaction(amt)
        elif choice == "2":
            amt = float(input("Expense amount: "))
            add_transaction(-amt)
        elif choice == "3":
            print(f"Balance: ${balance():.2f}")
        elif choice == "4":
            show_history()
        elif choice == "5":
            print("Good bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()