# Simple Text Adventure Project
import string
import random
import secrets
import time






#region Names
# 92 names
names_list = ['Abdullah', 'Aiko', 'Akira', 'Alejandro', 'Ali', 'Amelia', 'Ana', 'Ananya', 'Andreas', 'Anika', 'Ari', 'Arjun', 'Arman', 'Arvid', 'Ava', 'Ayman', 'Azra', 'Bao', 'Bartosz', 'Bela', 'Ben', 'Benjamin', 'Beyza', 'Bianca', 'Bodhi', 'Bogdan', 'Bojana', 'Bonnie', 'Bradley', 'Brayden', 'Brianna', 'Brittany', 'Bruce', 'Bryan', 'Calvin', 'Cameron', 'Carina', 'Carl', 'Carla', 'Carlos', 'Carolina', 'Caroline', 'Carter', 'Cassandra', 'Catherine', 'Cecilia', 'Cedric', 'Celia', 'Chantal', 'Charis', 'Charles', 'Charlotte', 'Chen', 'Cheryl', 'Chiara', 'Chloe', 'Chris', 'Christine', 'Chun', 'Cindy', 'Claire', 'Clara', 'Clarissa', 'Cole', 'Colin', 'Colton', 'Connor', 'Constantin', 'Corey', 'Courtney', 'Cristina', 'Cynthia', 'Daisy', 'Dakota', 'Dana', 'Daniel', 'Daniela', 'Daphne', 'Daria', 'Darius', 'David', 'Dawid', 'Dean', 'Delia', 'Denis', 'Deniz', 'Derek', 'Desiree', 'Diana', 'Diego', 'Dimitris', 'Dino', 'Dominic', 'Dominik', 'Donna', 'Dora', 'Dorian', 'Dorota', 'Dorothy', 'Douglas', 'Drew', 'Dylan', 'Edgar', 'Edith', 'Edwin', 'Eileen', 'Eleanor', 'Elena', 'Eliana', 'Elias', 'Elif', 'Elisa', 'Elisabeth', 'Elizabeth', 'Ella', 'Ellen', 'Ellie', 'Elodie', 'Elsa', 'Emilia', 'Emily', 'Emma', 'Emmanuel', 'Eric', 'Erica', 'Erika', 'Erin', 'Esther', 'Ethan', 'Eva', 'Evan', 'Evelina', 'Evelyn', 'Evie', 'Fabian', 'Faith', 'Fang', 'Fanny', 'Farid', 'Fatima', 'Federico', 'Felipe', 'Felix', 'Fiona', 'Florian', 'Francesca', 'Francis', 'Frank', 'Frankie', 'Fred', 'Gabriel', 'Gael', 'Gage', 'Gareth', 'Garrett', 'Gavin', 'George', 'Georgia', 'Georgina', 'Gerald', 'Gia', 'Gideon', 'Gina', 'Giulia', 'Gloria', 'Grace', 'Gracie', 'Grant', 'Greg', 'Gregory', 'Greta', 'Guillermo', 'Gustav', 'Hailey', 'Haley', 'Hana', 'Hanna', 'Hannah', 'Hao', 'Harold', 'Harry', 'Hayden', 'Heather', 'Heidi', 'Helen', 'Helena', 'Henry', 'Hiroshi', 'Holly', 'Hong', 'Hope', 'Howard', 'Hugo', 'Hunter', 'Ian', 'Ibrahim', 'Ida', 'Igor', 'Ilayda', 'Iman', 'Imogen', 'Ines', 'Ingrid', 'Ioanna', 'Iris', 'Isaac', 'Isabel', 'Isabella', 'Isabelle', 'Isaiah', 'Isidora', 'Isis', 'Ismail', 'Ivana', 'Ivanna', 'Ivo', 'Ivy', 'Izabela', 'Izabella', 'Izzy', 'Jack', 'Jackson', 'Jacob', 'Jacqueline', 'Jade', 'Jaden', 'Jae', 'Jai', 'Jaime', 'Jakob', 'Jalen', 'James', 'Jamie', 'Jana', 'Jane', 'Janet', 'Janina', 'Jared', 'Jasmin', 'Jasmine', 'Jason', 'Jasper', 'Jay', 'Jayden', 'Jayla', 'Jazmin', 'Jean', 'Jeff', 'Jeffrey', 'Jemma', 'Jenna', 'Jennifer', 'Jenny', 'Jeremy', 'Jerry', 'Jessica', 'Jessie', 'Jett', 'Jia', 'Jillian', 'Jim', 'Joanna', 'Jocelyn', 'Joe', 'Joel', 'Joey', 'John', 'Johnny', 'Jonah', 'Jonathan', 'Jordan', 'Jordi', 'Jorge', 'Jose', 'Joseph', 'Josh', 'Joshua', 'Josiah', 'Joy', 'Joyce', 'Juan', 'Judith', 'Jules', 'Julia', 'Julian', 'Juliana', 'Julianna', 'Julie', 'Julien', 'Juliet', 'Juliette', 'June', 'Juniper', 'Justin', 'Justine', 'Kaden', 'Kaitlyn', 'Kalea', 'Kaleb', 'Kamila', 'Kara', 'Karen', 'Karina', 'Karla', 'Karolina', 'Kasey', 'Kasper', 'Kassandra', 'Kate', 'Katelyn', 'Katherine', 'Kathleen', 'Kathryn', 'Katie', 'Katja', 'Katrina', 'Kay', 'Kayla', 'Kaylee', 'Keira', 'Keith', 'Kelly', 'Kelsey', 'Kendra', 'Kenneth', 'Kenny', 'Kevin', 'Kiera', 'Kierra', 'Kim', 'Kimberley', 'Kimberly', 'Kingsley', 'Kira', 'Kirsten', 'Klaudia', 'Klaus', 'Knox', 'Kris', 'Krista', 'Kristen', 'Kristin', 'Kristina', 'Kristine', 'Kristoffer', 'Krystal', 'Kurt', 'Kyla', 'Kyle', 'Kyler', 'Kylie', 'Lacey', 'Laila', 'Lana', 'Lara', 'Larissa', 'Lars', 'Laura', 'Lauren', 'Laurie', 'Lavinia', 'Lawrence', 'Layla', 'Lea', 'Leah', 'Leandro', 'Leanne', 'Lee', 'Leif', 'Leila', 'Lena', 'Leo', 'Leon', 'Leona', 'Leonard', 'Leonardo', 'Leslie', 'Leticia', 'Levi', 'Levy', 'Liam', 'Lila', 'Lilia', 'Lilian', 'Liliana', 'Lilith', 'Lillian', 'Lilly', 'Lily', 'Lina', 'Linda', 'Linnea', 'Lionel', 'Lisa', 'Lisbeth', 'Lise', 'Lisette', 'Liv', 'Livia', 'Liz', 'Liza', 'Lizbeth', 'Lizette', 'Logan', 'Lois', 'Lola', 'Lolita', 'Lora', 'Loren', 'Lorena', 'Lorene', 'Lorenzo', 'Lori', 'Lorraine', 'Lotus', 'Lou', 'Louie', 'Louis', 'Louisa', 'Louise', 'Lourdes', 'Luca', 'Lucas', 'Lucia', 'Lucian', 'Luciana', 'Luciano', 'Lucie', 'Lucien', 'Lucinda', 'Lucrezia', 'Lucy', 'Ludovic', 'Ludovica', 'Luigi', 'Luis', 'Luka', 'Lukas', 'Luke', 'Lula', 'Lulu', 'Luna', 'Luz', 'Lydia', 'Lyla', 'Lyle', 'Lynda', 'Lynn', 'Lynne', 'Lysandra', 'Mabel', 'Macey', 'Mackenzie', 'Macy', 'Madalena', 'Maddie', 'Maddison', 'Madeleine', 'Madeline', 'Madelyn', 'Madison', 'Madisyn', 'Madonna', 'Mae', 'Maeva', 'Magdalena', 'Maggie', 'Magnus', 'Maia', 'Maira', 'Maisie', 'Maja', 'Makayla', 'Makenzie', 'Malak', 'Malcolm', 'Maleah', 'Malia', 'Malik', 'Malin', 'Mallory', 'Malte', 'Mandy', 'Manuel', 'Manuela', 'Mara', 'Marc', 'Marcel', 'Marcela', 'Marcelina', 'Marceline', 'Marcella', 'Marcello', 'Marcellus', 'Marcia', 'Marco', 'Marcus', 'Marek', 'Maren', 'Margaret', 'Margarida', 'Margaux', 'Marge', 'Margie', 'Margot', 'Maria', 'Mariah', 'Mariam', 'Marian', 'Mariana', 'Marianna', 'Marianne', 'Maribel', 'Marie', 'Mariela', 'Marilyn', 'Marina', 'Marine', 'Mario', 'Marion', 'Marisa', 'Marisol', 'Marit', 'Marita', 'Maritza', 'Mark', 'Marko', 'Markus', 'Marla', 'Marlee', 'Marlene', 'Marley', 'Marlon', 'Marlowe', 'Marly', 'Marlyn', 'Marnie', 'Marsha', 'Marshall', 'Mart', 'Marta', 'Martha', 'Martina', 'Martinus', 'Marty', 'Marv', 'Marvin', 'Mary', 'Maryam', 'Maryann', 'Marybeth', 'Masen', 'Mason', 'Mat', 'Matheo', 'Mathew', 'Mathias', 'Mathilda', 'Mathilde', 'Matias', 'Matilda', 'Matilde', 'Matt', 'Matthew', 'Matthias', 'Matthew', 'Maud', 'Maureen', 'Maurice', 'Mauricio', 'Mauro', 'Mavis', 'Max', 'Maxim', 'Maxime', 'Maximilian', 'Maximiliano', 'Maximilianus', 'Maximus', 'Maxine', 'Maxwell', 'May', 'Maya', 'Mayra', 'Mckenzie', 'Meadow', 'Meagan', 'Megan', 'Meghan', 'Mei', 'Meike', 'Meira', 'Melanie', 'Melchior', 'Melina', 'Melinda', 'Melissa', 'Melody', 'Melvin', 'Mena', 'Mendel', 'Mercedes', 'Mercy', 'Meredith', 'Merle', 'Merlin', 'Merlyn', 'Merrill', 'Merritt', 'Mervin', 'Meryl', 'Meta', 'Mia', 'Micah', 'Michael', 'Michaela', 'Michal', 'Michel', 'Michele', 'Michelle', 'Mickey', 'Mieke', 'Mies', 'Miguel', 'Mika', 'Mikael', 'Mikaela', 'Mike', 'Mikhail', 'Mila', 'Milan', 'Mildred', 'Milena', 'Miles', 'Millicent', 'Millie', 'Milo', 'Milton', 'Mimi', 'Mina', 'Minerva', 'Ming', 'Minh', 'Minna', 'Minnie', 'Mira', 'Mirabelle', 'Miracle', 'Miranda', 'Miriam', 'Mirjam', 'Miroslav', 'Mischa', 'Missy', 'Misty', 'Mitch', 'Mitchell', 'Mittie', 'Moa', 'Moana', 'Mohammed', 'Moira', 'Mollie', 'Molly', 'Mona', 'Monica', 'Monika', 'Monique', 'Montana', 'Monte', 'Montgomery', 'Montserrat', 'Morgan', 'Morgane', 'Morris', 'Morten', 'Morton', 'Moses', 'Moss', 'Muriel', 'Musa', 'Mustafa', 'Mya', 'Myah', 'Mylene', 'Myra', 'Myriam', 'Myrna', 'Myron', 'Nadia', 'Nadine', 'Nahla', 'Nala', 'Nana', 'Nancy', 'Nanette', 'Nanna', 'Naomi', 'Napoleon', 'Nash', 'Nasir', 'Natalia', 'Natalie', 'Natan', 'Nate', 'Nathan', 'Nathanael', 'Nathaniel', 'Nava', 'Naveen', 'Naya', 'Neal', 'Ned', 'Neela', 'Nefertiti', 'Neil', 'Nelda', 'Nelia', 'Nell', 'Nella', 'Nelle', 'Nellie', 'Nelly', 'Nelson', 'Nenagh', 'Nerea', 'Nereus', 'Nevada', 'Nevaeh', 'Neve', 'Niamh', 'Nicholas', 'Nichole', 'Nick', 'Nicki', 'Nicklas', 'Nicky', 'Niclas', 'Nicodemus', 'Nicolette', 'Nicolas', 'Nicole', 'Nigel', 'Nik', 'Nike', 'Nikhil', 'Niki', 'Sigurd', 'Sigyn', 'Silas', 'Silja', 'Silke', 'Silvana', 'Silvia', 'Simba', 'Simen', 'Simeon', 'Simon', 'Simone', 'Sina', 'Sindre', 'Siobhan', 'Siri', 'Sirius', 'Sita', 'Siv', 'Sive', 'Siyabonga', 'Skylar', 'Skyler', 'Slavica', 'Sloan', 'Sloane', 'Smilla', 'Sol', 'Solange', 'Solomon', 'Solveig', 'Sondre', 'Sonia', 'Sonja', 'Sonny', 'Sonya', 'Sophia', 'Sophie', 'Sora', 'Soraya', 'Soren', 'Sorin', 'Spencer', 'Spike', 'Stacey', 'Staci', 'Stacie', 'Stacy', 'Stan', 'Stanislaus', 'Stanislav', 'Stanley', 'Star', 'Stavros', 'Stefan', 'Stefanie', 'Stefano', 'Stella', 'Stephan', 'Stephania', 'Stephanie', 'Stephen', 'Sterling', 'Steve', 'Steven', 'Stian', 'Stig', 'Storm', 'Stratton', 'Stuart', 'Sue', 'Sukie', 'Sulaiman', 'Sullivan', 'Summer', 'Sun', 'Sunniva', 'Sunny', 'Suri', 'Surya', 'Susa', 'Susan', 'Susana', 'Susann', 'Susanna', 'Susanne', 'Susie', 'Suzan', 'Suzanne', 'Suzette', 'Suzie', 'Suzuki', 'Svea', 'Sven', 'Svetlana', 'Sybil', 'Sydney', 'Sylvester', 'Sylvia', 'Sylvie', 'Synne', 'Sølvi', 'Søren', 'Sølve', 'Sølvi', 'Søren', 'Sølve', 'Sønnøve', 'Tabatha', 'Tabitha', 'Taddeo', 'Tadeusz', 'Tadhg', 'Tae', 'Tahlia', 'Tahnee', 'Tahsin', 'Tai', 'Taina', 'Taisiya', 'Tait', 'Taiwo', 'Taj', 'Takumi', 'Tala', 'Talia', 'Talitha', 'Tallulah', 'Talullah', 'Tam', 'Tamara', 'Tamera', 'Tami', 'Tamia', 'Tamika', 'Tamina', 'Tamir', 'Tammi', 'Tammie', 'Tammy', 'Tancred', 'Tane', 'Taneli', 'Tanesha', 'Tania', 'Tanja', 'Tanner', 'Tansy', 'Tanya', 'Tao', 'Tara', 'Taran', 'Tarek', 'Tariq', 'Taryn', 'Tasha', 'Tasia', 'Tasneem', 'Tate', 'Tatum', 'Tatyana', 'Taurin', 'Taurus', 'Tawanda', 'Tawanna', 'Tawny', 'Tayla', 'Taylor', 'Teagan', 'Ted', 'Teddy', 'Teemu', 'Tegan', 'Teija', 'Tejas', 'Tekla']
#endregion

#region Predefined lists 
yes_list = ['Yes', 'Y', 'Ya', 'Yeah', 'Sure', 'Yea']
no_list = ['No', 'N', 'Na', 'Nah', 'Nope']
stats_list = ['Weak', 'Average', 'Strong']
height_list = ['Short', 'Average', 'Tall']
beauty_list = ['Ugly', 'Average', 'Beautiful']
npc_choose = [
    'That\'s quite alright, I will decide...',
    'I understand. Allow me to choose...',
    'Indecisive? How about this...',
    'I will choose for you.',
    'You can\'t decide? Then I will choose.',
    'Allow me to provide something in your stead...',
    'I will help you out.',
    'Hmm... How about...',
    'I will quickly pick for you...',
    'I can provide you with...'

    ]

typed_help = ['"Help"  - Provides a list of available user commands', 
                  '"Up"    - Same as "North" (Go North)', 
                  '"Down"  - Same as "South" (Go South)', 
                  '"Right" - Same as "East" (Go East)', 
                  '"Left"  - Same as "West" (Go West)', 
                  '"Inv"   - Inspect current inventory', 
                  '"Look"  - Inspect your surroundings. \n            Append with keywords to inspect things more closely (If available.) \n            Syntax: look book, look door, look rock.', 
                  '"Use"   - Use inventory item (if available.) \n            Append with keyword of desired item. \n            Syntax: use chocolatebar, use smoothstone, use twine', 
]

player = {
    'name': None,
    'height': None,
    'stats': None,
    'beauty': None,
}

inventory = {
    'chocolate_bar': True,
    'smooth_stone': True,
    'long_stick': False,
    'twine': False,
    'paperclip': False,
    'fork': False,
    'key_a': False,
    'key_b': False,
    'key_c': False,
}
#endregion

#region Help

def asked_for_help():
    if input().lower() == 'help' or input().lower() == 'h':
    #   print(typed_help)
        for i in typed_help:
            print(i)

#endregion

#region Rooms

room_list = ['2F Your Room?', '2F Hallway', '2F Bathroom', '2F Bedroom', 'Staircase', '1F Foyer', '1F Living Room', '1F Kitchen', '1F Office', 'Front Stoop',]

room_state = {
    '2F Your Room?': False, 
    '2F Hallway': False, 
    '2F Bathroom': False, 
    '2F Bedroom': False, 
    'Staircase': False, 
    '1F Foyer': False, 
    '1F Living Room': False, 
    '1F Kitchen': False, 
    '1F Office': False, 
    'Front Stoop': False,
}

#endregion

#region Yes or No

def choose():
    match = False
    while not match:
        choice = input('Are you satisfied with your choices?\n: ').capitalize()
        time.sleep(1)
        if choice in yes_list:
            match = True
            return choice
        elif choice in no_list:
            match = True
            return choice
        else:
            print('Would you kindly provide a proper reponse.')
            time.sleep(1)

def response():
    match = False
    while not match:
        responding = input('Are you here to participate?\n: ').capitalize()
        time.sleep(1)
        if responding in yes_list:
            match = True
            print(f'\nWonderful.')
            time.sleep(1)

        elif responding in no_list:
            print('\nI see...')
            time.sleep(2)
            print('Unfortunately, you may not loiter.')
            time.sleep(1)
            print('Farewell.')
            time.sleep(2)
            print('(The connection has been closed.)')
            time.sleep(3)
            exit()
        else:
            print('\nThe question is simple.')
            time.sleep(1)

#endregion

#region allowed_lists
# Branching depending on users input
def allowed_lists(_list):
    match = False
    # Checking if there is a match in the height_list
    if _list == height_list:
        while not match:
            for item in _list:
                print(item)
            height = input('\nEnter It\'s height.\n: ').capitalize()
            time.sleep(1)
            if height in _list:
                match = True
                print(f'\nIt is {height}.')
                time.sleep(2)
                print('Splendid.')
                time.sleep(2)
                print('Truly splendid.')
                time.sleep(2)
                return height
            if height == '':
                match = True
                print('\n' + npc_choose[random.randrange(0, 9)])
                time.sleep(1)
                height = height_list[random.randrange(0, 2)]
                print(f'It is {height}.')
                time.sleep(2)
                print('Splendid.')
                time.sleep(2)
                print('Truly splendid.')
                time.sleep(2)
                return height
            else:
                print('No, that won\'t work.')
                time.sleep(1)
                print('Your options are below.\n') 
                time.sleep(1)
    # Checking if there is a match in the stats_list
    if _list == stats_list:
        while not match:
            for item in _list:
                print(item)
            stats = input('\nEnter It\'s stature.\n: ').capitalize()
            time.sleep(1)
            if stats in _list:
                match = True
                print(f'{stats}.')
                time.sleep(2)
                print('Magnificent.')
                time.sleep(2)
                return stats
            if stats == '':
                match = True
                print('\n' + npc_choose[random.randrange(0, 9)])
                time.sleep(1)
                stats = stats_list[random.randrange(0, 2)]
                print(f'\n{stats}.')
                time.sleep(2)
                print('Magnificent.')
                time.sleep(2)
                return stats
            else:
                print('No, that won\'t work.')
                time.sleep(1)
                print('Your options are below.\n')
                time.sleep(1)
    # Checking if there is a match in the beauty_list 
    if _list == beauty_list:
        while not match:
            for item in _list:
                print(item)
            beauty = input('\nEnter what It looks like.\n: ').capitalize()
            if beauty in _list:
                match = True
                print(f'\nIt is {beauty}.')
                time.sleep(2)
                print('Amazing.')
                time.sleep(2)
                print('Absolutely amazing.')
                time.sleep(2)
                return beauty
            if beauty == '':
                match = True
                print('\n' + npc_choose[random.randrange(0, 9)])
                time.sleep(1)
                beauty = beauty_list[random.randrange(0, 2)]
                print(f'\nIt is {beauty}.')
                time.sleep(2)
                print('Amazing.')
                time.sleep(2)
                print('Absolutely amazing.')
                time.sleep(2)
                return beauty
            else:
                print('No, that won\'t work.')
                time.sleep(1)
                print('Your options are below.\n')  
                time.sleep(1)
#endregion

#region response()
# Check if user enters 'Yes', 'No' or something else
def response():
    match = False
    while not match:
        responding = input('Are you here to participate?\n: ').capitalize()
        time.sleep(1)
        if responding in yes_list:
            match = True
            print(f'\nWonderful.')
            time.sleep(1)

        elif responding in no_list:
            print('\nI see.')
            time.sleep(2)
            print('Unfortunately, you may not loiter.')
            time.sleep(1)
            print('Farewell.')
            time.sleep(2)
            print('(The connection has been closed.)')
            time.sleep(3)
            exit()
        else:
            print('\nThe question is simple.')
            time.sleep(1)
#endregion

#region random_chars()
def random_chars():
    for i in range(1, 60):
        num = random.randrange(1, 25) 
        res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num))
        num2 = random.randrange(1, 25) 
        res2 = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num2))
        print((str(res) + names_list[random.randrange(0, 922)] + str(res2)))
        time.sleep(.05)
#endregion

#region Character Setup
asked_for_help()
room = room_list[0]   
print('Welcome.')
time.sleep(1)
print('It is very nice to have you here.')
time.sleep(1)
response()
#If user responds with yes, start game, otherwise end
# Have the user input their name and characteristics
def char_setup():
    finalize = False
    while not finalize:
        name = input('\nPlease enter It\'s name.\n: ')
        if name == '':
            name = names_list[random.randrange(0, 922)]
            print('\n' + npc_choose[random.randrange(0, 9)])
            time.sleep(2)
        print(f'{name}...')
        time.sleep(2)
        print('Yes, of course. That is a wonderful name.\n')
        time.sleep(1)
        print('Please enter It\'s height. Below are your choices.\n')
        time.sleep(1)
        height = allowed_lists(height_list)
        print('Now, please enter It\'s stature. Your choices are below.\n')
        time.sleep(1)
        stats = allowed_lists(stats_list)
        print('Finally, how does It look?\n')
        time.sleep(1)
        beauty = allowed_lists(beauty_list)
        print('\nI trust you have put a lot of thought into It\'s traits.')
        time.sleep(2)
        print(f'It\'s name is: {name},')
        time.sleep(1)
        print(f'It\'s height is currently: {height},')
        time.sleep(1)
        print(f'It\'s stature is currently: {stats},')
        time.sleep(1)
        print(f'And it currently looks: {beauty}.')
        choice = choose()
        while choice in yes_list:
            player['name'] = name
            player['height'] = height
            player['stats'] = stats
            player['beauty'] = beauty
            print('Splendid, so we shall continue.')
            time.sleep(1)
            print('However...')
            time.sleep(2)
            print('It displeases me to tell you these choices do not matter.\n')
            time.sleep(2)
            print('You see...')
            time.sleep(2)
            print('In this world, we do not get to choose who we are.\n')
            time.sleep(2)
            print(f'({name} has been discarded.)\n')
            time.sleep(3)
            print('It\'s name...')
            time.sleep(2)
            print('will...')
            time.sleep(2)
            print('be...\n')
            time.sleep(2)
            random_chars()
            time.sleep(2)
            return player
        else:
            print('Alright, let us start over from the beginning.')
            time.sleep(2)
    
#endregion




#region Start Game
char_setup()    
print('\nYou awaken in a soft bed. The bright sunlight is streaming in through the window and there are birds chirping outside. You can hear a dog barking in the distance.' )

#endregion
























