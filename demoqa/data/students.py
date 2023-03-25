from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    user_email: str
    gender: str
    user_number: str
    subjects: str
    hobbies: str
    address: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    state: str
    city: str
    photo: str
