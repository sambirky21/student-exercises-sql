import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first = first
        self.last = last
        self.slack = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first} {self.last} is in {self.cohort}.'

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])


    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First,
                s.Last,
                s.Slack,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student.first} {student.last} is in {student.cohort}.')
            for student in all_students:
                print(student)
            # [print(s) for s in all_students]

reports = StudentExerciseReports()
reports.all_students()

student = Student('Bart', 'Simpson', '@bart', 'c8')
print(f'{student.first} {student.last} is in {student.cohort}.')


# In this chapter, you are going to use the sqlite3 package to connect to your studentexercises.db database and generate data reports that will output to your terminal.

# Display all cohorts.

class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name} is a thing.'

class CohortReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"

    def all_cohorts(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select Id,
                name
            from Cohort
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

reports2 = CohortReports()
reports2.all_cohorts()

# Display all exercises.

class Exercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'Complete {self.name} in {self.language}.'

class ExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"

    def all_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select Id,
                Name,
                Language
            from Exercise
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

reports3 = ExerciseReports()
reports3.all_exercises()

# Display all JavaScript exercises.

class JavascriptExercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'Complete {self.name} in {self.language}, AGAIN.'

class JavascriptExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"

    def javascript_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: JavascriptExercise(
                row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select Id,
                name,
                language
            from Exercise
            where language = "JavaScript"
            """)

            javascript_exercises = db_cursor.fetchall()

            for exercise in javascript_exercises:
                print(exercise)

reports4 = JavascriptExerciseReports()
reports4.javascript_exercises()

# Display all Python exercises.

class PythonExercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'Complete {self.name} in {self.language}, AGAIN.'

class PythonExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"

    def python_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: PythonExercise(
                row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select Id,
                name,
                language
            from Exercise
            where language = "Python"
            """)

            python_exercises = db_cursor.fetchall()

            for exercise in python_exercises:
                print(exercise)

reports5 = PythonExerciseReports()
reports5.python_exercises()

# Display all C# exercises.

class CsharpExercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        if {self.language} == "Python":
            return f'Complete {self.name} in {self.language}, AGAIN.'
        elif {self.language} == "":
            return f'No exercises in this language.'

class CsharpExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"

    def csharp_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: CsharpExercise(
                row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select Id,
                name,
                language
            from Exercise
            where language = "C#"
            """)

            csharp_exercises = db_cursor.fetchall()

            for exercise in csharp_exercises:
                print(exercise)

reports6 = CsharpExerciseReports()
reports6.csharp_exercises()

# Display all students with cohort name.
# The above is printed first

# Display all instructors with cohort name.
class Teacher():

    def __init__(self, first, last, cohort):
        self.first = first
        self.last = last
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first} {self.last} teaches {self.cohort}.'

class TeacherReports():


    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"

    def all_teachers(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Teacher(
                row[1], row[2], row[4])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select p.Id,
                p.First,
                p.Last,
                p.CohortId,
                c.Name
            from Instructor p
            join Cohort c on p.CohortId = c.Id
            order by p.CohortId
            """)

            all_teachers = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student.first} {student.last} is in {student.cohort}.')
            for teacher in all_teachers:
                print(teacher)
            # [print(s) for s in all_students]

reports27 = TeacherReports()
reports27.all_teachers()

# class Assignment():

#     def __init__(self, first, last, name):
#         self.first = first
#         self.last = last
#         self.name = name

#     def __repr__(self):
#         return f'{self.first} {self.last} {self.name}.'

class ExerciseAssignment():

    def __init__(self):
        self.db_path = "/Users/sbirky21/workspace/python/StudentExercises/studentexercises.db"


    def exercises(self):
        exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.First,
                    s.Last
                from Exercise e
                join Assignment se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')
            print(exercises)

assignents = ExerciseAssignment()
assignents.exercises()