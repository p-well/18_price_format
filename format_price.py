import argparse
import re


def format_price_in_local(price):
    price_template = '\d*[.,]?\d*$'
    price_template_with_quotes = '[\',\"]\d*[.,]?\d*[\',\"]$'
    if any([
            re.fullmatch(price_template, str(price)),
            re.fullmatch(price_template_with_quotes, str(price))
       ]):
        price = re.search(
            r'\d*[.,]?\d{0,3}',
            str(price)
        ).group(0).replace(',','.')
        price = float(price)
        if price.is_integer():
            price_comma_delimeted = '{:,.0f}'.format(price) #no decimal
        else:
            price_comma_delimeted = '{:,.2f}'.format(price) #2 decimals
        return price_comma_delimeted.replace(',',' ')
    else:
        raise ValueError('Wrong price format')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price')
    arguments = parser.parse_args()
    local_price = format_price_in_local(arguments.price)
    print(local_price)
