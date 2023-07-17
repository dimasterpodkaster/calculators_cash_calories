import datetime as dt

class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        date_time_obj = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.date = date_time_obj

    def __str__(self):
        return "Запись"

class Calculator:
    def __init__(self, limit):
        self.remain = limit
        self.records = []

    def __str__(self):
        return "Калькулятор"

    def add_record(self, rec):
        self.records.append(rec)

    def get_today_stats(self):
        sum_of_stats = 0
        now = dt.datetime.now()
        date_rn = now.date()
        for element in self.records:
            if element.date == date_rn:
                sum_of_stats += element.amount
        return sum_of_stats

    def get_week_stats(self):
        sum_of_stats = 0
        now = dt.datetime.now()
        date_rn = now.date()
        date_st = date_rn - dt.timedelta(weeks=1)
        for element in self.records:
            if date_st < element.date <= date_rn:
                sum_of_stats += element.amount
        return sum_of_stats

class CashCalculator(Calculator):
    # Курс, актуальный на 17.07.2023
    usd_val = 90.24
    eur_val = 101.56
    rub_val = 1
    def get_today_cash_remained(self, currency):
        currencies = {
            'eur': ('Euro', self.eur_val),
            'usd': ('USD', self.usd_val),
            'rub': ('Rub', self.rub_val)
        }
        currency_name = currencies[currency][0]
        currency_val = currencies[currency][1]
        val_of_remained_cash = self.remain - self.get_today_stats()
        val_of_remained_cash_in_cur = val_of_remained_cash / currency_val
        if val_of_remained_cash > 0:
                return f"На сегодня осталось {val_of_remained_cash_in_cur} {currency_name}"
        elif val_of_remained_cash == 0:
            return f"Денег нет, держись"
        else:
            return f"Денег нет, держись: твой долг - {abs(val_of_remained_cash)} {currency_name}"

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        val_of_remained_cal = self.remain - self.get_today_stats()
        if val_of_remained_cal > 0:
                return f"Сегодня можно съесть что-нибудь еще, но с общей калорийностью не более {val_of_remained_cal} кКал"
        else:
            return f"Хватит есть!"

r1 = Record(145, "Безудержный шопинг", "08.03.2019")
r2 = Record(1568, "Наполнение потребительской корзины", "09.03.2019")
r3 = Record(691, "Катание на такси", "08.03.2019")
r7 = Record(551, "Поездка в отпуск", "17.07.2023")
r8 = Record(458, "Хорошо погулял", "15.07.2023")
r9 = Record(1140, "Баночка чипсов", "17.07.2023")

r4 = Record(1186, "Кусок тортика. И еще один.", "24.02.2019")
r5 = Record(84, "Йогурт", "23.02.2019")
r6 = Record(1140, "Баночка чипсов", "24.02.2019")
r10 = Record(1140, "Баночка чипсов", "17.07.2023")
r11 = Record(84, "Йогурт", "14.07.2023")

calc_cash = CashCalculator(1000)
calc_cal = CaloriesCalculator(2000)
calc_cash.add_record(r1)
calc_cash.add_record(r2)
calc_cash.add_record(r3)
calc_cash.add_record(r7)
calc_cash.add_record(r8)
calc_cash.add_record(r9)
print(calc_cash.get_today_stats())
print(calc_cash.get_week_stats())
print(calc_cash.get_today_cash_remained("rub"))

print("--")


calc_cal.add_record(r4)
calc_cal.add_record(r5)
calc_cal.add_record(r6)
calc_cal.add_record(r10)
calc_cal.add_record(r11)
print(calc_cal.get_today_stats())
print(calc_cal.get_week_stats())
print(calc_cal.get_calories_remained())