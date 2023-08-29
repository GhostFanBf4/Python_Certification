from decimal import Decimal
class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        # Preparing strings
        title = self.category.center(30,'*') + '\n'
        total = 'Total: ' + str("%.2f" %(self.get_balance()))
        description = amount = ''

        # Reading dictionaries in the ledger for values of both keys, and formating 
        for dict in self.ledger:
            description +=  '{:23.23}'.format(str(dict.get('description')).ljust(23)) + '{:7.7}'.format(str("%.2f" % (dict.get('amount'))).rjust(7)) + '\n'
            
        return title + description + total
    
    def deposit(self,amount,description=''):
        self.ledger.append({"amount":amount,"description":description})
    
    def get_balance(self):
        balance = 0
        # Reading dictionaries in the ledger for value of key "amount"
        for dict in self.ledger:
            balance += dict.get('amount')

        # Decimal for accurate numbers
        return Decimal(balance)
    
    def check_funds(self,amount):
            if amount > self.get_balance():
                return False
            else:
                return True

    def withdraw(self,amount,description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount":-amount,"description":description})
            return True
        else:
            return False
    
    def transfer(self,amount,category):#
        if self.check_funds(amount) == True:
            self.withdraw(amount,'Transfer to {}'.format(category.category))
            category.deposit(amount,'Transfer from {}'.format(self.category))
            return True
        else:
            return False
    


def create_spend_chart(categories):
    spend_by_category = {}
    total_spend = 0
    for category in categories:
        spend = 0
        # Reading dictionaries in the ledger for negative value of key "amount"
        for dict in category.ledger:
            if dict.get('amount') < 0:
                # Getting positive number form negative numbers (withdraws)
                total_spend -= dict.get('amount')
                spend -= dict.get('amount')
                spend_by_category.update({category.category : spend})
        
    # Calculating percentage
    percentage_per_category = []
    for money in spend_by_category.values():
        percentage = money / total_spend * 100
        # Rounding to nearest 10
        
        percentage_per_category.append(round(percentage / 10)*10)
    
    # Creating string
    the_string = ''
    # Top title
    title = "Percentage spent by category \n"
    # o and percents
    print_o = 0
    for num in range(100,-1,-10):
        the_string += (str(num) +'| ').rjust(5)
        if num in percentage_per_category:
            print_o += 1
        the_string += ('o  ' * print_o + '\n')
    # bottom line
    bottom_line = ('-' * int(len(percentage_per_category) * print_o + 1)).rjust(5 + int(len(percentage_per_category) * print_o)) + '\n'
    # categories
    sorted_by_category = sorted(spend_by_category, key=spend_by_category.get, reverse=True)
    categories = '     '
    max_letters = index = 0
    while index <= max_letters:
        for word in sorted_by_category:
            if len(word) > max_letters:
                max_letters = len(word)
            try:
                categories += (word[index] + '  ')
            except:
                categories += '   '
        categories += '\n' + '     '
        index += 1

    Final = (title + the_string + bottom_line + categories).strip()
    return Final
