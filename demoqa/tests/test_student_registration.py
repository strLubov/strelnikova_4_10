from demoqa.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name("Иван")
    registration_page.fill_last_name("Свиридов")
    registration_page.fill_user_email("IvanSviridov@gmail.com")
    registration_page.fill_user_number("1234567891")
    registration_page.fill_user_gender("Male")
    registration_page.fill_subjects("Computer Science")
    registration_page.fill_hobbies("Reading")
    registration_page.fill_address("Moscowskaya Street 18")
    registration_page.fill_date_of_birth('1999', 'May', '11')
    registration_page.fill_state("NCR")
    registration_page.fill_city("Delhi")
    registration_page.upload_photo('/resources/foto.jpg')
    registration_page.click_submit()

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