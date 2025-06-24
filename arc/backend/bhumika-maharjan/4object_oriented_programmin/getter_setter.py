class Label:
    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

label = Label("Fruits")
label.get_text()
label.set_text("Vegetables")
label.get_text()


