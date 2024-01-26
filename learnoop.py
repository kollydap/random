class Button:
    def __init__(self, color: str, length: float, heigth: float) -> None:
        self.color = color
        self.heigth = heigth
        self.length = length

    def change_color(self, color: str = None):
        if color == None:
            self.color = "Blue"
        else:
            self.color = color


class SubmitButton(Button):
    def __init__(
        self,
        color: str,
        length: float,
        heigth: float,
        link: str,
    ) -> None:
        self.link = link
        super().__init__(color, length, heigth)

    def submit(self, link: str = None):
        if link == None:
            # print(f"submitting to {self.link}")
            return link, False

        else:
            print(f"submitting to {link}")
            return link, True


s1 = SubmitButton(color="Brown", length=40, heigth=90, link="www.google.com")

v, y = s1.submit()
if y:
    print(v)
