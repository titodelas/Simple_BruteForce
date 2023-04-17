# Password Guesser

This Python program uses a brute force approach to try to guess a password that is provided to it.

## How it works

The program generates all possible combinations of characters, starting from a length of 1 and gradually increasing up to a predefined maximum length. It then compares each of these combinations with the provided password and stops searching when it finds a match.

If the program guesses the password, it will display the password and the total elapsed time. If it is unable to guess the password, it will display the number of failed attempts and the total elapsed time.

## How to use

To use the program, follow these steps:

1.  Clone or download the repository to your computer.
2.  Open the `password_guesser.py` file in your favorite Python editor.
3.  Run the program from your editor or from the Python command line.
4.  When prompted, enter the password you wish to guess.
5.  Wait for the program to finish running.

## Limitations

It's important to note that this program uses a brute force approach to guess passwords and may therefore be inefficient and impractical in some cases. The program's effectiveness will depend on the complexity of the password and the maximum length allowed to be tested.

Additionally, please note that this program is provided for educational purposes only and should not be used to guess other users' passwords without their consent.