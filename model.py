import re
import tkinter as tk
from tkinter import ttk


class Model:
    def __init__(self, first_name, email):
        self.email = email
        self.first_name = first_name

    @property
    def email(self):
        return self.__email

    @property
    def first_name(self):
        return self.__first_name

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('data.txt', 'a') as f:
            f.write(self.email + '\n' + self.first_name)
