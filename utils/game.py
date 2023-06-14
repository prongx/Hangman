class Hangman:
    def __init__(self):
        possible_words=['becode', 'learning', 'mathematics', 'sessions']
        word_to_find=["b","e","c","o","d","e"]
        lives=5
        correctly_guessed_letters=[]
        wrongly_guessed_letters=[]
        error_count=0
        turn_count=0

    def play(self):
        """ method that asks the player to enter a letter. 
        Optional: Be careful that the player shouldn't be allowed to type something else than a letter, and not more than a letter. 
        If the player guessed a letter well, add it to the correctly_guessed_letters list. 
        If not, add it to the wrongly_guessed_letters list and add 1 to error_count."""
        input("Give me an input letter")



    def start_game(self):
        """ method that:
        will call play() until the game is over (because the user guessed the word or because of a game over).
        will call game_over() if lives is equal to 0.
        will call well_played() if all the letter are guessed.
        will print correctly_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn. """

    
    def game_over(self):
        # method that will stop the game and print game over....

    def well_played(self):
        # method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!
