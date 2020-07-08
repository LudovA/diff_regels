"""
    Dit programma is geschreven door Ludo van Alst naar een idee van Jan Bosma.
    Geinspireerd door Stiching Studiebegeleiding Leiden.

    Tijdens het nakijken in de differentieerstoomcursus 2020-2021 kwam Jan met het idee om een programma te bouwen
    dat automatisch differentieervragen genereert basis van het niveau van de leerling. Dit wilde ik natuurlijk
    direct in praktijk brengen, en zie hier het resultaat/de voortgang.

    Interactie met het script is in het nederlands, code is engelstalig.
"""


# %% Importing modules
import numpy as np
from quiz_master import QuizMaster


# %% Initialize static variables
question_types_ordered = ['enkel_nat_macht',
                          'meer_nat_macht',
                          'meer_reeel_macht',
                          'prod_regel_machtreeks',
                          'prod_regel_wortel',
                          'quotient_regel_macht',
                          'quotient_regel_ketting']
init_prob_dist = np.zeros(len(question_types_ordered))  # non-normalized prob_dist
init_prob_dist[:3] = 100


# %% Main
if __name__ == '__main__':
    quiz_master = QuizMaster(init_prob_dist=init_prob_dist,
                             question_types_ordered=question_types_ordered)

    try:
        quiz_master.start()

    except KeyboardInterrupt:
        print("Programma stopt.")
