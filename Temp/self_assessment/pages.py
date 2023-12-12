from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


def vars_for_all_templates(self):
    return dict(
        part_index=self.participant.vars['part_index'],
        levels=Constants.levels,
        choices=Constants.choices
    )


class SelfAssessment(Page):
    form_model = 'player'
    form_fields = ['favor_return', 'unjust_revenge', 'people_best_intent']


class RiskAssessment(Page):
    form_model = 'player'
    form_fields = ['risk_assessment']

    def before_next_page(self):
        return self.player.update_part_index()

    
page_sequence = [
    SelfAssessment,
#    RiskAssessment
]
