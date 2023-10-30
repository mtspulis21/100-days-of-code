alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(chipher_direction,start_text,shift_size):
    new_text = ""
    if chipher_direction == "decode":
        shift_size *= -1
    for letter in  start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_size) % 26
            new_text += alphabet[new_position]
        else:
            new_text = letter
    print(f'{chipher_direction} text is {new_text}')

end_program = False
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(chipher_direction=direction,start_text=text,shift_size=shift)

    restart = input("Restart program? Y or N?").lower()
    if restart == "n":
        end_program = True