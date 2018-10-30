hangman_parts = [
    "head",
    "left arm",
    "torso",
    "right arm",
    "left leg",
    "right leg"
    ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist",
    "supercalifragilistiexpealidocious"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        # how did you even get here?
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)

#check a guess to see if it is correct

#Get input from console
name = input("What is you name:")
print("Hello",name, "! Time to play hangman!")

#Let user input a guess, then check and see if it is correct
word = 'test'

wrong_guesses = 0

while wrong_guesses < num_wrong_guesses_allowed:
    guess = input('guess a letter:').lower()
    if guess in word:
        print(guess, "is Correct")
    else:
        print(guess, "is Incorrect!")
        wrong_guesses = wrong_guesses + 1
        draw_hangman(wrong_guesses)