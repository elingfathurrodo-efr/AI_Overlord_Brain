class CapitalManager:

    def __init__(self,capital):

        self.capital = capital
        self.secured_profit = 0

    def update_capital(self,new_capital):

        if new_capital >= self.capital * 2:

            secure = new_capital / 2

            self.secured_profit += secure

            self.capital = new_capital - secure

            print("Profit secured:",secure)

        else:

            self.capital = new_capital

    def get_status(self):

        return {

            "capital":self.capital,
            "secured_profit":self.secured_profit

        }
