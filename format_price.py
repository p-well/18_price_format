import argparse
from re import fullmatch


def format_price(price):
    if isinstance(price, (int, float)):
        price = float(price)
    if isinstance(price, str) and fullmatch('\d*[.,]?\d*$', price):
        price = float(price.replace(',','.'))
    if price.is_integer():
        price_no_fractional = int('{:08.0f}'.format(price))
        print(price_no_fractional, len(str(price_no_fractional)))
        #price_no_fractional = int(locale.format('%d', price))
        price_comma_delimeted = '{:,}'.format(price_no_fractional)
        price_whitespace_delimeted = price_comma_delimeted.replace(',',' ')
        return price_whitespace_delimeted
    else:
        return format(price, '.2f')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price')
    args = parser.parse_args()
print(format_price(args.price))

#The ',' option signals the use of a comma for a thousands separator. For a locale aware separator, use the 'n' integer presentation type instead.

#6.1.3.2
#In most of the cases the syntax is similar to the old %-formatting, with the addition of the {} and with : used instead of %. For example, '%03.2f' can be translated to '{:03.2f}'.
