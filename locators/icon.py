from locators.base_elements import BaseElement

class Icon(BaseElement):
    @property
    def type_of(self) -> str:
        return "icon"
