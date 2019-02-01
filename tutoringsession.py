## Name: Round to 5 Tutoring
## Date: 1/31/2019
## Author: Alessandro Lou

## Calculate multiple of 5 in the range 1 and 100
## The nearestmultiple of 5 is x
## The number you entered is a multiple of 5
## You did not pick a number from 1 and 100 go back again

def main():
    
    number = int(input('Enter number between 1 and 100: '))

    ## explaining to student what a function is
    transformNumber(number)
    
def transformNumber(dog):
    if(dog < 1 or dog > 100):
        print("You have to go back and do this again")
    elif(dog % 5 == 0):
        print("This number is: ", dog, " the number you entered is already a multiple of 5.")
    else:
         print("The closest multiple of 5 for your number is", round(dog/5)*5)

         
main()
