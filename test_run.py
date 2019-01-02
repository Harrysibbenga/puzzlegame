import unittest
import quiz
import run

class test_run(unittest.TestCase):
    ''' run.py test suit '''
    
    def test_can_read_a_json_file(self):
        '''
        test that the 'read_json_file' function reads a json filename and returns it into a list with a length greater than 0
        '''
        riddle_data = run.read_json_file('data/text.json')
        self.assertGreater(len(riddle_data), 0)
        
    def test_check_answer(self):
        ''' 
        test that the user input is equal to the answers in the riddle data by importing the quiz file and doing the following tests 
        to check if they pass.
        
        check_answer(riddle_answer, "turkey")
        check_answer(riddle_answer, "Turkey")
        check_answer(riddle_answer, "TURKEY")
        check_answer(riddle_answer, "   Turkey   ")
        check_answer(riddle_answer, "yesterday, today, tomorrow")
        check_answer(riddle_answer, "yesterday,   today,    tomorrow")
        '''
        riddle = {0: "What kind of key do you use on Thanksgiving?", 1: "turkey"}
        riddle2 = {0: "Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?", 1:"yesterday,today,tomorrow"}
        
        result = quiz.check_answer(riddle2[1], "yesterday,   today,    tomorrow")
        assert result
        