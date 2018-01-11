import argparse
import locale
from re import fullmatch


def format_price(price):
    locale.setlocale(locale.LC_ALL, ('RU'))
    if isinstance(price, (int, float)):
        price = float(price)
    if isinstance(price, str) and fullmatch('\d*[.,]?\d*$', price):
        price = float(price.replace(',','.'))
    if price.is_integer():
        price_no_fractional = int(format(price, '.0f'))
        #price_no_fractional = int(locale.format('%d', price))
        price_comma_delimeter = '{0:,}'.format(price_no_fractional)
        price_whitespace_delimeter = price_comma_delimeter.replace(',',' ')
        return price_whitespace_delimeter
    else:
        return format(price, '.2f')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price')
    args = parser.parse_args()
    print(format_price(args.price))