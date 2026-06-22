import random
import string

U = string.ascii_uppercase
L = string.ascii_lowercase
D = string.digits
S = string.punctuation
ALL = U + L + D + S

def generate_password(length=12):

    password = random.choices(ALL, k=length)

    indices = random.sample(range(length), 4)
   
    password[indices[0]] = random.choice(U)
    password[indices[1]] = random.choice(L)
    password[indices[2]] = random.choice(D)
    password[indices[3]] = random.choice(S)
    
    return "".join(password)

if __name__ == "__main__":
    try:
        n = int(input("Length (min 4): "))
        if n >= 4:
            print(generate_password(n))
        else:
            print("Error: Minimum length is 4.")
    except ValueError:
        print("Error: Invalid number.")