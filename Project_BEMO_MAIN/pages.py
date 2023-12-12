from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(self):
    return {
        # 'p_hi': "{0:.1f}".format(Constants.probability) + "%",
        # 'p_lo': "{0:.1f}".format(100 - Constants.probability) + "%",
        'p_hi': "{0:.0f}".format(Constants.probability) + "%",
        'p_lo': "{0:.0f}".format(100 - Constants.probability) + "%",
        'hi':   "{0:.0f}".format(Constants.lottery_hi),
        'lo':   "{0:.0f}".format(Constants.lottery_lo),
        'part_index': self.participant.vars['part_index'],
        'currency': Constants.currency
    }


# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #
class Instructions(Page):

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return dict(
            today=Constants.today,
            in_12_months=Constants.in_12_months
        )


# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # only display if previous choice was not "indifferent"
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        previous_choices = [p.choice for p in self.player.in_previous_rounds()]
        return 'I' not in previous_choices

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['choice']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_choices
        page = self.subsession.round_number
        progress = page / total * 100
        print("{0:.0f}".format(self.participant.vars['icl_time_sure_payoffs'][page - 1]))
        print(type(self.participant.vars))

        dicti = {'0':['$100 with probability 10%', '$50 with probability 70% ', '$20 with probability 20%', '', '$50 with probability 100%', ''], 
                '1':['$100 with probability 30%', '$50 with probability 10% ', '$20 with probability 60%','', '$50 with probability 100%', ''], 
                '2':['$100 with probability 10%', '$50 with probability 70% ', '$20 with probability 20%', '$100 with probability 30%', '$50 with probability 10%', '$20 with probability 60%'], 
                '3':['$100 with probability 10%', '', '$20 with probability 90%', '', '$50 with probability 30%', '$20 with probability 70%'], 
                '4':['$100 with probability 70%', '$50 with probability 30% ', '', '$100 with probability 80%', '','$20 with probability 20%'], 
                
                
                }

        return {
            'page':        page,
            'total':       total,
            'progres':    progress,
            # 'sure_payoff': "{0:.0f}".format(self.participant.vars['icl_time_sure_payoffs'][page - 1])
            #'sure_payoff': "$100 with probability 10% \n $50 with probability 70% \n $20 with probability 20% \n $50 with probability 100%"
            'sure_payoff': 'abc',
            'a_1': dicti[str(page-1)][0],
            'a_2': dicti[str(page-1)][1],
            'a_3': dicti[str(page-1)][2],
            'b_1': dicti[str(page-1)][3],
            'b_2': dicti[str(page-1)][4],
            'b_3': dicti[str(page-1)][5]
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_sure_payoffs()
        self.player.update_switching_row()
        self.player.set_final_switching_row()
        if self.subsession.round_number == Constants.num_choices:
            self.player.update_part_index()


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [Decision]

if Constants.instructions:
    page_sequence.insert(0, Instructions)


