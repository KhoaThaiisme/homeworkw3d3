# DESCRIPTION:
# Given a string, return a string that :
# Moves the first letter of each word to the end of it, then adds “ay” to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it(‘Pig latin is cool’) : ‘igPay atinlay siay oolcay’
# pig_it(‘Hello world !’)     : ‘elloHay orldway !’

def move(String):
    moved = []
    word = String.split()

    for char in word:
        if char != '!':
            char = char[1:]+char[0]+'ay'
            moved.append(char)
        else:
            moved.append(char)

    return (" ".join(moved))
    #    moved.append(char)
        # print(char[-1])

    # return moved


print(move('Hello world !'))
