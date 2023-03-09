import argparse
import sys
import os
import datetime
from datetime import timedelta

def generateInRange(args):
    from_date=args.from_date
    from_date=datetime.datetime.strptime(from_date,"%d/%m/%Y").date()
    to_date=args.to_date
    to_date=datetime.datetime.strptime(to_date,"%d/%m/%Y").date()
    curr=from_date
    print(type(curr))
    while(curr<=to_date):
        print(curr)
        curr=curr+timedelta(days=1)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--from_date',type=str,help="Enter from date")
    parser.add_argument('--to_date',type=str,help="Enter to date")
    args=parser.parse_args()
    sys.stdout.write(str(generateInRange(args)))