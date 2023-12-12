from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Altruism(Page):
    form_model = 'player'
    form_fields = ['altruism_hypothetical']

    def vars_for_template(self):
        return dict(
            endowment_str="{:,}".format(Constants.endowment),
            endowment=Constants.endowment,
            part_index=self.participant.vars['part_index']
        )

    def before_next_page(self):
        return self.player.update_part_index()


page_sequence = [Altruism]
