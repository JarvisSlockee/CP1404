class ProgrammingLanguage:
    def __init__(self, name="", typing="", year="", reflection=False):
        self.name = name
        self.typing = typing
        self.year = year
        self.reflection = reflection

    def is_dynamic(self):
        return self.typing == "dynamic"

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.year, self.reflection)
