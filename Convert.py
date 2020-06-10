from forex_python.converter import CurrencyRates, CurrencyCodes 

class converter():

    def __init__(self):
        self.c = CurrencyRates()
        self.code = CurrencyCodes()
        self.currency_list = c.get_rates('USD')

    def convert(self, ch_from,ch_to, amount):
        """ converts the currency amount by the user specifed chang from currency to the specifes change to currency """
        conversion = self.c.convert(ch_from, ch_to, amount)
        return conversion

    def get_currencyCode(self, ch_to):
        """ gets the currency symbol based on the user specifed ch_to input   """
        code = self.code.get_symbol
        return code 

    def check_valid_currency(self, curr):
        """ checks if user entered currency type is in the correct format"""
        if curr in self.currency_list:
            return True

    def check_amount_data_type(self, amount):
        if isinstance(amount, int) or isinstance(amount, float):
            return True 
    
    def check_valid_amount(self, amount): 
        if amount > 0: 
            return True


            





