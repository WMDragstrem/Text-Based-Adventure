# Malachi Dragstrem
# Text Based Adventure Game WIP
# I recommend playing before checking the code because that'd be kinda cool I think
print('GREETINGS! And welcome to my poorly optimized coding project/adventure!')
input("When you're ready for your GRAND STORY to begin, PRESS ENTER")
print('\n You shoot awake from a deep slumber, your mind is foggy and your back aches.')
print(' Looking down, you see stone floors. \n Your resting place was nothing more than a hardwood cot.')
print(' Try as you might, you cannot recall how you arrived here, all you know is you gotta get out!')
print(' Suddenly, amidst the fog, a single word makes its way into your mind.\n "Is it? It must be..."')

#Purposely vague when asking for name in hopes of comedic result
name = input(' What is that word? (Type your response) ')
print('\n "Of course! My name must be',name + '."')

def press_enter():
    input('Press ENTER to continue.')
press_enter()

#need to format text to fit better, I don't know how though :)
# User realises they needto escape, identify items in cell, ask what they will do (For later project)
# Can't do that right now! Don't know if/else statements, RANDOM BS TIME
# (AKA the only way I can think to fit math into this to get a good grade)

# Included end= command a few times below (My teammate Erick Rodriguez showed me how to use it as I had no clue what it did)
print('\n  Without warning, the iron door guarding the entrance to your cell suddenly EXPLODES open!', end='')
print(' A man with a great beard and flowing robes appears before you.')

# concatenates the name with punctuation
print(' "I am the GREAT WIZARD BERBANDINO! And I have come to rescue YOU,', name + '!"')

# sep= command makes it so there's no space between whats in quotes and what isn't when outputted
print('\n "Me?? ', name, '?"',sep = '')

# concatenates the name with punctuation, again, and repeats it 3 times in the middle of the sentence
#(with punctuation)
print('\n "That'+"'s right! I've come for", (name + ', ') * 3 + 'and ONLY', name + '!"')



#when i know how to make libraries the player will choose here whether or not to trust the wizard.



print('\n "As magnificent as you may seem, how do I know I can trust you BERBANDINO?" You inquire.')
num1 = int(input('\n "Hmmm..." mutters the wizard, "QUICK! Name your favorite whole number! And then press ENTER! '))

# Adds 1 to the given numeric input
print('\n "Wow!', "That's pretty neat! (Personally, my favorite number is", num1 + 1, end='')
print(' but to each their own I guess..)"')

# I included a concatenation in the line below because it kept thinking I was starting a new string
#when i used quotes/apostrophes within quotes/apostrophes
print(' "Now, what is your LEAST favorite whole number?"')

# Concatenation to include apostrophes in quotes
print(' "What do you mean you don\'t have one? Don\'t tell me you\'re one of THOSE guys."')
num2 = int(input('"JUST PICK ONE:" '))
while num2 == num1:
    num2 = int(input('"Erm... no... that number won\'t work"\n"Try a different one:" '))
if num2 == (num1 + 1):
    print('"MOCK ME WILL YOU!?!"\n"Fine..."')

else:
    print('\n "EXCELLENT!"')
print(' "Now, watch in amazement as I, the GREAT BERBANDINO wow you with my awesome MATHEMATICAL POWERS!"')

#basic addition
print('\n "' + str( num1), "+", num2,"=", str(num1 + num2)+'"', )
print('\n "WOW!" you exclaim.')
print('\n "Now watch THIS!"')
# '0.2f' limits output of below equation to 2 decimals, equation written is same as stated by program
# / just does normal division
print(' "The square of the sum of', num1, 'and', num2, ' when divided by the difference of', num2, 'and', num1, 'gives you:', end=' ')
print(str(format(((num1 + num2) ** 2) / (num2 - num1),'0.2f') + '"'))
# // divides then rounds
print(' "Or if you'+"'re", 'a prude who only accepts integers:', int(((num1 + num2) ** 2) // (num2 - num1)), end = '')

# % divides and outputs the remainder
print(' with a remainder of', str(((num1 + num2) ** 2) % (num2 - num1)) +'"')
press_enter()
print('\n You fall down to your knees')
print('\n "Clearly I am not worthy of being in your presence oh dear BERBANDINO, yet I must implore you to save me."')
print('\n "Very well then, but first I must test your mathematical abilities..."')
print(' "Answer these questions three and I shall see whether your claims of unworthiness are TRUE or FALSE"')


#Player has to answer several math problems and wizard will allow them to continue
#if they get at least 2/3 right. If they get 0 right they lose the game.
while True:
    totalPoints = 0
    math1 = int(input('\n "WHAT is 1+1?" '))
    math2 = int(input(' "WHAT is my favorite number?" '))
    math3 = input(' "WHAT is the meaning of life, the universe, and everything?" ')
    if math1 == 2:
        totalPoints +=1
    if math2 == num1 + 1:
        totalPoints +=1
# 42 is formatted as a str below since its likely people will respond with something other than a number for the
#3rd question if they don't get the reference
    while math3 == 'God' or math3 == 'god':
        print('"Well... that could be interpreted as correct.. yes. But that\'s not exactly what im looking for."')
        math3 = input('"Try that one again:"\n"WHAT is the meaning of life, the universe, and everything?" ')
    if math3 == '42':
        totalPoints +=1        
    finalScore = totalPoints / 3
    if finalScore == 1:
        print('\nAstounding! You are beyond worthy!')
        break
    elif finalScore == 2/3:
        print('\nWell... you got a 66% so at least it wasn''t an F... YOU ARE WORTHY!')
        break
    elif finalScore == 1/3:
        print('Pathetic... only one correct answer. Yet, you show promise, TRY AGAIN')
    else:
        print('\nZERO?? You got ZERO CORRECT!?!?!')
        input('Press ENTER to continue')
        for interval in range(1000):
            print('YOU SUCK')
        print('ENDING UNLOCKED: Incomprehensibly Incompetent')
        import sys
        sys.exit()
        #i found out about the above function at https://stackoverflow.com/questions/73663/how-to-terminate-a-script    


press_enter()
print('SIKE!!! thats all there is for now.')

##print(not((math1 == 2) and (math2 == num1 + 1) or (math3 == str(42))), '."', sep='')
##input('Press ENTER to continue!')

# No further sources needed
#(I know its probably hard to tell due to how MASTERFULLY optimized this is)

# Sorry if I included too many comments, I didn't know if you wanted me to include a new one every time
#I used an operator or only once for each one
