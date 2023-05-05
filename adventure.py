# Simple Text Adventure Project



# Predefined lists to check against user responses 
yes_list = ['Yes', 'Y', 'Ya', 'Yeah', 'Sure']
no_list = ['No', 'N', 'Na', 'Nah', 'Nope']
stat_list = ['Weak', 'Average', 'Strong']
height_list = ['Short', 'Average', 'Tall']
beauty_list = ['Ugly', 'Average', 'Beautiful']



# Branching depending on users input
def allowed_lists(_list):
    match = False
    # Checking if there is a match in the stat_list
    if _list == stat_list:
        while not match:
            for item in _list:
                print(item)
            stat = input('\nEnter It\'s body type:\n').capitalize()
            if stat in _list:
                match = True
                input(f'\n{stat}. Splendid. Truly splendid.')
                return stat
            else:
                input('No, that won\'t work.')
                input('Your options are below.\n')
    # Checking if there is a match in the height_list
    if _list == height_list:
        while not match:
            for item in _list:
                print(item)
            height = input('\nEnter It\'s height: ').capitalize()
            if height in _list:
                match = True
                input(f'\nIt is {height}. Magnificent.')
                return height
            else:
                input('No, that won\'t work.')
                input('Your options are below.\n') 
    # Checking if there is a match in the beauty_list 
    if _list == beauty_list:
        while not match:
            for item in _list:
                print(item)
            beauty = input('\nEnter what It looks like: ').capitalize()
            if beauty in _list:
                match = True
                input(f'\nAmazing. It is {beauty}.')
                return beauty
            else:
                input('No, that won\'t work.')
                input('Your options are below.\n')  

#If user responds with yes, start game, otherwise end
def start_game():

# Have the user input their name and characteristics
    name = input('Please enter It\'s name: ')
    input(f'\n{name}...')
    input('Yes, of course. That is a wonderful name.')
    input('Please enter It\'s height. Below are your choices:\n')
    height = allowed_lists(height_list)
    input('Now, please enter It\'s body type. Your choices are below:\n')
    stat = allowed_lists(stat_list)
    input('Finally, how does It look?\n')
    beauty = allowed_lists(beauty_list)
    input('\nI trust you have put a lot of thought into It\'s traits.')
    input('However, it displeases me to tell you these choices do not matter.\n')
    input('You see...')
    input('In this world, we do not get to choose who we are.\n')
    input(f'({name} has been discarded.)\n')
    input('It\'s name will be...\n')



# Check if user enters 'Yes', 'No' or something else
def response():
    match = False
    while not match:
        responding = input('Are you here to participate?\n:').capitalize()
        if responding in yes_list:
            match = True
            input(f'\nWonderful.')
            start_game()

        elif responding in no_list:
            input('\nI see.')
            input('Unfortunately, you may not loiter.')
            input('Farewell.')
            print('(The connection has been closed.)')
            match = True
            return
        else:
            input('\nThe question is simple.')








            
input('Welcome.')
input('It is very nice to have you here.')
response()

































