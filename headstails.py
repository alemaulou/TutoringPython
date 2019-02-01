## Name: Headstails
## Date: 1/31/2019
## Author: Alessandro Lou

import random

def main():
    for i in range(10):
        flip()


def flip():
    coin = random.randrange(2)
    if(coin == 1):
        print("Tails")
    else:
        print("Heads")
        
main()
