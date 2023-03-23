from selene import have, command
from selene.support.shared import browser

import os


class RegistrationPage:
    def __init__(self):
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

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_user_email(self, value):
        self.user_email.type(value)
        return self

    def fill_user_number(self, value):
        self.user_number.type(value)
        return self

    def fill_user_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()
        return self

    def fill_subjects(self, value):
        self.subjects.type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        self.hobbies.element_by(have.exact_text(value)).click()
        return self

    def fill_address(self, value):
        self.address.type(value)
        return self

    def upload_photo(self, value):
        self.photo.send_keys(os.getcwd() + value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.month_of_birth.type(month)
        self.year_of_birth.type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self


    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.list_state.element_by(have.exact_text(name)).click()
        return self

    def fill_city(self, name):
        self.city.click()
        self.list_city.element_by(
            have.exact_text(name)
        ).click()
        return self

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def click_submit(self):
        self.submit.perform(command.js.click)
        return self

    def should_registered_user_with(self, full_name, email, gender, number, dateofbirth, subjects, hobbies, photo, address, stateandcity):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                '1234567891',
                '11 May,1999',
                'Computer Science',
                'Reading',
                'foto.jpg',
                'Moscowskaya Street 18',
                'NCR Delhi',
            )
        )
        return self