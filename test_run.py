import unittest
import run

class test_run(unittest.TestCase):
    ''' run.py test suit '''
    
    def test_can_read_a_json_file(self):
        '''
        test that the 'read_json_file' function reads a json filename and returns it into a list with a length greater than 0
        '''
        riddle_data = run.read_json_file('data/text.json')
        self.assertGreater(len(riddle_data), 0)
        
    def test_are_the_answers_equal_to_user_input(self):
        ''' 
        test that the user input is equal to the answers in the riddle data.
        '''
        def check_answer(riddle_data, user_answer):
            user_input = user_answer.lower().strip().replace(" ", "")
            assert riddle_data[1] == user_input, "Expected {0}, got {1}".format(riddle_data[1], user_input)
        
        riddle = {0: "What kind of key do you use on Thanksgiving?", 1: "turkey"}
        riddle2 = {0: "Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?", 1:"yesterday,today,tomorrow"}
        
        check_answer(riddle, "turkey")
        check_answer(riddle, "Turkey")
        check_answer(riddle, "TURKEY")
        check_answer(riddle, "   Turkey   ")
        check_answer(riddle2, "yesterday, today, tomorrow")
        check_answer(riddle2, "yesterday,   today,    tomorrow")