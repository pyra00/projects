class BankAccount:
    def __init__(self):
        self.customer = BankAccount()
    def display_account(self):
        self.customer.show_name()
        print('Balance; $500')