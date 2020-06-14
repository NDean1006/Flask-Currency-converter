from forex_python.converter import CurrencyRates, CurrencyCodes 
from flask import flash

class Convert():

    def __init__(self):
        self.c = CurrencyRates()
        self.code = CurrencyCodes()
        self.currency_list = self.c.get_rates('USD')

    def exchange(self, ch_from, ch_to, amount):
        """ converts the currency amount by the user specifed chang from currency to the specifes change to currency """
        return "{:.2f}".format(self.c.convert(ch_from, ch_to, int(amount))) 

    def all_true(self, ch_from, ch_to, amount):
        """ validates all index.html /convert from user inputs """
        ch_from = self.check_valid_currency(ch_from)
        ch_to = self.check_valid_currency(ch_to)
        amount = self.check_valid_amount(amount)

        if  ch_from and ch_to and amount:
            return True

    def get_currency_code(self, ch_to):
        """ gets the currency symbol based on the user specifed ch_to input   """
        code = self.code.get_symbol(ch_to)
        return code 

    def check_valid_currency(self, curr):
        """ checks if user entered currency type is in the correct format"""
        if curr in self.currency_list:
            return True
        else:  flash(f"{curr}: is not a valid currency format")

    def check_amount_data_type(self, amount):
        try: 
            if isinstance(int(amount), int):
                return True
        except ValueError:
            flash(f"{amount}: is not a valid numerical value")
    
    def check_valid_amount(self, amount): 
        if self.check_amount_data_type(amount):
            if int(amount) > 0: 
                return True
            else: flash(f"{amount}: is not a possative numerical value")
         
           


       

            





