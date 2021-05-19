
def main():

    '''Main hangman game.
    Use Python 3.
    '''

    HANGMAN_PHOTOS = dict()
    MAX_TRIES = 7
    old_letters_guessed = [ ]
    number_of_valid_guesses=0
    letter_guessed  = ''

#---------------------------------------------------------------------------

    def check_win():
        '''This function compare between the secret word and the guessed word
        :return   True if they are identical and  False if they are not .'''
        for elemet, value in enumerate( secret_word ):
            if guessed_word[ elemet ] != value:
                return False
        return True

#---------------------------------------------------------------------------
    def check_valid_input( letter_guessed):
        '''This function check if lletter guessed  is Alphabet or not
        :return   True if it is a valid input and False if it is not valid.'''

        if  ((letter_guessed >= 'a' and letter_guessed <= 'z') or
                (letter_guessed >= 'A' and letter_guessed <= 'Z')):
            return True
        else:
            return False
#-----------------------------------------------------------------------------------------

    def fill_letter_to_guessed_word():
        '''This function fills the letter guessed to the gessed word if it is in secret word
        if it is not guessed before.
        :return   the new guessed word'''

        for letter1 in old_letters_guessed:
            for indx, letter in enumerate( secret_word ):
                if letter1 != letter:
                    continue
                else:
                    guessed_word.pop( indx )
                    guessed_word.insert( indx, letter1 )
        return guessed_word


#-------------------------------------------------------------------------------------------

    def try_update_letter_guessed(number_of_valid_guesses, letter_guessed):
        '''This function shows the letter that the  player guesses from the letters of the secret word.
            :param secret_word is a string of alphbete characters
            :param old_letters_guessed is list of alphbete character the player guessed
            :return  string containing the result of players guessed of the secret word
                        characters missing from the secret word represented with underscors'''

        if (letter_guessed.lower() not in secret_word) and \
                (number_of_valid_guesses<int(num_of_tries_choosed)) and\
                (letter_guessed.lower() not in old_letters_guessed) and\
                check_win()== False :

            print( "X", "\n\n" )
            print( ':( ' )
            print( '\n' )
            picture = get_hangman_status( number_of_valid_guesses+1  )
            print(picture)
            print('\n')
            print( ''.join( guessed_word ) )

            old_letters_guessed.append( letter_guessed )
            return False

        if  (check_win() == False) and \
                (number_of_valid_guesses ==int(num_of_tries_choosed) ) and\
                (letter_guessed.lower() not in secret_word) and\
                (letter_guessed.lower() not in old_letters_guessed)   :

            print( "X", "\n\n" )
            print( ':( ' )
            print( '\n' )
            picture = get_hangman_status(7)
            print(picture,'\n')
            print( ''.join( guessed_word ) )
            print( "LOSE" )

            return False

        if  (check_win() == False) and\
                (number_of_valid_guesses <= int(num_of_tries_choosed)) and\
                (letter_guessed.lower()  in secret_word) and\
                (letter_guessed.lower() not in old_letters_guessed):

            old_letters_guessed.append( letter_guessed )

            print( ':( ' )
            print( '\n' )
            if number_of_valid_guesses == 1:
                picture = get_hangman_status( 1 )
                print( picture )
            else:
                picture = get_hangman_status( number_of_valid_guesses  )
                print( picture )
            fill_letter_to_guessed_word()
            print('\n')
            print( ''.join( guessed_word ) )

            if check_win() == True:
                print("WIN")
                return True
            return True


        if (check_win() == True) and \
                (number_of_valid_guesses <= int( num_of_tries_choosed )):
            print( ':( ' )
            print( '\n' )

            if number_of_valid_guesses == 1:
                picture = get_hangman_status( 1  )
                print( picture )
            else:
                picture = get_hangman_status( number_of_valid_guesses-1 )
                print( picture )
            print( "WIN\n" )
            print( ''.join( guessed_word ) )

            return  True


        if letter_guessed.lower() not in old_letters_guessed:
            old_letters_guessed.append( letter_guessed )

            return False

 #-------------------------------------------------------------------------------
    def choose_word(file_path, index):
        '''This function accepts a path of a file and a place index in file
        it returns the word in place of index given.
        :param file_path the path to source  file
        :param index of  a secret word  in the file
        :return  secret word'''

        f = open( file_path, 'r' )
        file_contents = f.read()

        # find_word
        # index given, begin from 1 not from 0

        notFound = True

        splitted = file_contents.split()

        while notFound:
            if index == 0:
                word = splitted[ index ]
                notFound = False
            elif notFound and index <= len( splitted ) - 1:
                word = splitted[ index - 1 ]
                notFound = False
            else:
                index = index - len( splitted ) - 1
        f.close()
        return word

# ---------------------------------------------------------------------------------------
    def check_file_exsistment(file1):
        '''This function checks validity of path, if file exists, returns Boolean True.
        :param path for file
        :return  Boolean value of True if it exsists False if it is not exsists'''

        try:
            f=open(file1,'r')
            f.close
            return True
        except IOError:
            print('File not found, try again')
            return False


#-------------------------------------------------------------------

    def check_valid_number(num):
        '''This function checks if the given parameter is a number.
         :param num is the input given for check
         :return  True if the input is a number and False if it is not a number'''
        val = 0
        try:
            val = int( num )
            if val < 0 or val > 999999999:
                raise RuntimeError( "value is either to samall or to big" )
            else:
                return True
        except RuntimeError as e:
            print( e )
            return False
        except ValueError:
            try:
                float( num )
                print( "Input is an float number." )
                return False
            except ValueError:
                print( "This is not a number. Please enter a valid number" )
                return False
            except RuntimeError as e:
                print( e )
            return False


# ---------------------------------------------------------------------------------------

    def get_hangman_status(num):
        '''This function prints the states of a hangman depending on the user's guess try.
        :param num_of_tries an input from player
        :return  the printed status of hangman'''

        num = int( num )
        pic0 = (
'''
x-------x''')
        HANGMAN_PHOTOS[ 1 ] = pic0

        pic1 = (
'''
x-------x
|
|
|
|
| ''')
        HANGMAN_PHOTOS[ 2 ] = pic1

        pic2 = (
'''
x-------x
|       |
|       0
|
|
| ''')
        HANGMAN_PHOTOS[ 3 ] = pic2

        pic3 = (
'''
x-------x
|       |
|       0
|       |
|
| ''')
        HANGMAN_PHOTOS[ 4 ] = pic3

        pic4 = (
'''
x-------x
|       |
|       0
|      /|\\    
|
|''')
        HANGMAN_PHOTOS[ 5 ] = pic4

        pic5 = (
'''
x-------x
|       |
|       0
|      /|\\
|      /
|''')
        HANGMAN_PHOTOS[ 6 ] = pic5

        pic6 = (
'''
x-------x
|       |
|       0
|      /|\\
|      / \\
|''')

        HANGMAN_PHOTOS[ 7 ] = pic6
        HANGMAN_PHOTOS[ 8 ] = " "
        HANGMAN_PHOTOS[ 9 ] = " "

        return HANGMAN_PHOTOS[ num ]

    #--------------------------------------
#       This is the main game flow
#--------------------------------------
#   step #1
#   welcoming the user
    name = input( "What is your name? \n" )
    print( "Hello, " + name, ", time to play hangman!" )


#    print the logo of the game
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
    result = get_hangman_status( start )
    print( result, '\n\n' )

    # ***************************************************

    #step #2
    while True:

        file_name =input("Enter path to the file where secret words are? ")
#         needed for running program in my station at home
        #path = "C:\\Users\\Carmi House\\PycharmProjects\\firstOne\\numpyPandaTutorial"
        #file_name = path + "\\" + file_name
        #
        result = check_file_exsistment( file_name )
        if result == True:
            print('\n')
            break

# ***************************************************

    # step #3

    while True:
        num_of_tries_choosed = input( 'Choose number of tries...' )
        if check_valid_number( num_of_tries_choosed ) == True and int( num_of_tries_choosed ) <=MAX_TRIES :
            print( '\n' )
            break

# ***************************************************
    # step #4
    # here we set the secret word and number of tries for game
    while True:
        position = input( 'Where is the position of secret word in the file?...')
        if check_valid_number( position ) == True :
            print( '\n' )
            break

    secret_word = choose_word( file_name, int(position ))

#****************************************************************************


    #step 5  initialize the gueesed word
    guessed_word = len( secret_word ) *  ['_']
    guessed_word_toScreen =   len( secret_word ) *  '_'
    print(guessed_word_toScreen)

#****************************************************************************


#    step #6  guessing process
    while True:
        if    number_of_valid_guesses < int(num_of_tries_choosed):
            letter_guessed = input( "Guess a letter: " )


            if (check_valid_input( letter_guessed) == True) and \
                    (letter_guessed.__len__() == 1) and\
                    (letter_guessed.lower() not in old_letters_guessed) :

                number_of_valid_guesses += 1

                try_update_letter_guessed( number_of_valid_guesses, letter_guessed )

                if letter_guessed.lower() in secret_word :
                    number_of_valid_guesses -= 1
                
                if check_win()==True :
                    break
                if number_of_valid_guesses==int(num_of_tries_choosed):
                    break


if __name__ == '__main__':
    main()
