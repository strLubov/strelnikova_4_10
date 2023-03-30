from demoqa.model.pages.registration_page import RegistrationPage
from demoqa.data.students import Student

student = Student(first_name='Иван', last_name='Свиридов', user_email='IvanSviridov@gmail.com', gender='Male',
                  user_number='1234567891',
                  subjects='Computer Science', hobbies='Reading', address='Moscowskaya Street 18',
                  photo='/resources/foto.jpg',
                  day_of_birth='11', month_of_birth='May', year_of_birth='1999', state='NCR', city='Delhi')


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.registration_student(student)
    registration_page.should_registered_user_with(
        'Иван Свиридов',
        'IvanSviridov@gmail.com',
        'Male',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi',
    )
