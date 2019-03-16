from util import get_weighted_spl_random_numbers_list
from collections import defaultdict
DIFFICULTY_TYPES = {1: "EASY", 2: "MEDIUM", 3: "HARD"}


class Question(object):
    def __init__(self, question_id, question_name, marks, difficulty_level):
        self.id = question_id
        self.name = question_name
        self.marks = marks
        self.difficulty_level = difficulty_level


class QuestionBook(object):
    __instance = None

    @staticmethod
    def get_instance():
        if QuestionBook.__instance is None:
            QuestionBook()
        return QuestionBook.__instance

    def __init__(self):
        if QuestionBook.__instance is not None:
            raise Exception("Use get_instance method to get object!!")
        else:
            self.QUESTIONS_LIST = dict()
            self.difficulty_wise_question = defaultdict(lambda: {})
            self.CURRENT_QUESTION_ID = 1
            QuestionBook.__instance = self

    def register_questions(self, QUESTION_DETAILS):
        if not QUESTION_DETAILS:
            raise ValueError("Input Quetion details can't be empty.!!")
        for question in QUESTION_DETAILS:
            question_id = self.CURRENT_QUESTION_ID
            name = str(question[0])
            difficulty = int(question[1])
            marks = int(question[2])
            obj_question = Question(question_id, name, marks, difficulty)
            self.__register_questions_difficulty_wise(obj_question)
            self.QUESTIONS_LIST[question_id] = obj_question
            self.CURRENT_QUESTION_ID += 1

    def get_questions_list(self):
        return self.QUESTIONS_LIST

    def question_details_by_id(self, question_id):
        return self.QUESTIONS_LIST[question_id]

    def __register_questions_difficulty_wise(self, question):
        self.difficulty_wise_question[question.difficulty_level].update(
            {question.id: question.marks})

    def get_questions_difficulty_wise(self, difficulty):
        return self.difficulty_wise_question[difficulty]


class QuestionPaper(object):
    __instance = None

    @staticmethod
    def get_instance():
        if QuestionPaper.__instance is None:
            return QuestionPaper()
        return QuestionPaper.__instance

    def __init__(self):
        if QuestionPaper.__instance is not None:
            raise Exception("Use get instance method to get instance of this.")
        else:
            self.total_marks = 0
            self.number_of_questions = 0
            self.marks_distribution = dict()
            self.FINAL_QUESTIONS_LIST = list()
            QuestionPaper.__instance = self

    def set_question_paper_attr(self, total_marks, total_question, marks_distribution):
        self.total_marks = total_marks
        self.number_of_questions = total_question
        self.marks_distribution = marks_distribution

    def __add_question_to_paper(self, question):
        self.FINAL_QUESTIONS_LIST.append(question)

    def __get_total_marks(self):
        return self.total_marks

    def __get_marks_distribution(self):
        return self.marks_distribution

    def __total_number_of_question(self):
        return self.total_number_of_question

    def __get_final_question_paper(self):
        return self.FINAL_QUESTIONS_LIST

    def __get_all_questions_list(self):
        question_book = QuestionBook.get_instance()
        marks_distribution = self.__get_marks_distribution()
        total_marks = self.__get_total_marks()
        for difficulty_type_id in DIFFICULTY_TYPES:
            difficulty_level_wise_value = (
                marks_distribution[difficulty_type_id] * total_marks)/100

            questions_list = self.__difficulty_level_wise_question_list(
                difficulty_type_id, difficulty_level_wise_value)
            for question_id in questions_list:
                obj_question = question_book.question_details_by_id(
                    question_id)
                self.__add_question_to_paper(obj_question)
        return self.__get_final_question_paper()

    def __difficulty_level_wise_question_list(self, difficulty_level, max_marks):
        question_book = QuestionBook.get_instance()
        question_details = question_book.get_questions_difficulty_wise(
            difficulty_level)
        questions = get_weighted_spl_random_numbers_list(
            question_details, max_marks)
        return questions

    def __print_question_paper(self, all_questions):
        all_questions = sorted(all_questions, key=lambda l: l.id)
        print "QuestionId\t", "QuestionName\t", "Marks\t\t", "Difficulty"
        for question in all_questions:
            print question.id, "\t\t", question.name, "\t\t", question.marks, "\t\t", DIFFICULTY_TYPES[
                question.difficulty_level]

    def generate_question_paper(self):
        all_questions = self.__get_all_questions_list()
        self.__print_question_paper(all_questions)
