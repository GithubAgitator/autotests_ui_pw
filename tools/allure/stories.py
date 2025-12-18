from enum import Enum

class AllureStories(str, Enum):
    REGISTER = "Register"
    LOGIN = "Login"
    COURSER = "Courser"
    DASBOARD = "Dasboard"