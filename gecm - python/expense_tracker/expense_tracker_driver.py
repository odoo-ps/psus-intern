usage = '''
Expense Tracker CLI

Usage:
    expense_tracker_driver.py init
    expense_tracker_driver.py view [<view_category>]
    expense_tracker_driver.py <amount> <category> [<message>] [<date>]
'''

from pydoc import doc

from docopt import docopt
from tabulate import tabulate

from expense_tracker import *

args = docopt(usage)

if args['init']:
    init()
    print('User Profile Created')
elif args['view']:
    category = args['<view_category>']
    total, results = view(category)
    print(f'Your expenses were: \n{tabulate(results)}')
    print(f'The total amount spent is ${total}')
elif args['<amount>']:
    #try:
    #    print(args['<amount>'])
        amount = float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'], args['<date>'])
        print('Logged info correctly')
    #except:
    #    print(f'Error in arguments\n${usage}')
