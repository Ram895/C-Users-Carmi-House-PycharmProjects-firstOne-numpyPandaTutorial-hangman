def main():

    """Main hangman game.
    Use Python 3.
    """

    old_letters_guessed = []
    MAX_TRIES = 7
    HANGMAN_PHOTOS = dict()

#---------------------------------------------------------------------------------

    def choose_word(file_path, index):
        """This function accepts a path of a file and a place index in file
        it returns the word in place of index given.
        :param file_path the path to source  file
        :param index of  a secret word  in the file
        :return  secret word"""

        f = open( file_path, 'r' )
        file_contents = f.read()

        #find_word
        #index given, begin from 1 not from 0

        notFound = True

        splitted = file_contents.split()

        while notFound:
            if index == 0:
                word = splitted[index ]
                notFound = False
            elif notFound and index<=len(splitted)-1:
                word = splitted[index-1]
                notFound = False
            else:
                index = index - len(splitted)-1
        f.close()
        return word

#---------------------------------------------------------------------------------------

    def print_hangman(num):
        """This function prints the states of a hangman depending on the user's guess try.
        :param num_of_tries an input from player
        :return  the printed status of hangman"""


        num = int(num)
        pic0 = (
'''
x-------x''' )
        HANGMAN_PHOTOS[ 1 ] = pic0

        pic1 = (
'''
x-------x
|
|
|
|
| ''' )
        HANGMAN_PHOTOS[ 2 ] = pic1



        pic2 = (
'''
x-------x
|       |
|       0
|
|
| ''' )
        HANGMAN_PHOTOS[ 3 ] = pic2



        pic3 = (
'''
x-------x
|       |
|       0
|       |
|
| ''' )
        HANGMAN_PHOTOS[ 4 ] = pic3


        pic4 = (
'''
x-------x
|       |
|       0
|      /|\\    
|
|''' )
        HANGMAN_PHOTOS[ 5 ] = pic4


        pic5 = (
'''
x-------x
|       |
|       0
|      /|\\
|      /
|''' )
        HANGMAN_PHOTOS[ 6 ] = pic5

        
        pic6 = (
'''
x-------x
|       |
|       0
|      /|\\
|      / \\
|''' )

        HANGMAN_PHOTOS[ 7 ] = pic6
        HANGMAN_PHOTOS[8] = " "
        HANGMAN_PHOTOS[9] = " "

        return HANGMAN_PHOTOS[num]

#----------------------------------------------------------------------------------------

    def input_from_player():
        # Python Program to check character is Alphabet or not
        letter_guessed = ''
        while True:
            letter_guessed = input( "Guess a letter: " )
            letter_guessed_len = letter_guessed.__len__()
            if letter_guessed_len == 1 and ((letter_guessed >= 'a' and letter_guessed <= 'z') or
                                        (letter_guessed >= 'A' and letter_guessed <= 'Z')):
                break
            else:
                print("Allowed only one Alphbet letter, try again....")
        if letter_guessed.lower() not in old_letters_guessed:
            # set the players guess to guesses
            old_letters_guessed.append( letter_guessed )
            if letter_guessed not in secret_word:
                print( "X", "\n\n" )
        elif letter_guessed_len == 1 and not ((letter_guessed >= 'a' and letter_guessed <= 'z') or
                                              (letter_guessed >= 'A' and letter_guessed <= 'Z')):
            print( "X" )
        return  letter_guessed

    
    def fill_letter_to_guessed_word():

        for letter1 in old_letters_guessed:
            for indx, letter in enumerate( secret_word ):
                if letter1 != letter:
                    continue
                else:
                    guessed_word.pop( indx )
                    guessed_word.insert( indx, letter1 )
        return guessed_word

#----------------------------------------------------------------------------------


    def check_for_finish():
        for elemet, value in enumerate( secret_word ):
            if guessed_word[ elemet ] != value:
                return False
        return True

#-----------------------------------------------------------------------------------------

    def show_hidden_word(secret_word, old_letters_guessed):
        """This function shows the letter that the  player guesses from the letters of the secret word.
            :param secret_word is a string of alphbete characters
            :param old_letters_guessed is list of alphbete character the player guessed
            :return  string containing the result of players guessed of the secret word
                        characters missing from the secret word represented with underscors"""


        i = 1
        for guess in range( MAX_TRIES ):
            b = input_from_player()
            picture = print_hangman( i+1 )
            print( ':( ' )
            print( '\n' )
            if not ((i == MAX_TRIES) or  (i == num_choosed)):
                print(picture)
            # print( 'Guessed letter:  ', b )

            a = fill_letter_to_guessed_word()
            print( ' '.join( a ) )


            if (i == MAX_TRIES) or  (i == num_choosed) :
                picture = print_hangman(7)
                print(picture,'\n')
                # print('turn #',i, 'num_turns_asked ',num_choosed)
                print( "LOSE" )


            if check_for_finish():
                print( "WIN\n" )
                print( f"You win !!! it takes you {i} guesses." )
                break

            if (i == MAX_TRIES) or (i == num_choosed):
                break

            i += 1




#-----------------------------------------------------------------------------------------

    def check_file_exsistment(file1):
        """This function checks validity of path, if file exists, returns Boolean True.
        :param path for file
        :return  Boolean"""

        try:
            f=open(file1,'r')
            f.close
            return True
        except IOError:
            print('File not found, try again')
            return False

#---------------------------------------------------------------------------------------

    def input_number(string_question):
        """This function return only valid integer  number .
        :param  string_question a string use to decide what question to display
        :return integer number  from players input"""

        if string_question == 'number_of_tries' :
            what_to_disply = "Enter how many guess? "
        elif string_question == 'word_secret_location' :
            what_to_disply = "Enter location of secret word in file? "

        check = True
        while check:
            user_input = input( what_to_disply )
            try:
                val = int( user_input )
                check = False
            except ValueError:
                try:
                    val = float( user_input )
                    print( "Input is a float  number. Number = ", val )
                except ValueError:
                    print( "No.. input is not a number. It's a string" )
            if string_question == 'number_of_tries' :
                check = False
        return val

#-------------------------------------------------------------------------------------
#   ----------------------------
    #This is the main game flow
#   ----------------------------

    #step #1
    # welcoming the user
    name = input( "What is your name? \n" )
    print( "Hello, " + name, ", time to play hangman!" )

    #print the logo of the game
    print( ''' 
             _    _                                         
            | |  | |                                        
            | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
            |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | |  | | (_| | | | | (_| | | | | | | (_| | | | |
            |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                 __/ |                      
                                |___/''' )

    start = 1
    result = print_hangman(start)
    print(result,'\n\n')
#***************************************************

    #step #2
    while True:

        file_name =input("Enter path to the file where secret words are? ")
        # needed for running program in my station at home
        path = "C:\\Users\\Carmi House\\PycharmProjects\\firstOne\\numpyPandaTutorial"
        #
        result = check_file_exsistment( file_name )
        if result == True:
            print('\n')
            break

#*******************************************************

    #step #3
    # here we set the secret word and number of tries for game

    while True:
        num_choosed =  input_number('number_of_tries')
        if num_choosed <= MAX_TRIES:
            print('\n')
            break

    position = input_number('word_secret_location')
    secret_word = choose_word(file_name, position)
    #print(secret_word)     for testing purpose only

#*********************************************************

    #step 4  initialize the gueesed word
    guessed_word = len( secret_word ) *  ['_']
    guessed_word_toScreen =   len( secret_word ) *  '_'
    print(guessed_word_toScreen)

#***********************************************************

    #step #5  guessing process
    show_hidden_word( secret_word, old_letters_guessed )


if __name__ == '__main__':
    main()
