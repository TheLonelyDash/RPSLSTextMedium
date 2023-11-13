import random

options = {'a':'Rock', 'b':'Paper', 'c':'Scissors', 'd':'Lizard', 'e':'Spock'}
results = {'Ties': 0, "Wins": 0, "Losses": 0}

def playerChoice():
    while True:
        choice = input('\nChoose your weapon: ').lower()
        if choice == 'q': quit()
        if choice in options: return choice
        else: print('yeah...you didn\'t choose a weapon...')

def computerChoice():
    return random.choice(list(options.keys()))

def compare(pc, cc):
    if pc == cc: return 1
    elif \
        (pc == 'a' and (cc == 'd' or cc == 'c')) or \
        (pc == 'b' and (cc == 'a' or cc == 'e')) or \
        (pc == 'c' and (cc == 'a' or cc == 'd')) or \
        (pc == 'd' and (cc == 'e' or cc == 'b')) or \
        (pc == 'e' and (cc == 'c' or cc == 'a')):
        return 2
    else: return 3

def playGame():
    print('\nWelcome to Rock, Paper, Scissors, Lizard, Spock...a weird game I just created.')
    for letter, weapon in options.items(): print(letter.upper() + ". " + weapon)
    print('Q. Quit')

    pc,cc = playerChoice(), computerChoice()
    num = compare(pc, cc)

    print('You chose ' + options[pc] + ' and the computer chose ' + options[cc] + ".")

    if num == 1:
        results['Ties'] += 1 
        print('You tied!')
    elif num == 2: 
        results['Wins'] += 1 
        print('You win!')
    else: 
        results['Losses'] += 1 
        print("You lose!")

    print ('Wins: ' + str(results["Wins"]) + ',  Losses: ' + str(results["Losses"]) + ', Ties: ' + str(results['Ties']) + '.')

    return playGame()

playGame()