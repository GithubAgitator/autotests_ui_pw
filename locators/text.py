from locators.base_elements import BaseElement

class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"