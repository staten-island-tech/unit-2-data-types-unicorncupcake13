#write_a_sentence = input ("write a sentence")
#if write_a_sentence == "I like the color purple":
    #print("correct")
    #print("5 words")
#elif write_a_sentence == "my name is Misha":
    #print("correct")
    #print("4 words")
#else:
    #print("incorrect") 
    #print("1 word")

from numbers import Number


def even_odd():
    even_odd = int(input ("input a number: "))
    if even_odd % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd()

def bill():
    bill = int(input ("How much did you pay for the meal?: "))
    rating = int(input ("service: 0-bad, 1-okay, 2-good, or 3-great: "))
    if rating == 0: 
        print(bill)
    elif rating == 1:
        total = bill + (bill*.15)
        print(total)
    elif rating == 2: 
        total = bill + (bill*.2)
        print(total)
    elif rating == 3:
        total = bill + (bill*.25)
        print(total)

bill()


def test():
    num = int(input ("input a number you want to factor: "))
    factors = set()
    for i in range(1, num + 1):
        if num % i == 0:
            factors.add(i)
    print(factors)
test()

    
