# %% Importing modules
import numpy as np
import sympy as sym

import function_generators as fg


# %% Defining functions
def get_function_dict(question_types_ordered):
    """ Returns list of functions orders according to question_type_ordered. """
    function_dict = {}
    for question_type in question_types_ordered:
        function_dict[question_type] = fg.get_function(question_type)
    return function_dict


# %% Defining classes
class QuizMaster:
    def __init__(self, init_prob_dist, question_types_ordered):
        self.prob_dist = init_prob_dist  # use non-normalized distribution
        self.qto = question_types_ordered
        self.scores = {qt: [0, 0] for qt in question_types_ordered}
        self.function_dict = get_function_dict(question_types_ordered)
        self.n_functions = len(self.function_dict)

    def draw_function(self):
        norm_prob_dist = self.prob_dist / np.sum(self.prob_dist)
        drawn_qt = np.random.choice(self.qto, p=norm_prob_dist)
        return self.function_dict[drawn_qt], drawn_qt

    def update_prob_dist(self, question_type, result: bool):
        pass

    def start(self):
        while True:
            function, drawn_qt = self.draw_function()
            answer = sym.diff(function)

            user_answer = input("Wat is de afgeleide van {}?".format(function))
            self.scores[drawn_qt][1] += 1
            user_answer_parsed = sym.parsing.parse_expr(user_answer)

            if user_answer_parsed == answer:
                print("Goed geantwoord!")
                self.update_prob_dist(question_type=drawn_qt, result=True)
                self.scores[drawn_qt][0] += 1

            else:
                print("Helaas, dat antwoord is fout, het moest zijn {}.".format(answer))
                self.update_prob_dist(question_type=drawn_qt, result=False)

    def stop(self):
        pass
