# Riddle Me Guessing Game

The purpose of this game it to give the user a set of riddles for them to guess the correct answer which then directs them on to the next riddle.
If the user guesses wrong then their score is reduced by one. The game nds when the user reaches 0 poins or the user finishes the game. The aim for the user is to reach the end of the game 
with the most points. 

## UX

This web application is intended for any user that would like a challange to answer a set of riddles in the most simplistic and clear way, suitable for all users.
The way this is archeved in a simplistic way is, as soon as the webpage is loaded an input box is displayed central with rules on how to play the game displayed in a lighter font compared to the 
background next to a leaderboard that displays session scores once completed.

* A user wanting to play the game for the firts time will siply be able to load the app read the rules and input user name and start the game.

* A user wanting to replay the game once completed they are prompted with 2 options to play again or quit and can choose either and view thier score aswell.

## Technologies Used

* [Flask Web Framework](http://flask.pocoo.org/)
    * Allowed me to build the web application also with getting user information through GET and PUSH requests and render templates. 

* [Bootstrap Grayscale Theme]((https://blackrockdigital.github.io/startbootstrap-grayscale/)
    * Used to give the theame of the webpage.

## Testing

### Manual Testing

* Tested to see if to see if the website is responsive on different screen sizes. 

* One of the tests done manually was to ensure the correct session username was displayed on the leaderboard section this was done by 
changing the score value to 1 and maunally using different usernames to end the game. What I found was that the previous session username was being
used and displayed on the leaderboard so the work around this was to end the session before getting the username from the form. Line 25 on file run.py.

* Another test was to make sure that when the user has an empty input box and presses enter no action is taken by adding a required attribute on each input element.

### Automated Testing

By importing unittest into the test_run.py file I managed to create two automated tests linked to the run.py file and the quiz.py file.

* Frist test was to determaine wether the json file that's used in the run.py file will be read and returned using the read_json_file() function, if the length is greater than 0 then we are reading the file sucssesfully. 

* Second test was to check that the answer was equal to the user input using the check_answer() function created in the quiz.py file. 
Througout this test I found that I needed to change the answers in the json file to make sure they had no spaces and all lowercase this 
made it easier to edit the user input making sure it matches the answer regardless if the user uses spaces between words or capitalization. 

## Deployment

To deploy the website from Cloud 9 workspace to Github pages I used the following commands in sequence.

    * git init - which creates a new Git repository.
    * git status - to see which files have been updated on Cloud 9.
    * git add - to add the updated files to the staging area.
    * git commit -m "actions taken" - to commit the files to the local repository.
    * git remote add origin https://github.com/Harrysibbenga/riddlegame.git - specifies which remote repository commants will be used in.
    * git push -u origin master - to push the commits made on local branch to the Github remote repository.
    
Once that was done it was simple to publish the website on the settings in the repository, by selecting the master branch as the source for Github Pages.

Published at : https://harrysibbenga.github.io/riddlegame/

The webpage was also published on Heroku through Cloud 9 workspace using the following command for an exisiting git repository.
    
    * heroku git:remote -a riddle-me-guessing-game

Before it was published I needed to create a Procfile commit and push it also changed the Config Vars in heroku to the following.
    * IP = 0.0.0.0
    * PORT = 5000
    
## Credits

* Uploaded bootstrap theme from [Grayscale](https://blackrockdigital.github.io/startbootstrap-grayscale/)