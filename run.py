from sample_input import QUESTIONS_DETAILS
from sample_input import TOTAL_MARKS
from sample_input import MARKS_DISTRIBUTION
from sample_input import TOTAL_NUMBER_OF_QUESTION
from question_paper import QuestionBook
from question_paper import QuestionPaper


def get_inputs():
    # register questions and its details
    question_book = QuestionBook.get_instance()
    question_paper = QuestionPaper().get_instance()
    question_book.register_questions(QUESTIONS_DETAILS)
    question_paper.set_question_paper_attr(
        TOTAL_MARKS, TOTAL_NUMBER_OF_QUESTION, MARKS_DISTRIBUTION)


def main():
    get_inputs()
    question_paper = QuestionPaper.get_instance()
    question_paper.generate_question_paper()


if __name__ == "__main__":
    main()
