import argparse
import sys
import os
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
def generate(args):
    current_date=datetime.date.today()
    temp_date=datetime.date.today() 
    while(current_date<temp_date+relativedelta(years=int(args.years))):
        print(current_date)
        current_date=current_date+timedelta(days=1)
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--years',type=str,default="4",help="Enter no of years")
    
    args=parser.parse_args()
    sys.stdout.write(str(generate(args)))