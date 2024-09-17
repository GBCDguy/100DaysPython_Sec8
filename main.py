"""
def my_function():
    # Do this
    # Do this
    # And do this

my_function()
"""


def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")


greet()

"""
Def my_function(input):
    # Do this with input
    # Do this
    # And do this
"""


def adv_greet(name):
    print(f"Hello {name}.")
    print(f"How do you do {name}?")
    print(f"How's the weather today {name}?")


adv_greet("Glenn")

'''Life in weeks'''


def life_in_weeks(age):
    year_span = 90 - age
    return year_span * 52


age = int(input(""))
week_span = life_in_weeks(age)
print(f"You have {week_span} weeks left.")


def greet(name, location):
    """Make a greeting"""
    print(f"Hello {name}")
    print(f"How do you do?")
    print(f"How's the weather today in {location}?")


greet(name="Glenn", location="Jakarta")
"""Love calculator"""


def calculate_love_score(name_1, name_2):
    TRUE_WORD = ['t', 'r', 'u', 'e']
    LOVE_WORD = ['l', 'o', 'v', 'e']

    true_score = 0
    love_score = 0
    for key_letter in TRUE_WORD:
        for key_name in name_1.lower():
            if key_letter == key_name:
                true_score += 1
        for key_name in name_2.lower():
            if key_letter == key_name:
                true_score += 1
    for key_letter in LOVE_WORD:
        for key_name in name_1.lower():
            if key_letter == key_name:
                love_score += 1
        for key_name in name_2.lower():
            if key_letter == key_name:
                love_score += 1
    print(f"{true_score}{love_score}")


name_male = input("Please input the male name:\n\t")
name_female = input("Please input the female name:\n\t")
calculate_love_score(name_male, name_female)

"""Ceaser Cypher"""
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Decrypt / Encrypt:\t").lower()
text = input("Please kindly input your text:\n\t").lower()
shift = int(input("Please type in shift number: "))


# TODO 1: Create encrypt function with shift and text as the input
def encrypt(original_text, shift_amount):
    # TODO 2: Shift the original text with the amount shifted
    shifted_text = ''
    for letter in original_text:
        # For alphabetical word
        if letter in ALPHABET:
            index_in_alphabet = ALPHABET.index(letter)
            shifted_letter = ALPHABET[index_in_alphabet + shift_amount + 26]
            shifted_text += shifted_letter
        # For spaces
        else:
            shifted_text += letter
    print(shifted_text)


# TODO 3: Create decrypt function with shift and text as the input
def decrypt(original_text, shift_amount):
    # TODO 4: Shift the original text with the amount shifted
    shifted_text = ''
    for letter in original_text:
        # For alphabetical word
        if letter in ALPHABET:
            index_in_alphabet = ALPHABET.index(letter)
            shifted_letter = ALPHABET[index_in_alphabet - shift_amount + 26]
            shifted_text += shifted_letter
        # For spaces
        else:
            shifted_text += letter
    print(shifted_text)


# TODO 5: Ask the cypher to encrypt or decrypt
if direction == 'encrypt':
    encrypt(text, shift)
else:
    decrypt(text, shift)
