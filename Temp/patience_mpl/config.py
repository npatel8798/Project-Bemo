# <imports>
from otree.api import Currency as c
from otree.constants import BaseConstants
# </imports>


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Task-specific Settings --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # currency (symbol)
    currency = '€'

    # number of binary choices between "payment today" and "payment in 12 months"
    num_choices = 25

    # include certain choice
    certain_choice = True

    # original list of payments in 12 moths used by Falk et al. (2016)
    original_list = [
        100.00, 103.00, 106.10, 109.20, 112.40,
        115.60, 118.80, 122.10, 125.40, 128.80,
        132.30, 135.70, 139.20, 142.80, 146.40,
        150.10, 153.80, 157.50, 161.30, 165.10,
        169.00, 172.90, 176.90, 180.90, 185.00
        ]

    # Use original list of payments
    # "True" means that the for the payments in 12 months the original list by Falk et al. (2016) will be used.
    # "False" means that the list of payments in 12 months will be created anew,
    # based on the parameter "increment" and "rate" specified below.
    use_original_list = True

    # if the list is to be created anew
    # "payment" denotes the payment today
    # "payment12" denotes the initial payment in 12 months, i.e. at row 1
    # "increment" determines the initial increment in the payment in 12 months (i.e. from row 1 to row 2)
    # "rate" denotes how much the increment changes from row to row

    payment = 100
    payment12 = payment
    increment = 3
    rate = 0.05

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Overall Settings and Appearance --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # Consistency (single switching point)
    # ---------------------------------------------------------------------------------------------------------------
    # Enforce consistency, i.e. only allow for a single switching point
    # if <enforce_consistency = True>, all options "A" above a selected option "A" are automatically selected
    # similarly, all options "B" below a selected option "B" are automatically checked, implying consistent choices
    # note that <enforce_consistency> is only implemented if <one_choice_per_page = False> and <random_order = False>
    enforce_consistency = True

    # Single click
    # if <enforce_consistency = True> and <single_click = True>, when a participant selects option "B" at a certain row,
    # not only all options "B" below the selected option "B" are automatically checked (as in enforce_consistency),
    # but also all options "A" above the selected option "B" are automatically checked.
    # In other words, the participant is required to click only once.
    single_click = True

    # ---------------------------------------------------------------------------------------------------------------

    # show each lottery pair on a separate page
    # if <one_choice_per_page = True>, each single binary choice is shown on a separate page
    # if <one_choice_per_page = False>, all <num_choices> choices are displayed in a table on one page
    one_choice_per_page = False

    # order choices between lottery pairs randomly
    # if <random_order = True>, the ordering of binary decisions is randomized for display
    # if <random_order = False>, binary choices are listed in ascending order of the probability of the "high" outcome
    random_order = False

    # depict probabilities as percentage numbers
    # if <percentage = True>, the probability of outcome "high" will be displayed as percentage number, i.e. "50%"
    # if <percentage = False>, the probabilities will be displayed as fractions, i.e. "1/2" etc.
    percentage = True

    # show small pie charts for each lottery
    # if <small_pies = True>, a pie chart depicting the probabilities of outcomes is rendered next to each lottery
    # if <small_pies = False>, no graphical representation of probabilities is displayed
    small_pies = True

    # display lotteries in terms of large pie charts
    # if <large_pies = True>, lotteries are depicted as pie charts; if <large_pies = False> lotteries are list items
    # note that <large_pies = True> only affects the task's appearance if <one_choice_per_page = True>
    large_pies = True

    # show progress bar
    # if <progress_bar = True> and <one_choice_per_page = True>, a progress bar is rendered
    # if <progress_bar = False>, no information with respect to the advance within the task is displayed
    # the progress bar graphically depicts the advance within the task in terms of how many decision have been made
    # further, information in terms of "page x out of <num_choices>" (with x denoting the current choice) is provided
    progress_bar = True

    # show instructions page
    # if <instructions = True>, a separate template "Instructions.html" is rendered prior to the task
    # if <instructions = False>, the task starts immediately (e.g. in case of printed instructions)
    instructions = True

    # show results page summarizing the task's outcome including payoff information
    # if <results = True>, a separate page containing all relevant information is displayed after finishing the task
    # if <results = False>, the template "Results.html" will not be rendered
    results = False

    # null payoff (if results is false and the task is not incentive compatible)
    null_payoff = 0

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- oTree Settings (Don't Modify) --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    name_in_url = 'patience_mpl'
    players_per_group = None

    if one_choice_per_page:
        if certain_choice:
            num_rounds = num_choices
        else:
            num_rounds = num_choices - 1
    else:
        num_rounds = 1
