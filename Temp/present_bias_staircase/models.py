from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from present_bias_staircase.config import *
import random


author = 'Felix Holzmeister'

doc = """
Staircase risk elicitation task as proposed by Falk et al. (2016), Working Paper.
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    # initiate list of sure payoffs and implied switching row in first round
    # ------------------------------------------------------------------------------------------------------------
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['icl_sure_payoffs'] = [Constants.sure_payoff]
                p.participant.vars['icl_switching_row'] = 2 ** Constants.num_choices

                # create Part index to show in templates' title (i.e., "Part <index>")
                # ------------------------------------------------------------------------------------------------------
                if "p.participant.vars['part_index']" not in globals():
                    p.participant.vars['part_index'] = 1


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    # ----------------------------------------------------------------------------------------------------------------
    #random_draw = models.IntegerField()
    #payoff_relevant = models.StringField()
    sure_payoff = models.FloatField()
    choice = models.StringField()
    switching_row = models.IntegerField()

    #payoff_ecu = models.FloatField()

    # set sure payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_sure_payoffs(self):

        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.sure_payoff = self.participant.vars['icl_sure_payoffs'][self.round_number - 1]

        # determine sure payoff for next choice and append list of sure payoffs
        # ------------------------------------------------------------------------------------------------------------
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['icl_sure_payoffs'].append(
                    self.participant.vars['icl_sure_payoffs'][self.round_number - 1]
                    + Constants.delta / 2 ** (self.round_number - 1) + 2.75 / 2 **(self.round_number - 1)
                )
            elif self.choice == 'B':
                self.participant.vars['icl_sure_payoffs'].append(
                    self.participant.vars['icl_sure_payoffs'][self.round_number - 1]
                    - Constants.delta / 2 ** (self.round_number - 1)
                )
            else:
                pass

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def update_switching_row(self):

        if self.choice == 'B':
            self.participant.vars['icl_switching_row'] -= 2 ** (Constants.num_choices - self.round_number)

        elif self.choice == 'I':
            self.participant.vars['icl_switching_row'] /= 2

    # set final switching row
    # ----------------------------------------------------------------------------------------------------------------
    def set_final_switching_row(self):

        current_round = self.subsession.round_number
        current_choice = self.in_round(current_round).choice

        # set final switching row if all choices have been completed or if "indifferent" was chosen
        # ------------------------------------------------------------------------------------------------------------
        if current_round == Constants.num_rounds or current_choice == 'I':

            # randomly determine choice to "pay" (i.e., in which round otree fills in the switching row)
            # --------------------------------------------------------------------------------------------------------
            completed_choices = len(self.participant.vars['icl_sure_payoffs'])
            choice_to_pay = random.randint(1, completed_choices)

            # implied switching row
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).switching_row = self.participant.vars['icl_switching_row']

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] += 1

