from tabulate import tabulate

class Membership_User:
    data = {
        'Sumbul' : 'Platinum',
        'Ana' : 'Gold',
        'Cahya' : 'Platinum'
        }
    
    def __init__(self, username):
        self.username = username

    def show_benefit(self):
        table = [
            ['Platinum', '15%', 'Benefit Silver + Gold + Voucher + Cashback 30%'],
            ['Gold', '10%', 'Benefit Silver + Voucher Ojek Online'],
            ['Silveer', '8%', 'Voucher Makanan']
            ]
        header = ['Membership', 'Discount', 'Another Benefit']

        print(tabulate(table, header, tablefmt = 'github', stralign = 'center'))

    def show_requirements(self):
        table = [
            ['Platinum', 8, 15],
            ['Gold', 6, 10],
            ['Silver', 5, 7]
            ]
        header = ['Membership', 'Monthly Expenses (juta)', 'Monthly Income (juta)']

        print(tabulate(table, header, tablefmt = 'github', numalign = 'center'))

    def predict_membership(self, monthly_expenses, monthly_income):
        requirement = [[8, 15], [6, 10], [5, 7]]
        counter = 0
        list_dist = []

        while counter < len(requirement):
            calc_1 = (monthly_expenses - requirement[counter][0]) ** 2
            calc_2 = (monthly_income - requirement[counter][1]) ** 2
            dist = round(((calc_1 + calc_2) ** 0.5), 2)
            list_dist.append(dist)
            counter += 1

        dict_dist = {
            'Platinum' : list_dist[0],
            'Gold' : list_dist[1],
            'Silver' : list_dist[2]
            }
        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {dict_dist}")

        for member, distance in dict_dist.items():
            if distance == min(list_dist):
                self.data[self.username] = member
                return member
            
    def show_membership(self, username):
        for key, value in self.data.items():
            if key == username:
                return value
            
    def calculate_price(self, membership, list_price):
        for self.username, tier in self.data.items():
            if self.username == membership:
                if tier == 'Platinum':
                    sum_price = sum(list_price)
                    total_price = sum_price - (sum_price * 0.15)
                    return total_price
                elif tier == 'Gold':
                    sum_price = sum(list_price)
                    total_price = sum_price - (sum_price * 0.1)
                    return total_price
                elif tier == 'Silver':
                    sum_price = sum(list_price)
                    total_price = sum_price - (sum_price * 0.08)
                    return total_price
                else:
                    print("Tier doesn't exist")
            else:
                raise Exception("Membership doesn't exist")