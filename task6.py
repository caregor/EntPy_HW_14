"""
    ---Task 6---
📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
📌 Напишите 3-7 тестов pytest для данного проекта.
📌 Используйте фикстуры.
"""
import pytest

from src.error import ErrorLevel
from src.project import Project

@pytest.fixture
def project_instance():
    return Project(file_db='db/test_db.json')

def test_add_new_user_valid_level(project_instance):
    current_user_level = 5
    data_new_user = 'David 555 6'
    result = project_instance.add_new_user(data_new_user, current_user_level)
    assert result == "Пользователь добавлен"

def test_add_new_user_insufficient_level(project_instance):
    current_user_level = 7
    data_new_user = 'Eve 999 6'
    with pytest.raises(ErrorLevel):
        project_instance.add_new_user(data_new_user, current_user_level)

def test_wrong_input_len_data(project_instance):
    current_user_level = 7
    data_new_user = 'Max 444'
    with pytest.raises(ValueError):
        project_instance.add_new_user(data_new_user, current_user_level)

if __name__ == '__main__':
    pytest.main(['-v'])