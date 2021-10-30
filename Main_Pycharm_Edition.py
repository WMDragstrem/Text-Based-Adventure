# Malachi Dragstrem
# Text Based Adventure Game WIP
# I recommend playing before checking the code
# because that'd be kinda cool I think
print(
    'GREETINGS! And welcome to my poorly optimized coding project/adventure!')
input("When you're ready for your GRAND STORY to begin, PRESS ENTER")
print(
    '\n You shoot awake from a deep slumber, your mind is foggy and your '
    'back aches.')
print(
    ' Looking down, you see stone floors. \n Your resting place was nothing '
    'more than a hardwood cot.')
print(
    ' Try as you might, you cannot recall how you arrived here, all you know '
    'is you gotta get out!')
print(
    ' Suddenly, amidst the fog, a single word makes its way into your '
    'mind.\n "Is it? It must be..."')

# Purposely vague when asking for name in hopes of comedic result
name = input(' What is that word? (Type your response) ')
name = name.capitalize()
# Capitalize command learned from
# https://www.geeksforgeeks.org/string-capitalize-python/
print('\n "Of course! My name must be', name + '."')


def press_enter():
    input('Press ENTER to continue.')


press_enter()

# need to format text to fit better, I don't know how though :)
# User realises they need to escape, identify items in cell,
# ask what they will do (For later project)
# Can't do that right now! Don't know if/else statements, RANDOM BS TIME
# (AKA the only way I can think to fit math into this to get a good grade)

# Included end= command a few times below (My teammate Erick Rodriguez
# showed me how to use it as I had no clue what it did)
print(
    '\n  Without warning, the iron door guarding the entrance to your cell '
    'suddenly EXPLODES open!',
)
print(' A man with a great beard and flowing robes appears before you.')

# concatenates the name with punctuation
print(' "I am the GREAT WIZARD BERBANDINO! And I have come to rescue YOU,',
      name + '!"')

# sep= command makes it so there's no space between
# whats in quotes and what isn't when outputted
print('\n "Me?? ', name, '?"', sep='')

# concatenates the name with punctuation, again, and
# repeats it 3 times in the middle of the sentence
# (with punctuation)
print('\n "That' + "'s right! I've come for", (name + ', ') * 3 + 'and ONLY',
      name + '!"')

# when i know how to make libraries the player will choose
# here whether or not to trust the wizard.


print(
    '\n "As magnificent as you may seem, how do I know I can trust you '
    'BERBANDINO?" You inquire.')
num1 = int(input(
    '\n "Hmmm..." mutters the wizard, "QUICK! Name your favorite whole '
    'number! And then press ENTER! '))

# Adds 1 to the given numeric input
print('\n "Wow!', "That's pretty neat! (Personally, my favorite number is",
      num1 + 1, end='')
print(' but to each their own I guess..)"')

# I included a concatenation in the line below because it kept thinking I
# was starting a new string when i used quotes/apostrophes within
# quotes/apostrophes
print(' "Now, what is your LEAST favorite whole number?"')

# Concatenation to include apostrophes in quotes
print(
    ' "What do you mean you don\'t have one? Don\'t tell me you\'re one of '
    'THOSE guys."')
num2 = int(input(' "JUST PICK ONE:" '))
while num2 == num1:
    num2 = int(input(
        ' "Erm... no... that number won\'t work"\n"Try a different one:" '))
if num2 == (num1 + 1):
    print(' "MOCK ME WILL YOU!?!"\n "Fine..."')

else:
    print('\n "EXCELLENT!"')
print(
    ' "Now, watch in amazement as I, the GREAT BERBANDINO wow you with my '
    'awesome MATHEMATICAL POWERS!"\n')
press_enter()

# basic addition
print('\n "' + str(num1), "+", num2, "=", str(num1 + num2) + '"', )
print('\n "WOW!" you exclaim.')
print('\n "Now watch THIS!"')
# '0.2f' limits output of below equation to 2 decimals,
# equation written is same as stated by program
# / just does normal division
print(' "The square of the sum of', num1, 'and', num2,
      ' when divided by the difference of', num2, 'and', num1,
      'gives you:', end=' ')
print(str(format(((num1 + num2) ** 2) / (num2 - num1), '0.2f') + '"'))
# // divides then rounds
print(' "Or if you' + "'re", 'a prude who only accepts integers:',
      int(((num1 + num2) ** 2) // (num2 - num1)), end='')

# % divides and outputs the remainder
print(' with a remainder of', str(((num1 + num2) ** 2) % (num2 - num1)) + '"')
press_enter()
print('\n You fall down to your knees')
print(
    '\n "Clearly I am not worthy of being in your presence oh dear', end='')
print(' BERBANDINO, yet I must implore you to save me."')
print(
    '\n "Very well then, but first I must test your mathematical '
    'abilities..."')
print(
    ' "Answer these questions three and I shall see whether or not you are '
    'WORTHY."')

# Player has to answer several math problems and wizard will allow them to
# continue if they get at least 2/3 right. If they get 0 right they lose the
# game.
while True:
    totalPoints = 0
    math1 = int(input('\n "WHAT is 1+1?" '))
    math2 = int(input(' "WHAT is my favorite number?" '))
    math3 = input(
        ' "WHAT is the meaning of life, the universe, and everything?" ')
    if math1 == 2:
        totalPoints += 1
    if math2 == num1 + 1:
        totalPoints += 1
    # 42 is formatted as a str below since its likely people will respond with
    # something other than a number for the 3rd question if they don't get
    # the reference
    while math3 == 'God' or math3 == 'god':
        print(
            '"Well... that could be interpreted as correct.. yes. But '
            'that\'s not exactly what im looking for."')
        math3 = input(
            '"Try that one again:"\n"WHAT is the meaning of life, '
            'the universe, and everything?" ')
    if math3 == '42':
        totalPoints += 1
    finalScore = totalPoints / 3
    if finalScore == 1:
        print('\n "Astounding! You are beyond worthy!"')
        break
    elif finalScore == 2 / 3:
        print(
            '\n "Well... you got a 66% so at least it wasn''t an F...  '
            'YOU ARE WORTHY!"')

        break
    elif finalScore == 1 / 3:
        # there's that required != operator!
        if math3 != '42':
            print(
                ' "Pathetic... only one correct answer. Yet, you show promise,'
                ' TRY AGAIN"')
        else:
            print('"H- uh- wuh huh- HOO UH???? You can answer the impossible '
                  'question... YET YOU MISSED THE 2 QUESTIONS '
                  'PRIOR!?!"')
            print(' *sigh* "I shall declare you worthy, ONLY because I wish '
                  'to see what else you are hiding from me..."')
            break
    else:
        # First possible ending if zero answers are correct
        print('\nZERO?? You got ZERO CORRECT!?!?!')
        input('Press ENTER to continue')
        for interval in range(1000):
            print('YOU SUCK')
        print('ENDING UNLOCKED: Incomprehensibly Incompetent')
        import sys

        sys.exit()
# i found out about the above function at
# https://stackoverflow.com/questions/73663/how-to-terminate-a-script

press_enter()

# The While loop below doesn't terminate until a certain action is input that
# renders gameComplete as True
print('\n "Now your adventure begins... Each decision from here on out '
      'must be your own. Good luck', name + '."')
print(' "Type what you would like to do next, one word at a time please."')
print(' "Type "help" if you need some guidance."')

# numActions will keep track of the amount of cycles the player goes through
# the loop. At the end it will display how many inputs they had to type to
# beat the game.
gameComplete = False
numActions = 0
location = 'dungeon'
inventory = []


# Here's the required function that accepts a parameter, it's slightly
# adds item to end of inventory list
def add_item(item):
    inventory.append(item)
    print('"' + item + '"', 'has been successfully added to your inventory.')

    # Temporary function for debugging
    print('Your inventory is:', inventory)


# This function provides an easy way to include an error message anywhere
# whenever the user gives incorrect input
def failed_input():
    if action == 'grab':
        print(' "I don\'t think that\'s something I need to grab."')
    elif action == 'move':
        print(' "I can\'t get there."')
    else:
        print(' "I don\'t understand..."')


# There's my required not boolean vvv
while not gameComplete:

    # Action will be the recurring variable used to store the users input into
    # the game. progress is determined based on whether they input the correct
    # series of actions
    # lower command found at
    # https://www.programiz.com/python-programming/methods/string/lower
    # has to be included so program doesn't bug out if someone capitalizes
    # their input
    action = input()
    action = action.lower()
    if action == 'help':
        print('\nHey there! This command will be modified as time goes on!')
        print('To get out of the dungeon, you must type what actions you')
        print('deem necessary to escape. These commands come in the form')
        print('of ONE word! Such as "search", "interact", "move"')
        print('"inventory", "grab", "drop", and some that you will have')
        print('to discover yourself!\n\n')
        print('STRATEGY GUIDE\n--------------')
        print('Always make sure to inspect your surroundings, you never')
        print('know just how close the key to the puzzle may be. Also,')
        print('experiment!! try all sorts of combos of commands if you\'re')
        print('stuck!\n\n')
        print('That\'s all for now! Best of luck!')
    elif action == 'search' and location == 'dungeon':
        print('You gaze around the room before you, as noted before, '
              'it doesn\'t contain much in terms of decor...')
        print('The explosion caused by the wizard has cracked the stone '
              'floors and left a sharp rock at your feet.')
    elif action == 'grab':
        grab2 = input('What would you like to grab?\n')
        if location == 'dungeon':
            if grab2 == 'rock':
                add_item(grab2)
            else:
                failed_input()
    # Another temporary code for debugging
    elif action == 'numactions':
        print('Currently, numActions is at:', numActions)

    else:
        failed_input()
    numActions += 1

# I definitely need to add some try/except statements to prevent errors with
# some of the input statements. for now, however, that can wait
