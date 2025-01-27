import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    if encode_or_decode == 'decode':
        shift_amount *= 1
    for letter in original_text:
        if letter in alphabet:
            new_index = alphabet.index(letter) + shift_amount
            new_index %= len(alphabet)  # range from 0 to 25
            output_text += alphabet[new_index]
        else:
            # If the character is not in the alphabet, keep it as is
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True
while should_continue:
    direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:")).lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: /n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart[0] == 'n':
        should_continue = False
        print("Goodbye")