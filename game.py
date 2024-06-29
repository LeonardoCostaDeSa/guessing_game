import random
list_numbers_tried = []
number_max = int(input("number max: "))
number_min = int(input("number min: "))
def is_correct (number_tried):
    user_response = int(input("Am I right? 1 - Yes; 2 - No \n"))
    if user_response == 1:
        print("Great! Thanks for the game!")
        return True
    else:
        list_numbers_tried.append(number_tried)
        print("So, let's try again!")
        return False
def greater_or_lower(number_tried):
    greater_or_lower = int(input("is the number you are thinking about (1)greater or (2)lower than the number I tried?\n"))
    if greater_or_lower == 1:
        return 'greater'
    else:
        return 'lower'
while True:
    number_tried = random.randint(number_min,number_max)
    print(f' The number are you thinking is {number_tried}?')
    if is_correct(number_tried):
        break
    direction = greater_or_lower(number_tried)
    if direction == 'greater':
        number_min = number_tried + 1
    elif direction == 'lower':
        number_max = number_tried - 1
    print(f"Updated range: {number_min} to {number_max}")    
print(f"It took {len(list_numbers_tried) + 1} guesses.")
