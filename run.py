"""Python Script for running the Colors Quiz.
The question bank below can be moved into a separate file
when the amount of questions increases.
"""
QUESTIONS = [
    {
        'question': "Q1. Aureolin is a shade of what color?",
        'options': "1. Yellow\n2. Green\n3. Red\n4. Orange",
        'correct_option': '1',
        'correct_answer': 'Yellow'
    },
    {
        'question': "Q2. Cerulean is a shade of what color?",
        'options': "1. Brown\n2. Blue\n3. Grey\n4. White",
        'correct_option': '2',
        'correct_answer': 'Blue'
    },
    {
        'question': "Q3 Celadon is a shade of what color?",
        'options': "1. White\n2. Black\n3. Grey\n4. Green",
        'correct_option': '4',
        'correct_answer': 'Green'
    },
    {
        'question': "Q4 Maroon is a shade of what color?",
        'options': "1. Pink\n2. Blue\n3. Red\n4. Yellow",
        'correct_option': '3',
        'correct_answer': 'Red'
    },
    {
        'question': "Q5 Umber is a shade of what color?",
        'options': "1. Yellow\n2. Red\n3. Brown\n4. Orange",
        'correct_option': '3',
        'correct_answer': 'Brown'
    }
]


def introduction():
    """
    Introduces the player to the game and explains the rules
    """
    print(
        'Hi there! Welcome to this Python Quiz.\n'
        'There are five questions in total.\n'
        'Each question has four answer options.\n'
        'You get one point for each correct answer.\n'
        'Good luck!\n'
    )
    input('Press Enter to start the quiz.\n')
    main()  # initializes the quiz


def main():
    """
    Central function:
    Displays questions and answer options from list index.
    Confirms player's choice, and checks whether the answer is correct.
    Increments player's score if correct.
    If incorrect, displays the correct answer to the player.
    Moves on to the next question.
    Displays final score at the end of game.
    """
    score = 0
    question_index = 0
    while question_index < len(QUESTIONS):
        display_next_question(question_index)
        user_input = get_user_input()
        print(f'You selected option {user_input}')
        is_correct = check_user_answer(question_index, user_input)
        if is_correct:
            score += 1
            display_answer_value(question_index)
        else:
            display_correct_answer(question_index)
        print(f'Your score is: {score}\n')
        input('Press Enter to continue\n')
        question_index += 1
    print('Quiz ended. Well done! Your final score is: ' + str(score))


def get_user_input():
    """
    Receives and validates user input for answering questions.
    """
    is_user_input_invalid = True
    while is_user_input_invalid:
        user_input = input('Please enter a value between 1-4\n')
        if user_input in ['1', '2', '3', '4']:
            return user_input
        print('Invalid option, please re-enter')


def check_user_answer(question_index, user_selection):
    """
    Returns a boolean: true if the player's option is the same as
    the correct answer, and false if it isn't
    """
    question = QUESTIONS[question_index]
    return question['correct_option'] == user_selection


def display_next_question(question_index):
    """
    Retrieves the subsequent question from the list and prints it out.
    """
    question = QUESTIONS[question_index]
    print(question['question'])
    print(question['options'])


def display_correct_answer(question_index):
    """
    Alerts player of wrong answer,
    and prints out the correct answer.
    """
    question = QUESTIONS[question_index]
    correct_answer_value = question['correct_answer']
    correct_answer_option = question['correct_option']
    print(f'Oops, that is wrong. '
          f'The correct answer is option'
          f' {correct_answer_option}, {correct_answer_value}.')


def display_answer_value(question_index):
    """
    When player chooses right answer, the answer is printed out.
    e.g. Option 1 Brown is correct.
    """
    question = QUESTIONS[question_index]
    correct_answer_option = question['correct_option']
    correct_answer_value = question['correct_answer']
    print(f'Option {correct_answer_option}, '
          f'{correct_answer_value} is correct. Awesome!')


if __name__ == '__main__':
    introduction()
