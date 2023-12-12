from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Luca Congiu & Salvatore Nunnari (Bocconi University)'

doc = """
Questions to Measure "Trust Quantative" + "Positive Reciprocity Quantitative" in Preference Survey Module (Hypothetical Trust Game)
"""


class Constants(BaseConstants):
    name_in_url = 'trust_hypothetical'
    players_per_group = None
    num_rounds = 5

    # instructions template across pages
    instructions_template = 'trust_hypothetical/Instructions.html'

    # endowment, multiplication rate, amount transferred by the counterpart
    # ------------------------------------------------------------------------------------------------------------------
    endowment = 20
    rate = 3
    other_transfer = 5
    currency = '€'
    max_endowment = (rate + 1) * endowment  # only for instructions


class Subsession(BaseSubsession):

    def creating_session(self):

        for p in self.get_players():
            p.participant.vars['other_transfer'] = Constants.other_transfer
            p.participant.vars['final_endowment'] = Constants.endowment

            # create Part index to show in templates' title (i.e., "Part <index>")
            # ----------------------------------------------------------------------------------------------------------
            if "p.participant.vars['part_index']" not in globals():
                p.participant.vars['part_index'] = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # fields for the amount the player transfers at each of the five questions
    # ------------------------------------------------------------------------------------------------------------------
    transfer = models.IntegerField(
        min=0,
        label=''
    )

    # create function to determine maximum amount the participant can transfer at each of the five questions
    # ------------------------------------------------------------------------------------------------------------------
    def transfer_max(self):
        #print(self.round_number)
        if self.round_number < 5:
            return self.participant.vars['final_endowment']
        else:
            return Constants.endowment

    # create function to increase transfer by 5 at each question
    # ------------------------------------------------------------------------------------------------------------------
    def increase_other_transfer(self):
        self.participant.vars['other_transfer'] += 5

    # create function to compute the players' endowment at each turn
    # ------------------------------------------------------------------------------------------------------------------
    def compute_endowment(self):
        self.participant.vars['final_endowment'] = Constants.endowment + Constants.rate \
                                                   * self.participant.vars['other_transfer']
        self.participant.vars['other_endowment'] = Constants.endowment - self.participant.vars['other_transfer']

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] += 1
