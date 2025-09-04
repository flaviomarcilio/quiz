import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_question_with_valid_title():
    question = Question(title='Questão 1')

    assert question.title == 'Questão 1'

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)

def test_valid_choice_remotion():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    question.remove_choice_by_id(1)

    assert len(question.choices) == 2

def test_invalid_choice_remotion():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    with pytest.raises(Exception):
        question.remove_choice_by_id(4)

def test_all_choices_remotion():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    question.remove_all_choices()

    assert len(question.choices) == 0

def test_correct_selection():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    correct_selection = question.correct_selected_choices([2])

    assert len(correct_selection) == 1

def test_incorrect_selection():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    correct_selection = question.correct_selected_choices([1])

    assert len(correct_selection) == 0

def test_more_than_maximum_allowed_selections():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    with pytest.raises(Exception):
        correct_selection = question.correct_selected_choices([1, 2])

def test_set_correct_choice():
    question = Question(title='q1', max_selections=2)
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    question.set_correct_choices([1])
    correct_selection = question.correct_selected_choices([1, 2])

    assert len(correct_selection) == 2

def test_set_invalid_choices():
    question = Question(title='q1', max_selections=2)
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    with pytest.raises(Exception):
        question.set_correct_choices([4])
