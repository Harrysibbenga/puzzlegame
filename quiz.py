def check_answer(question_answer, user_answer):
    user_answer = user_answer.lower().strip().replace(" ", "")
    if question_answer == user_answer:
        return True
    else: 
        return False