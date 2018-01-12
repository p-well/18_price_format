import argparse
from re import fullmatch


def format_price(price):
    if isinstance(price, int) or isinstance(price, float):
        price = float(price)
    elif isinstance(price, str) and fullmatch('\d*[.,]?\d*$', price):
        price = float(price.replace(',','.'))
        if price.is_integer():
            price_no_decimal = int('{:.0f}'.format(price))
            price_comma_delimeted = '{:,}'.format(price_no_decimal)
        else:
            price_2_decimals = float('{:.2f}'.format(price))
            price_comma_delimeted = '{:,}'.format(price_2_decimals)
        price_whitespace_delimeted = price_comma_delimeted.replace(',',' ')
        return price_whitespace_delimeted
    else:
        raise ValueError("Wrong input")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price')
    args = parser.parse_args()
    print(format_price(args.price))
