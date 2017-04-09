#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


class Diary(object):
    def __init__(self):
        self.list_of_students = []

    def add_list_of_students(self, list_of_students):
        self.list_of_students += list_of_students

    def add_student(self, student):
        self.list_of_students.append(student)

    def get_students_total_average_score(self):
        result = []
        for element in self.list_of_students:
            for student in element:
                score = 0
                number_of_scores = 0
                for classes in element[student]:
                    for scores in classes:
                        score += sum(classes[scores]["Score"])
                        number_of_scores += len(classes[scores]["Score"])
                result.append({student : float(score)/float(number_of_scores)})

        return result

    def get_students_average_score_from_selected_class(self, name):
        result = []
        for element in self.list_of_students:
            for student in element:
                score = 0
                number_of_scores = 0
                for classes in element[student]:
                    # print classes
                    for scores in classes:
                        if scores == name:
                            score += sum(classes[scores]["Score"])
                            number_of_scores += len(classes[scores]["Score"])
                result.append({student: float(score) / float(number_of_scores)})

        return result

    def count_total_attendance_of_student(self):
        result = []
        for element in self.list_of_students:
            for student in element:
                attendance = 0
                number_of_scores = 0
                for classes in element[student]:
                    for scores in classes:
                        attendance += classes[scores]["Attendance"]
                result.append({student: attendance})
        return result

if __name__ == "__main__":
    list_of_students = [
        {"Ala Makota":
            [
                {"Math":
                    {
                        "Attendance": 5,
                        "Score": [2, 3, 4, 5]
                    }
                },
                {"Physics":
                    {
                        "Attendance": 4,
                        "Score": [5, 4, 5, 2]
                    }
                },
                {"Biology":
                    {
                        "Attendance": 5,
                        "Score": [2, 4, 3, 2]
                    }
                }
            ]
        },

        {"Ola Makota":
            [
                {"Math":
                    {
                        "Attendance": 3,
                        "Score": [5, 6, 4, 5]
                    }
                },
                {"Physics":
                    {
                        "Attendance": 4,
                        "Score": [2, 3, 5, 2]
                    }
                },
                {"Biology":
                    {
                        "Attendance": 3,
                        "Score": [4, 5, 3, 2]
                    }
                }
            ]
        },
        {"Jan Kowalski":
            [
                {"Math":
                    {
                        "Attendance": 7,
                        "Score": [4, 2, 4, 3]
                    }
                },
                {"Physics":
                    {
                        "Attendance": 4,
                        "Score": [3, 4, 2, 3]
                    }
                },
                {"Biology":
                    {
                        "Attendance": 5,
                        "Score": [5, 3, 2, 5]
                    }
                }
            ]
        },
    ]

    diary = Diary()
    diary.add_list_of_students(list_of_students)
    print diary.get_students_total_average_score()
    print diary.get_students_average_score_from_selected_class("Math")
    print diary.count_total_attendance_of_student()