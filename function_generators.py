# %% Importing modules
import numpy as np
import sympy as sym

# %% Declaring static variables
x = sym.Symbol('x')


# %% Defining functions
def get_function(question_type):
    if question_type == 'enkel_nat_macht':
        return single_natural_power()
    elif question_type == 'meer_nat_macht':
        return mult_natural_power()
    elif question_type == 'meer_reeel_macht':
        return mult_real_power()
    elif question_type == 'prod_regel_machtreeks':
        return prod_power_series()
    elif question_type == 'prod_regel_wortel':
        return prod_sqrt()
    elif question_type == 'quotient_regel_macht':
        return quot_power_series()
    elif question_type == 'quotient_regel_ketting':
        return quot_chain()
    else:
        print("Functie type {} bestaat niet.".format(question_type))
        return None


def single_natural_power():
    power = np.random.randint(1, 10)
    return x ** power


def mult_natural_power():
    n_terms = np.random.randint(1, 5)
    pm_list = np.random.choice([-1, +1], size=n_terms, p=[0.3, 0.7])
    power_list = np.sort(np.random.choice(range(1, 10), size=n_terms, replace=False))[::-1]

    func = 0
    for i in range(n_terms):
        func += pm_list[i] * x ** power_list[i]

    return func


def mult_real_power():
    n_terms = np.random.randint(1, 5)
    pm_list = np.random.choice([-1, +1], size=n_terms, p=[0.3, 0.7])
    power_list = np.sort(np.round(np.random.normal(0, scale=2, size=n_terms), 3))[::-1]

    func = 0
    for i in range(n_terms):
        func += pm_list[i] * x ** power_list[i]

    return func


def prod_power_series():
    return


def prod_sqrt():
    return


def quot_power_series():
    return


def quot_chain():
    return
