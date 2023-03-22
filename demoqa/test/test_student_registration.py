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
    registration_page.fill_address("Moscowskaya Street 18")
    registration_page.fill_date_of_birth('1999', 'May', '11')
    registration_page.fill_state("NCR")
    registration_page.fill_city("Delhi")
    registration_page.click_submit()