guess_number = 10
enter_number = int(input("Enter ur number: "))

if enter_number <= 0:
    print("The number must be positive and not equal 0")
elif enter_number == guess_number:
    print("My congrats, u guessed it!")
else:
    print("Unlucky, next time will be better")
