#using switch ….case   display whether accepted character is vowel or not
k = input("Enter vowel in uppercase")
match k:
    case 'A':
        print("Vowel")
    case 'E':
        print("Vowel")
    case 'I':
        print("Vowel")
    case 'O':
        print("Vowel")
    case 'U':
        print("Vowel")
    case _:
        print("Not a vowel")