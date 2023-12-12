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
Question to Measure "Positive Reciprocity Quantitative" in Preference Survey Module
"""


class Constants(BaseConstants):
    name_in_url = 'pos_reciprocity'
    players_per_group = None
    num_rounds = 1

    stranger_cost = 20
    cheap_present = 5
    expensive_present = 30
    currency = '€'

    # responses
    responses = [
        'No present', 'The present worth €5', 'The present worth €10',
        'The present worth €15', 'The present worth €20',
        'The present worth €25', 'The present worth €30']

    n = len(responses)
    # numerical value of the response
    levels = [str(j) for j in range(1, n + 1)]


class Subsession(BaseSubsession):

    def creating_session(self):

        # create Part index to show in templates' title (i.e., "Part <index>")
        # --------------------------------------------------------------------------------------------------------------
        if "p.participant.vars['part_index']" not in globals():
            for p in self.get_players():
                p.participant.vars['part_index'] = 1

                # Choices
                p.participant.vars['choices'] = [
                    [str(Constants.levels[i]), str(Constants.responses[i])]
                    for i in range(Constants.n)
                ]


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    reciprocity = models.StringField(
        widget=widgets.RadioSelect,
        label=''
    )

    # create set of choices
    # ------------------------------------------------------------------------------------------------------------------
    def reciprocity_choices(self):
        return self.participant.vars['choices']

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] += 1
