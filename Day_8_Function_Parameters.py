def greet_with_name (name, location):
    print(f'Hello {name} !!')
    print(f'How is the weather in {location} ?')

greet_with_name('Vikas', 'Toronto') # positional argument
greet_with_name(location='Toronto', name='Vikas') # keyword argument

# 'name' is a parameter
# "Vikas" is the argument

##### Life in Weeks #####
# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f'You have {weeks_left} weeks left.')

# Call your function with hard coded values
life_in_weeks(12)

##### Love calculator #####
def calculate_love_score(name1, name2):
    true_num = 0
    love_num = 0
    for letter in 'TRUE':
        for alpha in name1.upper()+name2.upper():
            if alpha == letter:
                true_num +=1

    for letter in 'LOVE':
        for alpha in name1.upper()+name2.upper():
            if alpha == letter:
                love_num +=1

    print(f'Love Score = {true_num}{love_num}')

calculate_love_score("Vikas Kaushik", "Prerna Sharma")

#### Caesar Cypher ####

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encrypt the cipher
# 1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# 2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#    by the shift amount and print the encrypted text.

def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet) # 0-25
        encrypted_letter = alphabet[shifted_position]

        encrypted_text += encrypted_letter

    print(f'Here is the encoded result: {encrypted_text}')

# 4: What happens if you try to shift z forwards by 9? Can you fix the code?

# 3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#    message.

# encrypt(original_text=text, shift_amount=shift)


# Decrypt the cipher
# 1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# 2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#    by the shift amount and print the decrypted text.
# 3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#    Use the value of the user chosen 'direction' variable to determine which functionality to use.

def decrypt(original_text, shift_amount):
    decrypted_text = ''
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount

        shifted_position %= len(alphabet) # 0-25
        encrypted_letter = alphabet[shifted_position]

        decrypted_text += encrypted_letter

    print(f'Here is the decoded result: {decrypted_text}')


# decrypt(original_text=text, shift_amount=shift)

def caesar(original_text, shift_amount, direction):
    if direction == 'encode':
        encrypt(original_text=text, shift_amount=shift)
    elif direction =='decode':
        decrypt(original_text=text, shift_amount=shift)
    else:
        print(f'You chose the wrong direction: {direction}. Accepted values are encode/decode')

caesar(original_text=text, shift_amount=shift, direction=direction)