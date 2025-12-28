from locators.base_elements import BaseElement

class Image(BaseElement):
    @property
    def type_of(self) -> str:
        return "image"