class ProgrammingLanguage:

    def __init__(self, name, Typing, Reflection, Year):
        self.name = name
        self.Typing = Typing
        self.Reflection = Reflection
        self.Year = Year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.Typing, self.Reflection,
                                                                           self.Year)

    def is_dynamic(self):
        if self.Typing == "Dynamic":
            return True
