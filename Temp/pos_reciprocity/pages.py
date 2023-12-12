from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Reciprocity(Page):
    form_model = 'player'
    form_fields = ['reciprocity']

    def vars_for_template(self):
        return dict(
            stranger_cost=Constants.stranger_cost,
            cheap_present=Constants.cheap_present,
            expensive_present=Constants.expensive_present,
            part_index=self.participant.vars['part_index']
        )

    def before_next_page(self):
        return self.player.update_part_index()


page_sequence = [Reciprocity]
