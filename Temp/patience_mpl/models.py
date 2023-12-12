from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from patience_mpl.config import *
import random
from random import randrange


author = 'Felix Holzmeister'

doc = """
Multiple price list task as proposed by Holt/Laury (2002), American Economic Review 92(5).
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:

            n = Constants.num_choices
            for p in self.get_players():

                # create Part index to show in templates' title (i.e., "Part <index>")
                # ----------------------------------------------------------------------------------------------------
                if "p.participant.vars['part_index']" not in globals():
                    p.participant.vars['part_index'] = 1

                # create list of lottery indices
                # ----------------------------------------------------------------------------------------------------
                indices = [j for j in range(1, n + 1)]

                # create list of payments in 12 months
                original_list = Constants.original_list.copy()
                p.participant.vars['list_payments'] = original_list

                if not Constants.use_original_list:

                    payment12 = Constants.payment12
                    increment = Constants.increment
                    list_payments = [payment12]

                    for j in range(n - 1):
                        increment += Constants.rate
                        payment12 += increment
                        list_payments.append(round(payment12, 1))

                    p.participant.vars['list_payments'] = list_payments

                # create list corresponding to form_field variables including all choices
                # ----------------------------------------------------------------------------------------------------
                form_fields = ['choice_' + str(k) for k in indices]

                # create list of choices
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['patience_choices'] = list(
                    zip(indices, form_fields, p.participant.vars['list_payments'])
                )

                # randomly determine index/choice of binary decision to pay
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['patience_index_to_pay'] = random.choice(indices)
                p.participant.vars['patience_choice_to_pay'] = 'choice_' + str(p.participant.vars['patience_index_to_pay'])

                # randomize order of lotteries if <random_order = True>
                # ----------------------------------------------------------------------------------------------------
                if Constants.random_order:
                    random.shuffle(p.participant.vars['patience_choices'])

                # initiate list for choices made
                # ----------------------------------------------------------------------------------------------------
                p.participant.vars['patience_choices_made'] = [None for j in range(1, n + 1)]

            # generate random switching point for PlayerBot in tests.py
            # --------------------------------------------------------------------------------------------------------
            for participant in self.session.get_participants():
                participant.vars['patience_switching_point'] = random.randint(1, n)


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
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    if Constants.certain_choice:
        for j in range(1, Constants.num_choices + 1):
            locals()['choice_' + str(j)] = models.StringField()
        del j
    else:
        for j in range(1, Constants.num_choices):
            locals()['choice_' + str(j)] = models.StringField()
        del j

    random_draw = models.IntegerField()
    choice_to_pay = models.StringField()
    option_to_pay = models.StringField()
    inconsistent = models.IntegerField()
    switching_row = models.IntegerField()

    # set player's payoff
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_payoffs(self):

        # set <choice_to_pay> to participant.var['choice_to_pay'] determined creating_session
        # ------------------------------------------------------------------------------------------------------------
        self.choice_to_pay = self.participant.vars['patience_choice_to_pay']

        # elicit whether lottery "A" or "B" was chosen for the respective choice
        # ------------------------------------------------------------------------------------------------------------
        self.option_to_pay = getattr(self, self.choice_to_pay)

        # random draw to determine whether to pay the "high" or "low" outcome of the randomly picked lottery
        # ------------------------------------------------------------------------------------------------------------
        self.random_draw = randrange(1, 11)

        # set player's payoff
        # ------------------------------------------------------------------------------------------------------------
        if self.option_to_pay == 'A':
            self.participant.vars['option_chosen'] = 'payment today'
            self.payoff = Constants.null_payoff
            if Constants.results:
                self.payoff = Constants.payment
        else:
            self.participant.vars['option_chosen'] = 'payment in 12 months'
            self.payoff = Constants.null_payoff
            if Constants.results:
                self.payoff = self.participant.vars['list_payments'][self.participant.vars['patience_index_to_pay'] - 1]

        # set payoff as global variable
        # ------------------------------------------------------------------------------------------------------------
        self.participant.vars['patience_payoff'] = self.payoff

    # determine consistency
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_consistency(self):

        n = Constants.num_choices

        # replace A's by 1's and B's by 0's
        self.participant.vars['patience_choices_made'] = [
            1 if j == 'A' else 0 for j in self.participant.vars['patience_choices_made']
        ]

        # check for multiple switching behavior
        for j in range(1, n):
            choices = self.participant.vars['patience_choices_made']
            self.inconsistent = 1 if choices[j] > choices[j - 1] else 0
            if self.inconsistent == 1:
                break

    # determine switching row
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def set_switching_row(self):

        # set switching point to row number of first 'B' choice
        if self.inconsistent == 0:
            self.switching_row = sum(self.participant.vars['patience_choices_made']) + 1

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] += 1
