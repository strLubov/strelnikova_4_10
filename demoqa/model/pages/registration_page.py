from selene import have, command
from demoqa.data.students import Student
from demoqa import resources
from pathlib import Path
import os


class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.user_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-checkbox')
        self.photo = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.city = browser.element('#city')
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.state = browser.element('#state')
        self.list_state = browser.all('[id^=react-select][id*=option]')
        self.city = browser.element('#city')
        self.list_city = browser.all('[id^=react-select][id*=option]')
        self.submit = browser.element('#submit')

    def _fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def _fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def _fill_user_email(self, value):
        self.user_email.type(value)
        return self

    def _fill_user_number(self, value):
        self.user_number.type(value)
        return self

    def _fill_user_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()
        return self

    def _fill_subjects(self, value):
        self.subjects.type(value).press_enter()
        return self

    def _fill_hobbies(self, value):
        self.hobbies.element_by(have.exact_text(value)).click()
        return self

    def _fill_address(self, value):
        self.address.type(value)
        return self

    def _upload_photo(self, file):
        self.photo.set_value(Path(f'resources/{file}').resolve())
        return self

    def _fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.month_of_birth.type(month)
        self.year_of_birth.type(year)
        self.browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def _fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.list_state.element_by(have.exact_text(name)).click()
        return self

    def _fill_city(self, name):
        self.city.click()
        self.list_city.element_by(
            have.exact_text(name)
        ).click()
        return self

    def open(self):
        self.browser.open('https://demoqa.com/automation-practice-form')
        self.browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        self.browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def click_submit(self):
        self.submit.perform(command.js.click)
        return self

    def registration_student(self, student: Student):
        self._fill_first_name(student.first_name)
        self._fill_last_name(student.last_name)
        self._fill_user_number(student.user_number)
        self._fill_user_gender(student.gender)
        self._fill_user_email(student.user_email)
        self._fill_subjects(student.subjects)
        self._fill_hobbies(student.hobbies)
        self._fill_address(student.address)
        self._upload_photo(student.photo)
        self._fill_date_of_birth(student.year_of_birth, student.month_of_birth, student.day_of_birth)
        self._fill_state(student.state)
        self._fill_city(student.city)
        self.click_submit()
        return self

    def should_registered_user_with(self, full_name, email, gender, number, dateofbirth, subjects, hobbies, photo,
                                    address, stateandcity):
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                dateofbirth,
                subjects,
                hobbies,
                photo,
                address,
                stateandcity,
            )
        )
        return self
