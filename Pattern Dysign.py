from abc import ABC, abstractmethod



class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass



class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print("\n--- Credit Card Payment ---")
        print(f"Payment Type : Credit Card")
        print(f"Amount       : ₹{amount:.2f}")
        print("Transaction  : Credit card payment processed successfully.")



class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print("\n--- PayPal Payment ---")
        print(f"Payment Type : PayPal")
        print(f"Amount       : ₹{amount:.2f}")
        print("Transaction  : PayPal payment processed successfully.")


class BitcoinPayment(PaymentStrategy):

    def pay(self, amount):
        print("\n--- Bitcoin Payment ---")
        print(f"Payment Type : Bitcoin")
        print(f"Amount       : ₹{amount:.2f}")
        print("Transaction  : Bitcoin payment processed successfully.")



class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
        print(f"\nPayment strategy changed to: {strategy.__class__.__name__}")

    def process_payment(self, amount):
        self.strategy.pay(amount)



def main():

    print("======================================")
    print("   CONFIGURABLE PAYMENT PROCESSOR")
    print("       Strategy Design Pattern")
    print("======================================")

    amount = float(input("\nEnter payment amount: ₹"))

   
    processor = PaymentProcessor(CreditCardPayment())

    while True:
        print("\n========== PAYMENT MENU ==========")
        print("1. Credit Card")
        print("2. PayPal")
        print("3. Bitcoin")
        print("4. Process Payment")
        print("5. Exit")
        print("==================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            processor.set_strategy(CreditCardPayment())

        elif choice == "2":
            processor.set_strategy(PayPalPayment())

        elif choice == "3":
            processor.set_strategy(BitcoinPayment())

        elif choice == "4":
            processor.process_payment(amount)

        elif choice == "5":
            print("\nThank you for using the Payment Processor.")
            break

        else:
            print("\nInvalid choice! Please try again.")



if __name__ == "__main__":
    main()
