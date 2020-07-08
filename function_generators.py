# %% Importing modules
import numpy as np


# %% Defining functions
def get_function(question_type):
    if question_type == 'enkel_nat_macht':
        return single_natural_power
    elif question_type == 'meer_nat_macht':
        return mult_natural_power
    elif question_type == 'meer_reeel_macht':
        return mult_real_power
    elif question_type == 'prod_regel_machtreeks':
        return prod_powerseries
    elif question_type == 'prod_regel_wortel':
        return prod_sqrt
    elif question_type == 'quotient_regel_macht':
        return quot_powerseries
    elif question_type == 'quotient_regel_ketting':
        return quot_chain
    else:
        print("Functie type {} bestaat niet.".format(question_type))
        return None

def single_natural_power():
    return

def mult_natural_power():
    return

def mult_real_power():
    return

def prod_powerseries():
    return

def prod_sqrt():
    return

def quot_powerseries():
    return

def quot_chain():
    return
