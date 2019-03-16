##Author Raghvendra Acharya
##Date 2019-03-16

A Question Paper Ganerator Based On Marks Distribution And Difficulty Level 

Description

A Python based question Paper generator which takes input as question details, marks difficulty wise marks distribution.

Assumptions
	1. For given marks distribution it guaranteed that there must be a solution.


Setup:
	
	Setup tested on Windows and Ubuntu 18.04(Work fine for all version).
	
	1. Install python2.7.

	2. Unzip project contents
       $  unzip question_paper_generator.zip
  
    3. Change directory to the newly created project directory
       $  cd question_paper_generator
    
    4. Set PYTHONPATH to enable importing local modules
       $ export PYTHONPATH=$PWD
    
    5. Set Custom Inputs in sample_input.py file.
        QUESTIONS_DETAILS = [["QUESTION_NAME","DIFFICULTY_TYPE_ID","MARKS"]]
        DIFFICULTY_TYPE_ID = {1: "EASY", 2: "MEDIUM", 3: "HARD"}
        MARKS_DISTRIBUTION = {"DIFFICULTY_TYPE_ID":"DISTRIBUTION_IN_PERCENTAGE"}


Run:
	
	1. Run run.py file

Sample Output:

QuestionId      QuestionName    Marks           Difficulty
2               Q2              2               EASY
5               Q5              3               EASY
7               Q7              3               MEDIUM
3               Q3              2               MEDIUM
9               Q9              5               MEDIUM
10              Q10             5               HARD