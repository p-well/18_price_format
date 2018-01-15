# Price Formatter

The purpose of this script is to convert string with goods prise to a more visual local form like 1 240.50 (RU format).

2 interfaces are implemented:

 - Command line interface (CLI) for direct usage in console
 - Software interface for usage as a part of program
 
 Additionally script is covered by unittests checking correct script's work.

Pavel Kadantsev, 2017. <br/>
p.a.kadantsev@gmail.com


# Installation

Python 3.5 should be already installed.
Simply clone this repo on your machnine using <br /> ```git clone https://github.com/p-well/18_price_format.git ```.

No 3rd party dependencies installation needed.


# Usage

To execute the script in CLI run the command ```python format_price.py <price>```.
To use price formatter in other code import it like ```from format_price import format```.


# Example of Scripts Launch

<pre>
<b>>python format_price.py 12345678,547</b>
12 345 678.55
</pre>


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
