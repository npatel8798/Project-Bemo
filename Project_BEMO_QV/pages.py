from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(self):
    return {
        'a': 'a'
    }


# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #
class Instructions(Page):

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return dict(
            today=Constants.today,
            in_12_months=Constants.in_12_months
        )


# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['choice']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_choices
        page = self.subsession.round_number
        progress = page / total * 100
        uid = self.participant.vars['uid'][page - 1]
        left_h = self.participant.vars['left_h'][page - 1]
        left_m = self.participant.vars['left_m'][page - 1]
        left_l = self.participant.vars['left_l'][page - 1]
        right_h = self.participant.vars['right_h'][page - 1]
        right_m = self.participant.vars['right_m'][page - 1]
        right_l = self.participant.vars['right_l'][page - 1]
        payouts_h = self.participant.vars['payouts_h'][page - 1]
        payouts_m = self.participant.vars['payouts_m'][page - 1]
        payouts_l = self.participant.vars['payouts_l'][page - 1]
        
        print("{}".format(self.participant.vars['uid'][page - 1]))
        

        count_a = 0
        if left_h > 0.0:
            text_ah = ("{0} with probability {1}%\n".format(payouts_h, int(left_h*100)))
            count_a += 1
        else:
            text_ah = ''
        if left_m > 0.0:
            text_am = ("{0} with probability {1}%\n".format(payouts_m, int(left_m*100)))
            count_a += 1
        else:
            text_am = ''
        if left_l > 0.0:
            text_al = ("{0} with probability {1}%\n".format(payouts_l, int(left_l*100)))
            count_a += 1
        else:
            text_al = ''
        text_a = text_ah + text_am + text_al
        
        text_a = text_a.strip()
        
        if count_a == 2:
            text_a += '\n'
        elif count_a == 1:
            text_a += '\n\n'
        
        count_b = 0
        if right_h > 0.0:
            text_bh = ("{0} with probability {1}%\n".format(payouts_h, int(right_h*100)))
            count_b += 1
        else:
            text_bh = ''
        if right_m > 0.0:
            text_bm = ("{0} with probability {1}%\n".format(payouts_m, int(right_m*100)))
            count_b += 1
        else:
            text_bm = ''
        if right_l > 0.0:
            text_bl = ("{0} with probability {1}%\n".format(payouts_l, int(right_l*100)))
            count_b += 1
        else:
            text_bl = ''
        text_b = text_bh + text_bm + text_bl
              
        text_b = text_b.strip()
        
        if count_b == 2:
            text_b += '\n'
        elif count_b == 1:
            text_b += '\n\n'

        left_path = self.participant.vars['uid'][page - 1] + '_Left'
        image_path_left = 'images/{}.png'.format(left_path)

        right_path = self.participant.vars['uid'][page - 1] + '_Right'
        image_path_right = 'images/{}.png'.format(right_path)
        return {
            'page':        page,
            'total':       total,
            'progres':    progress,
            'uid':uid,
            'a': text_a,
            'b': text_b,
            'left_path':image_path_left,
            'right_path':image_path_right
        }

    def before_next_page(self):
        self.player.set_sure_payoffs()


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [Decision]

if Constants.instructions:
    page_sequence.insert(0, Instructions)


