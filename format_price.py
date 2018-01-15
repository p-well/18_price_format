import argparse
import re


def format_price(price):
    price_template = '\d*[.,]?\d*$'
    price_template_with_quotes = '[\',\"]\d*[.,]?\d*[\',\"]$'
    if any([
            re.fullmatch(price_template, price),
            re.fullmatch(price_template_with_quotes, price)
       ]):
        price = re.search(r'\d*[.,]?\d{3}', price).group(0).replace(',','.')
        price = float(price)
        print(price)
        if price.is_integer():
            print('price is integer')
            price_comma_delimeted = '{:,.0f}'.format(price) #no decimal
        else:
            print('price is not integer')
            price_comma_delimeted = '{:,.2f}'.format(price) #2 decimals
        price_whitespace_delimeted = price_comma_delimeted.replace(',',' ')
        print(price_whitespace_delimeted)
    else:
        raise ValueError('Wrong price format')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price')
    arguments = parser.parse_args()
    local_price = format_price(arguments.price)
