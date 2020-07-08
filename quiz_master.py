# %% Importing modules
import numpy as np

import function_generators as fg


# %% Defining functions
def get_function_list(question_types_ordered):
    """ Returns list of functions orders according to question_type_ordered. """
    function_list = np.emtpy(len(question_types_ordered))
    for index, question_type in question_types_ordered:
        function_list[index] = fg.get_function(question_type)
    return function_list


# %% Defining classes
class QuizMaster:
    def __init__(self, init_prob_dist, question_types_ordered):
        self.prob_dist = init_prob_dist  # use non-normalized distribution
        self.function_list = get_function_list(question_types_ordered)

    def draw_function(self):
        norm_prob_dist = self.prob_dist / np.sum(self.prob_dist)
        drawn_function = np.random.choice(self.function_list, p=norm_prob_dist)
        return drawn_function

    def update_prob_dist(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass
