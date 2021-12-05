"""My COP 1500 Text-Based Adventure/Integration Project"""
__Author__ = "William Malachi Dragstrem"

import sys


def main():
    """This is the start of the code for the game. It introduces the scenery
    and asks the player for their name to establish the input/output style
    of play. The body of the game itself is in another function"""
    print(
        'GREETINGS! And welcome to my poorly optimized coding '
        'project/adventure!')
    input("When you're ready for your GRAND STORY to begin, PRESS ENTER")
    print(
        '\n You shoot awake from a deep slumber, your mind is foggy and your '
        'back aches.')
    print(
        ' Looking down, you see stone floors. \n Your resting place was '
        'nothing more than a hardwood cot.')
    print(
        ' Try as you might, you cannot recall how you arrived here, all '
        'you know is you gotta get out!')
    print(
        ' Suddenly, amidst the fog, a single word makes its way into your '
        'mind.\n "Is it? It must be..."')

    # Purposely vague when asking for name in hopes of comedic result
    name = input(' What is that word? (Type your response) ')
    name = name.capitalize()
    # Capitalize command learned from
    # https://www.geeksforgeeks.org/string-capitalize-python/

    print('\n "Of course! My name must be', name + '."')

    # If the player chooses to do the next portion, it still leads to them
    # playing the game.

    press_enter()
    game_continue = 0
    print(' Now, would you like to skip the next part, which serves only to '
          'ensure that the math requirements for this project are fulfilled?')

    while game_continue == 0:
        y_n = lower_input('Y or N?: ')
        if y_n == 'y':
            game_continue = 1
            game(name)
        elif y_n == 'n':
            game_continue = 1
            math_portion(name)
        else:
            print(' A simple "Y" or "N" will suffice.')


def math_portion(name_input):
    name = name_input

    # RANDOM BS TIME
    # (AKA the only way I can think to fit math into this to get a good grade)

    # Included end= command a few times below (My teammate Erick Rodriguez
    # showed me how to use it as I had no clue what it did)
    print(
        '\n  Without warning, the iron door guarding the entrance to your '
        'cell suddenly EXPLODES open!',
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
    print('\n "That' + "'s right! I've come for",
          (name + ', ') * 3, 'and ONLY',
          name + '!"', 'He booms')

    print(
        '\n "As magnificent as you may seem, how do I know I can trust you '
        'BERBANDINO?" You inquire.')
    num1 = num_input(
        '\n "Hmmm..." mutters the wizard, "QUICK! Name your favorite whole '
        'number! And then press ENTER! ')

    # Adds 1 to the given numeric input
    print('\n "Wow!', "That's pretty neat! (Personally, my favorite number is",
          num1 + 1, end='')
    print(' but to each their own I guess..)"')

    print(' "Now, what is your LEAST favorite whole number?"')

    print(
        ' "What do you mean you don\'t have one? Don\'t tell me you\'re one '
        'of THOSE guys."')
    num2 = num_input(' "JUST PICK ONE:" ')
    while num2 == num1:
        num2 = num_input(
            ' "Erm... no... that number won\'t work"\n"Try a different one:" ')
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
    print(' with a remainder of',
          str(((num1 + num2) ** 2) % (num2 - num1)) + '"')
    press_enter()
    print('\n You fall down to your knees')
    print(
        '\n "Clearly I am not worthy of being in your presence oh dear',
        end='')
    print(' BERBANDINO, yet I must implore you to save me."')
    print(
        '\n "Very well then, but first I must test your mathematical '
        'abilities..."')
    print(
        ' "Answer these questions three and I shall see whether or not you '
        'are WORTHY."')

    # Player has to answer several math problems and wizard will allow them to
    # continue if they get at least 2/3 right. If they get 0 right they
    # lose the game.
    while True:
        totalPoints = 0
        math1 = num_input('\n "WHAT is 1+1?" ')
        math2 = num_input(' "WHAT is my favorite number?" ')
        math3 = input(
            ' "WHAT is the meaning of life, the universe, and everything?" ')
        if math1 == 2:
            totalPoints += 1
        if math2 == num1 + 1:
            totalPoints += 1
        # 42 is formatted as a str below since its likely people will respond
        # with something other than a number for the 3rd question if they
        # don't get the reference
        while math3 == 'God' or math3 == 'god':
            print(
                '"Well... that could be interpreted as correct.. yes. But '
                'that\'s not exactly what im looking for."')
            math3 = input(
                '"Try that one again:"\n"WHAT is the meaning of life, '
                'the universe, and everything?"\n ')
        if math3 == '42':
            totalPoints += 1
        finalScore = totalPoints / 3
        if finalScore == 1:
            print('\n "Astounding! You are beyond worthy!"')
            break
        elif finalScore == 2 / 3:
            print(
                '\n "Well... you got a 66% so at least it wasn\'t an F...  '
                'YOU ARE WORTHY!"')

            break
        elif finalScore == 1 / 3:
            # there's that required != operator!
            if math3 != '42':
                print(
                    ' "Pathetic... only one correct answer. Yet, '
                    'you show promise, TRY AGAIN"')
            else:
                print(
                    '"H- uh- wuh huh- HOO UH???? You can answer the '
                    'impossible question... YET YOU MISSED THE 2 QUESTIONS '
                    'PRIOR!?!"')
                print(
                    ' *sigh* "I shall declare you worthy, ONLY because I wish '
                    'to see what else you are hiding from me..."')
                break
        else:
            # First possible ending if zero answers are correct
            print('\nZERO?? You got ZERO CORRECT!?!?!')
            input('Press ENTER to continue')
            for interval in range(1000):
                print('YOU SUCK')
            print('ENDING UNLOCKED: Incomprehensibly Incompetent')

            sys.exit()
    # I found out about the above sys.exit() function at
    # https://stackoverflow.com/questions/73663/how-to-terminate-a-script

    press_enter()
    game(name)


def game(name_input):
    name = name_input
    # The While loop below doesn't terminate until a certain action is input
    # that renders gameComplete as True
    print(' "Now your adventure begins... Each decision from here on out '
          'must be your own. Good luck', name + '."')
    print(' "Type what you would like to do next, one word at a time please."')
    print(' "Type "help" if you need some guidance."')

    # numActions will keep track of the amount of cycles the player goes
    # through the loop. At the end it will display how many inputs they had
    # to type to beat the game.
    gameComplete = False
    numActions = 0
    location = 'dungeon'
    inventory = []

    # Locations that are unavailable unless a certain action is performed:
    dungeon_open = False

    # There's my required not boolean vvv
    while not gameComplete:

        # Action will be the recurring variable used to store the users input
        # into the game. Progress is determined based on whether they input
        # the correct series of actions.
        # .lower command used to set all input as lowercase found at
        # https://www.programiz.com/python-programming/methods/string/lower
        # has to be included so program doesn't bug out if someone capitalizes
        # their input

        action = lower_input('>>>')

        if action == 'help':
            print(
                '\nHey there! This command will be modified as time goes on!')
            print('To get out of the dungeon, you must type what actions you')
            print('deem necessary to escape. These commands come in the form')
            print('of ONE word! Such as "search", "inspect", "move"')
            print('"inventory", "grab", "use", and some that you will have')
            print('to discover yourself! If your attempt fails, you have to\n '
                  'type the command again, it doesn\'t save the last command\n'
                  'executed.')
            print('(Not all of these words are guaranteed to work currently) '
                  '\n\n')
            print('STRATEGY GUIDE\n--------------')
            print('Always make sure to inspect your surroundings, you never')
            print('know just how close the key to the puzzle may be. Also,')
            print(
                'experiment!! try all sorts of combos of commands if you\'re')
            print('stuck!\n\n')
            print('That\'s all for now! Best of luck!')
        elif action == 'inventory':
            print('your current inventory is:', inventory)

        elif action == 'search' and location == 'dungeon':
            print('You gaze around the room before you, as noted before, '
                  'it doesn\'t contain much in terms of decor...')
            print('The explosion caused by the wizard has cracked the stone '
                  'floors and left sharp rocks at your feet.'
                  '\nFor some reason, the wizard replaced the door and its '
                  'lock upon his exit.')
            numActions += 1
        # All the possible outcomes for the grab command
        elif action == 'grab':
            grab2 = lower_input('What would you like to grab?\n>>>')
            if location == 'dungeon':
                if grab2 not in inventory:
                    if grab2 == 'rock' or grab2 == 'rocks':

                        add_item('rock', inventory)
                    else:
                        failed_input(action)
                else:
                    print('"I can\'t grab another one."')
            numActions += 1
        # All the possible outcomes for the use command
        elif action == 'use':
            used_item = lower_input('What would you like to use?\n>>>')
            if used_item in inventory:
                use_on = lower_input('What will you use it on?\n>>>')
                if location == 'dungeon':
                    if use_on == 'door' or use_on == 'lock':
                        if used_item == 'rock':
                            if dungeon_open is False:
                                print('You SMASH off the door\'s locks. You '
                                      'can now move on to the hallway')
                                dungeon_open = True
                            elif dungeon_open is True:
                                print('"I don\'t think I need to do that '
                                      'again"')
                        else:
                            failed_input(action)
                    else:
                        failed_input(action)
            else:
                print('"I don\'t have that on me."')

        elif action == 'move':
            destination = lower_input('Where to?\n>>>')
            if destination == 'hallway':
                print('You make your way to the hallway.')
                location = 'hallway'
                press_enter()
                gameComplete = True
            else:
                failed_input(action)

        # Another temporary code for debugging
        elif action == 'numactions':
            print('Currently, numActions is at:', numActions)
        # Easy way to terminate program
        elif action == 'quit':
            sys.exit()
        # 'I don't understand'
        else:
            failed_input(action)
        # numActions is an accumulator that keeps track of how many times the
        # while loop went through
        numActions += 1
    # Ending text
    print('\nCongrats! You escaped in', numActions, 'actions.')
    print('(Yeah I know "how exciting" I had to reformat my code several times'
          '\nover as I learned new things throughout the semester, so I '
          'didn\'t\nactually spend much time on the gameplay itself AND I got'
          '\nCalc and Physics finals to study for.)'
          '\nI hope you enjoyed this mess of a game regardless :)')


def press_enter():
    """This code is just a quick shortcut to reduce clutter in the main
    function as this line of code will be frequently repeated."""
    input('\nPress ENTER to continue.\n')


def num_input(msg):
    """This is a simple try/except loop that accepts input only if its an
    integer,otherwise it prints an error message and asks the user to input
    again."""
    input_invalid = True
    print(msg)
    while input_invalid:
        try:
            num_int = int(input())
            input_invalid = False
            return num_int
        except ValueError:
            print(' Errrm.... try again, I was asking for a WHOLE NUMBER. '
                  'Not whatever that was.')


def add_item(item, inventory):
    """This function is used to add more items to the users inventory as
    they collect items within the game"""
    inventory.append(item)
    print('"' + item + '"',
          'has been successfully added to your inventory.')

    # Optional print function for debugging in line below
    # print('Your inventory is:', inventory)


def failed_input(action):
    """This code prints a line whenever the user tries to perform an action
    that isn't necessary/available in their current location or if they try
    to perform an action on something that doesn't exist"""
    if action == 'grab':
        print(' "I don\'t think that\'s something I need to grab."')
    elif action == 'move':
        print(' "I can\'t get there."')
    elif action == 'use':
        print('"I don\'t see that being very productive."')
    elif action == 'move':
        print('"I can\'t get there from here."')
    else:
        print(' "I don\'t understand..."')


def lower_input(txt):
    """This allows the program to take in an input (with txt being the
    prompt for the input) and then return it as all lowercase so as to
    enable easier coding"""
    response = input(txt)
    return response.lower()


# I could likely streamline the commands for each action using function
# definitions, but I started the actual game too late for such an overhaul.
# So for now it will just be coded in the same manner as is.
# I would also like to include a timer in the future to allow a smoother
# delivery of text rather than a big wall all at once.


main()
