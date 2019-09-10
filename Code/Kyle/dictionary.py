


fruits = ["apple", "banana", "pear"]
prices = [1.2, 3.3, 2.1]

def combine_list(fruits, prices):
    return dict(zip(fruits, prices))

fruit_and_prices = combine_list(fruits, prices)


def calc_average_price(a_dict):
    # avg_price = 0
    prices = list(a_dict.values())
    # for price in prices:
    #     total += prices
    return round(sum(prices) / len(prices), 2)
