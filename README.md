# Python Colors Quiz #

## Purpose of the project ##
The Python Colors Quiz is for anyone curious about unusual shades of colors that we all know and recognize. The quiz can be used for educational as well as recreational purposes. To introduce a competitive element, the quiz counts the player's score and displays the final score at the end.

The purpose of this project is to use HTML, CSS and JavaScript to create a website with interactive elements, in this case a quiz game. The website is responsive on mobile, computer and tablet size screens.

![SCREENSHOT OF RESPONSIVE SCREENS](media/screenshot-responsive.png)

## How to play ##
The player begins by entering their name and receiving written instructions on how to play the quiz. Upon pressing Enter, the quiz commences.

The quiz contains multiple choice questions with four answer options per question. The player can choose one answer only, and receives one point for each correct answer. 

When the player submits an answer by typing 1-4 into the terminal, they can see if their choice was correct. If it was correct, they receive a confirmation and 1 point to their score. If their answer was incorrect, they do not receive any points and can see in print which choice was the correct answer. The player then needs to press Enter again to continue to the next question.

When all questions have been answered, the player is congratulated and informed of their final score.

## Features ##

__Header__
-	X

__Input validation and checking error__
-	Player must enter a valid choice, a number between 1-4.
-   If any other characters are entered, the game asks the player to re-enter their answer as it is invalid.


![SCREENSHOT OF QUIZ INTERFACE WITH ANSWER OPTIONS](media/screenshot-quiz-options.png)

- Once the Submit button has been clicked, the user is no longer able to change the answer, as the buttons are disabled. The correct answer option is shown in green. If the user's answer choice was incorrect, it will be shown in red.
- There is also a message below the questions alerting the user when an answer is correct or incorrect, and instructing the user to click Next.
- The score counter below increments with 1 when the submitted answer is correct.
- Clicking the Submit button also displays the Next button, giving the user the opportunity to re-read the question and their answers before moving on to the next question. This is also for educational purposes.

![SCREENSHOT OF SUBMITTED INCORRECT ANSWER](media/screenshot-answer-wrong.png)

- The image below shows what the quiz interface looks like when a user answers a question correctly.

![SCREENSHOT OF SUBMITTED CORRECT ANSWER](media/screenshot-answer-correct.png)

__Final Result__

- When all questions have been answered, an encouraging message is displayed along with the user's final score.

![SCREENSHOT OF QUiZ END](media/screenshot-quiz-end.png)

## Future features ##

- Both questions and answer options could be randomized to increase difficulty.
- A larger library of questions and answers could be added to create a quiz with variation.

## Technology ##
- [GitPod](https://gitpod.io/) was used to write, edit and commit the code, while [GitHub](https://github.com/) was used for deployment, storage and version control.
- [Am I Responsive](https://ui.dev/amiresponsive) was used to create screenshot of website on different screen sizes.

## Testing ##

### Code validation ###
- No errors were returned when passing the Python code through the [PEP8 Python Validator](https://pep8ci.herokuapp.com/)

![SCREENSHOT OF PYTHON VALIDATION](media/html-validation.png)

### Manual testing ###
I have manually tested this project by doing the following:
- Run the code through pylint using the terminal and received a rating of 10/10.
- Entered invalid inputs as question answers (pressing Enter without any input, entering invalid numerals, entering letters and entering empty space) several times over.
- Used PEP8 Python validator and returned the code with no errors.
- Tested the code in my local terminal as well as the Heroku terminal.

### Test cases ###

#### Quiz Introduction ####

- Testing performed: enter my name and press Enter.

- Expected outcome: displays welcome message with instructions on how to play the quiz, and a prompt to press Enter to start.

- Result: as expected.

- Test passed.

#### Quiz Start ####

- Testing performed: press Enter after the introduction to start the quiz.

- Expected outcome: display first question along with 4 answer options. Display instruction on how to answer the question.

- Result: as expected.

- Test passed.

#### Answer question correctly ####

- Testing performed: entering a valid number when answering a question (1-4).

- Expected outcome: See if my answer is correct, display the correct option, and my score.

- Result: as expected.

- Test passed.

#### Answer question incorrectly ####

- Testing performed: entering a invalid character (letter S) when answering a question.

- Expected outcome: alert message prompting me to re-enter a valid answer option.

- Result: as expected.

- Test passed.

#### End of quiz ####

- Testing performed: answer all questions.

- Expected outcome: display message showing final score.

- Result: as expected.

- Test passed.

### Fixed bugs ###

- In the early developent of the game, I tried a number of different lists and dictionaries to store my questions and answers. The first one shown below has the question as the key and the answer options in a list as the value. This proved to be a rudimentary model as there was no sustainable way to index the questions.

```
QUESTIONS = {
    "Aureolin is a shade of what color?": [
        "Yellow", "Green", "Red", "Orange"
    ],
```
- This was followed by a more sophisticated model shown below. The model proved to be too complex for me to work with at this stage as there were numerous syntax errors in GitPod.

```
OptionItem: {
option_id: int,
optionText: ”string”, 
}

QuestionItem: {
question: ”string"
option: [OptionItem]
correctOption: int,
}

QuestionList: [QuestionItem]
```

## Deployment ##

### Via GitPod ###
The GitHub repository was created using the Code Institute GitPod template:
https://github.com/Code-Institute-Org/gitpod-full-template
- Click the link to get to the template. Click “Use this template”.
- Enter repository name, QuizProject, make the repository is public and click “Create repository from template”.
- Click the green GitPod button, wait a moment for the workspace to open. All work was committed in GitPod.

- The repository can be accessed through following link: https://github.com/robinozer/QuizProject.git 

### Via GitHub Pages ###
Github Pages was used to deploy the website. The following steps were used:
- In GitHub, navigate to the repository and find the Settings tab at the top menu.
- Click on Pages in the left hand Menu.
- In “Build and deployment”, go to Branch, select main, and save.
- Wait a moment and refresh the page to find a box with the live URL. The website is now deployed.

## Credits ##
No content was borrowed in building this project.






## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.
