from mycroft import MycroftSkill, intent_file_handler


class DominosPizza(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pizza.dominos.intent')
    def handle_pizza_dominos(self, message):
        self.speak_dialog('pizza.dominos')


def create_skill():
    return DominosPizza()

