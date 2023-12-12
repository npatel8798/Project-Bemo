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
Question to Measure "Altruism Quantitative" in Preference Survey Module (Hypothetical Dictator Game)
"""


class Constants(BaseConstants):
    name_in_url = 'dictator_hypothetical'
    players_per_group = None
    num_rounds = 1

    endowment = 1_000


class Subsession(BaseSubsession):

    def creating_session(self):

        # create Part index to show in templates' title (i.e., "Part <index>")
        # ----------------------------------------------------------------------------------------------------------
        if "p.participant.vars['part_index']" not in globals():
            for p in self.get_players():
                p.participant.vars['part_index'] = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    altruism_hypothetical = models.IntegerField(
        min=0, max=Constants.endowment,
        label=''
    )

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] += 1

