import math

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

def get_number_of_bills(budget, denomination):
    return budget // denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    return math.floor(budget / (exchange_rate + (exchange_rate * (spread / 100))) / denomination) * denomination

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    return math.floor(budget / (exchange_rate + (exchange_rate * (spread / 100)))) - exchangeable_value(budget, exchange_rate, spread, denomination)
    

print(exchangeable_value(1500, 0.84, 25, 40))