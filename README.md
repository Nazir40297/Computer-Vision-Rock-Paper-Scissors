# Computer Vision RPS

Firstly, created a GitHub respository for the Rock Paper Scissors game. Then used Teachable-Machine to create a model of images for the rock, paper and scissors signs. These were then downloaded and uploaded to GitHub to use in our code to come. We will use these images to create an interactive game of Rock Paper Scissors where the player plays against the computer using the camera. Each class will represent an action made by the user. Using further dependecies and libraries we will be able to model the game. 

First started off with importing the random module which will be used in the computer choice whereby a random option will be picked by the computer between rock, paper and scissors. Defined our first function called get_computer_choice which randomly picked an option and returns said option. Then a function called get_user_choice was defined which asked the user for input and checks if this input belongs to "rock", "paper" or "scissors". If so, then it returns the user's choice. Then the function to get a winner was created which runs a series of if-elif statements which tells the computer what to print depending on what the corresponding options of the computer and user are.
