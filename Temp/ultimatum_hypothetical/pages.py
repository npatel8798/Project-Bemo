from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'player'
    form_fields = ['negative_reciprocity']

    def vars_for_template(self):
        return dict(
            endowment=Constants.endowment,
            part_index=self.participant.vars['part_index']
        )

    def before_next_page(self):
        return self.player.update_part_index()


page_sequence = [Decision]
