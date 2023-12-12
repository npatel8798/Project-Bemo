from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


def vars_for_all_templates(self):
    return dict(
        endowment=Constants.endowment,
        rate=Constants.rate,
        max_endowment=Constants.max_endowment,
        other_transfer=Constants.other_transfer,
        page=self.subsession.round_number,
        part_index=self.participant.vars['part_index'],
        currency=Constants.currency,
        instructions=Constants.instructions_template
    )


class Instructions(Page):
    pass


class Introduction(Page):

    form_model = 'player'

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

    def before_next_page(self):
        return self.player.compute_endowment(),


class Receiver(Page):

    form_model = 'player'
    form_fields = ['transfer']

    # only display from round 1 to 4
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number <= Constants.num_rounds - 1

    def vars_for_template(self):
        return dict(
            other_endowment=self.participant.vars['other_endowment'],
            final_endowment=self.participant.vars['final_endowment'],
            other_transfer=self.participant.vars['other_transfer']
        )

    def before_next_page(self):
        return self.player.increase_other_transfer(), self.player.compute_endowment()


class Sender(Page):

    form_model = 'player'
    form_fields = ['transfer']

    # only display instruction in round 5
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def before_next_page(self):
        return self.player.update_part_index()


page_sequence = [Introduction, Receiver, Sender]
