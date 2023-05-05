# Simple Text Adventure Project
import string
import random
import secrets
import time




#region Predefined lists to check against user responses 

#92
names_list = ['Abdullah', 'Aiko', 'Akira', 'Alejandro', 'Ali', 'Amelia', 'Ana', 'Ananya', 'Andreas', 'Anika', 'Ari', 'Arjun', 'Arman', 'Arvid', 'Ava', 'Ayman', 'Azra', 'Bao', 'Bartosz', 'Bela', 'Ben', 'Benjamin', 'Beyza', 'Bianca', 'Bodhi', 'Bogdan', 'Bojana', 'Bonnie', 'Bradley', 'Brayden', 'Brianna', 'Brittany', 'Bruce', 'Bryan', 'Calvin', 'Cameron', 'Carina', 'Carl', 'Carla', 'Carlos', 'Carolina', 'Caroline', 'Carter', 'Cassandra', 'Catherine', 'Cecilia', 'Cedric', 'Celia', 'Chantal', 'Charis', 'Charles', 'Charlotte', 'Chen', 'Cheryl', 'Chiara', 'Chloe', 'Chris', 'Christine', 'Chun', 'Cindy', 'Claire', 'Clara', 'Clarissa', 'Cole', 'Colin', 'Colton', 'Connor', 'Constantin', 'Corey', 'Courtney', 'Cristina', 'Cynthia', 'Daisy', 'Dakota', 'Dana', 'Daniel', 'Daniela', 'Daphne', 'Daria', 'Darius', 'David', 'Dawid', 'Dean', 'Delia', 'Denis', 'Deniz', 'Derek', 'Desiree', 'Diana', 'Diego', 'Dimitris', 'Dino', 'Dominic', 'Dominik', 'Donna', 'Dora', 'Dorian', 'Dorota', 'Dorothy', 'Douglas', 'Drew', 'Dylan', 'Edgar', 'Edith', 'Edwin', 'Eileen', 'Eleanor', 'Elena', 'Eliana', 'Elias', 'Elif', 'Elisa', 'Elisabeth', 'Elizabeth', 'Ella', 'Ellen', 'Ellie', 'Elodie', 'Elsa', 'Emilia', 'Emily', 'Emma', 'Emmanuel', 'Eric', 'Erica', 'Erika', 'Erin', 'Esther', 'Ethan', 'Eva', 'Evan', 'Evelina', 'Evelyn', 'Evie', 'Fabian', 'Faith', 'Fang', 'Fanny', 'Farid', 'Fatima', 'Federico', 'Felipe', 'Felix', 'Fiona', 'Florian', 'Francesca', 'Francis', 'Frank', 'Frankie', 'Fred', 'Gabriel', 'Gael', 'Gage', 'Gareth', 'Garrett', 'Gavin', 'George', 'Georgia', 'Georgina', 'Gerald', 'Gia', 'Gideon', 'Gina', 'Giulia', 'Gloria', 'Grace', 'Gracie', 'Grant', 'Greg', 'Gregory', 'Greta', 'Guillermo', 'Gustav', 'Hailey', 'Haley', 'Hana', 'Hanna', 'Hannah', 'Hao', 'Harold', 'Harry', 'Hayden', 'Heather', 'Heidi', 'Helen', 'Helena', 'Henry', 'Hiroshi', 'Holly', 'Hong', 'Hope', 'Howard', 'Hugo', 'Hunter', 'Ian', 'Ibrahim', 'Ida', 'Igor', 'Ilayda', 'Iman', 'Imogen', 'Ines', 'Ingrid', 'Ioanna', 'Iris', 'Isaac', 'Isabel', 'Isabella', 'Isabelle', 'Isaiah', 'Isidora', 'Isis', 'Ismail', 'Ivana', 'Ivanna', 'Ivo', 'Ivy', 'Izabela', 'Izabella', 'Izzy', 'Jack', 'Jackson', 'Jacob', 'Jacqueline', 'Jade', 'Jaden', 'Jae', 'Jai', 'Jaime', 'Jakob', 'Jalen', 'James', 'Jamie', 'Jana', 'Jane', 'Janet', 'Janina', 'Jared', 'Jasmin', 'Jasmine', 'Jason', 'Jasper', 'Jay', 'Jayden', 'Jayla', 'Jazmin', 'Jean', 'Jeff', 'Jeffrey', 'Jemma', 'Jenna', 'Jennifer', 'Jenny', 'Jeremy', 'Jerry', 'Jessica', 'Jessie', 'Jett', 'Jia', 'Jillian', 'Jim', 'Joanna', 'Jocelyn', 'Joe', 'Joel', 'Joey', 'John', 'Johnny', 'Jonah', 'Jonathan', 'Jordan', 'Jordi', 'Jorge', 'Jose', 'Joseph', 'Josh', 'Joshua', 'Josiah', 'Joy', 'Joyce', 'Juan', 'Judith', 'Jules', 'Julia', 'Julian', 'Juliana', 'Julianna', 'Julie', 'Julien', 'Juliet', 'Juliette', 'June', 'Juniper', 'Justin', 'Justine', 'Kaden', 'Kaitlyn', 'Kalea', 'Kaleb', 'Kamila', 'Kara', 'Karen', 'Karina', 'Karla', 'Karolina', 'Kasey', 'Kasper', 'Kassandra', 'Kate', 'Katelyn', 'Katherine', 'Kathleen', 'Kathryn', 'Katie', 'Katja', 'Katrina', 'Kay', 'Kayla', 'Kaylee', 'Keira', 'Keith', 'Kelly', 'Kelsey', 'Kendra', 'Kenneth', 'Kenny', 'Kevin', 'Kiera', 'Kierra', 'Kim', 'Kimberley', 'Kimberly', 'Kingsley', 'Kira', 'Kirsten', 'Klaudia', 'Klaus', 'Knox', 'Kris', 'Krista', 'Kristen', 'Kristin', 'Kristina', 'Kristine', 'Kristoffer', 'Krystal', 'Kurt', 'Kyla', 'Kyle', 'Kyler', 'Kylie', 'Lacey', 'Laila', 'Lana', 'Lara', 'Larissa', 'Lars', 'Laura', 'Lauren', 'Laurie', 'Lavinia', 'Lawrence', 'Layla', 'Lea', 'Leah', 'Leandro', 'Leanne', 'Lee', 'Leif', 'Leila', 'Lena', 'Leo', 'Leon', 'Leona', 'Leonard', 'Leonardo', 'Leslie', 'Leticia', 'Levi', 'Levy', 'Liam', 'Lila', 'Lilia', 'Lilian', 'Liliana', 'Lilith', 'Lillian', 'Lilly', 'Lily', 'Lina', 'Linda', 'Linnea', 'Lionel', 'Lisa', 'Lisbeth', 'Lise', 'Lisette', 'Liv', 'Livia', 'Liz', 'Liza', 'Lizbeth', 'Lizette', 'Logan', 'Lois', 'Lola', 'Lolita', 'Lora', 'Loren', 'Lorena', 'Lorene', 'Lorenzo', 'Lori', 'Lorraine', 'Lotus', 'Lou', 'Louie', 'Louis', 'Louisa', 'Louise', 'Lourdes', 'Luca', 'Lucas', 'Lucia', 'Lucian', 'Luciana', 'Luciano', 'Lucie', 'Lucien', 'Lucinda', 'Lucrezia', 'Lucy', 'Ludovic', 'Ludovica', 'Luigi', 'Luis', 'Luka', 'Lukas', 'Luke', 'Lula', 'Lulu', 'Luna', 'Luz', 'Lydia', 'Lyla', 'Lyle', 'Lynda', 'Lynn', 'Lynne', 'Lysandra', 'Mabel', 'Macey', 'Mackenzie', 'Macy', 'Madalena', 'Maddie', 'Maddison', 'Madeleine', 'Madeline', 'Madelyn', 'Madison', 'Madisyn', 'Madonna', 'Mae', 'Maeva', 'Magdalena', 'Maggie', 'Magnus', 'Maia', 'Maira', 'Maisie', 'Maja', 'Makayla', 'Makenzie', 'Malak', 'Malcolm', 'Maleah', 'Malia', 'Malik', 'Malin', 'Mallory', 'Malte', 'Mandy', 'Manuel', 'Manuela', 'Mara', 'Marc', 'Marcel', 'Marcela', 'Marcelina', 'Marceline', 'Marcella', 'Marcello', 'Marcellus', 'Marcia', 'Marco', 'Marcus', 'Marek', 'Maren', 'Margaret', 'Margarida', 'Margaux', 'Marge', 'Margie', 'Margot', 'Maria', 'Mariah', 'Mariam', 'Marian', 'Mariana', 'Marianna', 'Marianne', 'Maribel', 'Marie', 'Mariela', 'Marilyn', 'Marina', 'Marine', 'Mario', 'Marion', 'Marisa', 'Marisol', 'Marit', 'Marita', 'Maritza', 'Mark', 'Marko', 'Markus', 'Marla', 'Marlee', 'Marlene', 'Marley', 'Marlon', 'Marlowe', 'Marly', 'Marlyn', 'Marnie', 'Marsha', 'Marshall', 'Mart', 'Marta', 'Martha', 'Martina', 'Martinus', 'Marty', 'Marv', 'Marvin', 'Mary', 'Maryam', 'Maryann', 'Marybeth', 'Masen', 'Mason', 'Mat', 'Matheo', 'Mathew', 'Mathias', 'Mathilda', 'Mathilde', 'Matias', 'Matilda', 'Matilde', 'Matt', 'Matthew', 'Matthias', 'Matthew', 'Maud', 'Maureen', 'Maurice', 'Mauricio', 'Mauro', 'Mavis', 'Max', 'Maxim', 'Maxime', 'Maximilian', 'Maximiliano', 'Maximilianus', 'Maximus', 'Maxine', 'Maxwell', 'May', 'Maya', 'Mayra', 'Mckenzie', 'Meadow', 'Meagan', 'Megan', 'Meghan', 'Mei', 'Meike', 'Meira', 'Melanie', 'Melchior', 'Melina', 'Melinda', 'Melissa', 'Melody', 'Melvin', 'Mena', 'Mendel', 'Mercedes', 'Mercy', 'Meredith', 'Merle', 'Merlin', 'Merlyn', 'Merrill', 'Merritt', 'Mervin', 'Meryl', 'Meta', 'Mia', 'Micah', 'Michael', 'Michaela', 'Michal', 'Michel', 'Michele', 'Michelle', 'Mickey', 'Mieke', 'Mies', 'Miguel', 'Mika', 'Mikael', 'Mikaela', 'Mike', 'Mikhail', 'Mila', 'Milan', 'Mildred', 'Milena', 'Miles', 'Millicent', 'Millie', 'Milo', 'Milton', 'Mimi', 'Mina', 'Minerva', 'Ming', 'Minh', 'Minna', 'Minnie', 'Mira', 'Mirabelle', 'Miracle', 'Miranda', 'Miriam', 'Mirjam', 'Miroslav', 'Mischa', 'Missy', 'Misty', 'Mitch', 'Mitchell', 'Mittie', 'Moa', 'Moana', 'Mohammed', 'Moira', 'Mollie', 'Molly', 'Mona', 'Monica', 'Monika', 'Monique', 'Montana', 'Monte', 'Montgomery', 'Montserrat', 'Morgan', 'Morgane', 'Morris', 'Morten', 'Morton', 'Moses', 'Moss', 'Muriel', 'Musa', 'Mustafa', 'Mya', 'Myah', 'Mylene', 'Myra', 'Myriam', 'Myrna', 'Myron', 'Nadia', 'Nadine', 'Nahla', 'Nala', 'Nana', 'Nancy', 'Nanette', 'Nanna', 'Naomi', 'Napoleon', 'Nash', 'Nasir', 'Natalia', 'Natalie', 'Natan', 'Nate', 'Nathan', 'Nathanael', 'Nathaniel', 'Nava', 'Naveen', 'Naya', 'Neal', 'Ned', 'Neela', 'Nefertiti', 'Neil', 'Nelda', 'Nelia', 'Nell', 'Nella', 'Nelle', 'Nellie', 'Nelly', 'Nelson', 'Nenagh', 'Nerea', 'Nereus', 'Nevada', 'Nevaeh', 'Neve', 'Niamh', 'Nicholas', 'Nichole', 'Nick', 'Nicki', 'Nicklas', 'Nicky', 'Niclas', 'Nicodemus', 'Nicolette', 'Nicolas', 'Nicole', 'Nigel', 'Nik', 'Nike', 'Nikhil', 'Niki', 'Sigurd', 'Sigyn', 'Silas', 'Silja', 'Silke', 'Silvana', 'Silvia', 'Simba', 'Simen', 'Simeon', 'Simon', 'Simone', 'Sina', 'Sindre', 'Siobhan', 'Siri', 'Sirius', 'Sita', 'Siv', 'Sive', 'Siyabonga', 'Skylar', 'Skyler', 'Slavica', 'Sloan', 'Sloane', 'Smilla', 'Sol', 'Solange', 'Solomon', 'Solveig', 'Sondre', 'Sonia', 'Sonja', 'Sonny', 'Sonya', 'Sophia', 'Sophie', 'Sora', 'Soraya', 'Soren', 'Sorin', 'Spencer', 'Spike', 'Stacey', 'Staci', 'Stacie', 'Stacy', 'Stan', 'Stanislaus', 'Stanislav', 'Stanley', 'Star', 'Stavros', 'Stefan', 'Stefanie', 'Stefano', 'Stella', 'Stephan', 'Stephania', 'Stephanie', 'Stephen', 'Sterling', 'Steve', 'Steven', 'Stian', 'Stig', 'Storm', 'Stratton', 'Stuart', 'Sue', 'Sukie', 'Sulaiman', 'Sullivan', 'Summer', 'Sun', 'Sunniva', 'Sunny', 'Suri', 'Surya', 'Susa', 'Susan', 'Susana', 'Susann', 'Susanna', 'Susanne', 'Susie', 'Suzan', 'Suzanne', 'Suzette', 'Suzie', 'Suzuki', 'Svea', 'Sven', 'Svetlana', 'Sybil', 'Sydney', 'Sylvester', 'Sylvia', 'Sylvie', 'Synne', 'Sølvi', 'Søren', 'Sølve', 'Sølvi', 'Søren', 'Sølve', 'Sønnøve', 'Tabatha', 'Tabitha', 'Taddeo', 'Tadeusz', 'Tadhg', 'Tae', 'Tahlia', 'Tahnee', 'Tahsin', 'Tai', 'Taina', 'Taisiya', 'Tait', 'Taiwo', 'Taj', 'Takumi', 'Tala', 'Talia', 'Talitha', 'Tallulah', 'Talullah', 'Tam', 'Tamara', 'Tamera', 'Tami', 'Tamia', 'Tamika', 'Tamina', 'Tamir', 'Tammi', 'Tammie', 'Tammy', 'Tancred', 'Tane', 'Taneli', 'Tanesha', 'Tania', 'Tanja', 'Tanner', 'Tansy', 'Tanya', 'Tao', 'Tara', 'Taran', 'Tarek', 'Tariq', 'Taryn', 'Tasha', 'Tasia', 'Tasneem', 'Tate', 'Tatum', 'Tatyana', 'Taurin', 'Taurus', 'Tawanda', 'Tawanna', 'Tawny', 'Tayla', 'Taylor', 'Teagan', 'Ted', 'Teddy', 'Teemu', 'Tegan', 'Teija', 'Tejas', 'Tekla']
yes_list = ['Yes', 'Y', 'Ya', 'Yeah', 'Sure']
no_list = ['No', 'N', 'Na', 'Nah', 'Nope']
stat_list = ['Weak', 'Average', 'Strong']
height_list = ['Short', 'Average', 'Tall']
beauty_list = ['Ugly', 'Average', 'Beautiful']
#endregion

#region allowed_lists
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
#endregion

#region response()
# Check if user enters 'Yes', 'No' or something else
def response():
    match = False
    while not match:
        responding = input('Are you here to participate?\n').capitalize()
        if responding in yes_list:
            match = True
            input(f'\nWonderful.')

        elif responding in no_list:
            input('\nI see.')
            input('Unfortunately, you may not loiter.')
            input('Farewell.')
            print('(The connection has been closed.)')
            exit()
        else:
            input('\nThe question is simple.')
#endregion

#region random_chars()
def random_chars():
    for i in range(1, 60):
        num = random.randrange(1, 25) 
        res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num))
        num2 = random.randrange(1, 25) 
        res2 = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num2))
        print((str(res) + names_list[random.randrange(0, 922)] + str(res2)).center(50))
        time.sleep(.05)
#endregion

# Start the game   
input('Welcome.')
input('It is very nice to have you here.')
response()
#If user responds with yes, start game, otherwise end
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
random_chars()
input('You awaken in a soft bed. The bright sunlight is streaming in through the window and there are birds chirping outside. You can hear a dog barking in the distance.' )
































