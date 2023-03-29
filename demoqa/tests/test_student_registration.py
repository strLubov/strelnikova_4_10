from demoqa.model.pages.registration_page import RegistrationPage
from demoqa.data.students import Student
import allure

student = Student(first_name='Иван', last_name='Свиридов', user_email='IvanSviridov@gmail.com', gender='Male',
                  user_number='1234567891',
                  subjects='Computer Science', hobbies='Reading', address='Moscowskaya Street 18',
                  photo='foto.jpg',
                  day_of_birth='11', month_of_birth='May', year_of_birth='1999', state='NCR', city='Delhi')


@allure.title("Successful fill form")
def test_student_registration_form(setup_browser):
    registration_page = RegistrationPage(setup_browser)
    with allure.step("Open registrations form"):
        registration_page.open()

    with allure.step("Fill form"):
        registration_page.registration_student(student)

    with allure.step("Check form results"):
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
