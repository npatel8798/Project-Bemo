from otree.api import *
import pandas as pd
import numpy as np
import time

class C(BaseConstants):
    NAME_IN_URL = 'project_bemo_q'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 68
    instructions = True

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


def read_csv():
    dat = pd.read_csv("file/Tasks_68_Nov2023.csv")
    last_4_row = dat.tail(4)
    
    selected_row_index = np.random.choice(last_4_row.index)
    selected_row = dat.loc[selected_row_index].copy()
    dat = dat.drop(selected_row_index)
    dat = dat.sample(frac=1)
    dat = pd.concat([selected_row.to_frame().T, dat], ignore_index=True)
    dat = dat.reset_index(drop=True)

    return dat

def creating_session(subsession: Subsession):

    for p in subsession.get_players():

        dat = read_csv()
        p.participant.vars['uid']  = dat['UID'].tolist()
        p.participant.vars['left_h'] = dat['LEFT_High'].tolist()
        p.participant.vars['left_m'] = dat['LEFT_Middle'].tolist()
        p.participant.vars['left_l'] = dat['LEFT_Low'].tolist()
        p.participant.vars['right_h'] = dat['RIGHT_High'].tolist()
        p.participant.vars['right_m'] = dat['RIGHT_Middle'].tolist()
        p.participant.vars['right_l'] = dat['RIGHT_Low'].tolist()
        p.participant.vars['payouts_h'] = dat['PAYOUTS_High'].tolist()
        p.participant.vars['payouts_m'] = dat['PAYOUTS_Middle'].tolist()
        p.participant.vars['payouts_l'] = dat['PAYOUTS_Low'].tolist()
        # if "p.participant.vars['part_index']" not in globals():
        #     p.participant.vars['part_index'] = 1


class Player(BasePlayer):
    choice = models.LongStringField()
    is_mobile = models.BooleanField()
    u_id = models.LongStringField()
    pay_h = models.LongStringField()
    pay_m = models.LongStringField()
    pay_l = models.LongStringField()
    left_h = models.FloatField()
    left_m = models.FloatField()
    left_l = models.FloatField()
    righ_h = models.FloatField()
    righ_m = models.FloatField()
    righ_l = models.FloatField()
    page_time = models.FloatField()
    page_start_time = models.FloatField()
    survey_id = models.StringField()

    
    def set_sure_payoffs(self):
        self.page_time = time.time() - self.page_start_time
        csv_file_path = 'output\output_Q.csv'
        self.survey_id = 'Part 1'
        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.survey_id = 'Part 1'
        self.u_id = select_ui = self.participant.vars['uid'][self.round_number - 1]
        self.left_h = select_lh = self.participant.vars['left_h'][self.round_number - 1]
        self.left_m = select_lm = self.participant.vars['left_m'][self.round_number - 1]
        self.left_l = select_ll = self.participant.vars['left_l'][self.round_number - 1]
        self.pay_h = select_ph = self.participant.vars['payouts_h'][self.round_number - 1]
        self.pay_m = select_pm = self.participant.vars['payouts_m'][self.round_number - 1]
        self.pay_l = select_pl = self.participant.vars['payouts_l'][self.round_number - 1]
        self.righ_h = select_rh = self.participant.vars['right_h'][self.round_number - 1]
        self.righ_m = select_rm = self.participant.vars['right_m'][self.round_number - 1]
        self.righ_l = select_rl = self.participant.vars['right_l'][self.round_number - 1]

        df = pd.DataFrame({'session':self.session.code, 'participant_code':self.participant.code, 'participant_label':self.participant.label,'uid': self.u_id, 'choice':self.choice, 'Payout_High':self.pay_h, 'Payout_Middle':self.pay_m, 'Payout_Low':self.pay_l, 'Left_High':self.left_h, 'Left_Middle':self.left_m, 'Left_low':self.left_l, 'Right_High':self.righ_h, 'Right_Middle':self.righ_m, 'Right_Low':self.righ_l, 'Page_Time':self.page_time, 'Time_Started_UTC':self.page_start_time, 'Survey_ID':self.survey_id}, index=[self.round_number])
        existing_df = pd.read_csv(csv_file_path) if pd.io.common.file_exists(csv_file_path) else pd.DataFrame()
        merged_df = pd.concat([existing_df, df], axis=0)
        merged_df.to_csv(csv_file_path, index=False, header=True)

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] += 1



# PAGES
class Decision(Page):
    form_model = 'player'
    form_fields = ['choice']
    @staticmethod
    def vars_for_template(self):
        self.page_start_time = time.time()
        # specify info for progress bar
        total = C.NUM_ROUNDS
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
            'quest':        page,
            'total':       total,
            'progres':    progress,
            'uid':uid,
            'a': text_a,
            'b': text_b,
            'left_path':image_path_left,
            'right_path':image_path_right
        }

    def before_next_page(player : Player, timeout_happened):
        player.set_sure_payoffs()

class Instructions(Page):
    form_model = 'player'
    form_fields = ['is_mobile']
    def is_displayed(self):
        return self.subsession.round_number == 1

    def error_message(player: Player, values):
        if values['is_mobile']:
            return "Sorry, this experiment does not allow mobile browsers."

    def vars_for_template(self):
        pass

class Results(Page):
    form_model = 'player'
    # form_fields = ['is_mobile']
    def is_displayed(self):
        return self.subsession.round_number == 68

    # def error_message(player: Player, values):
    #     if values['is_mobile']:
    #         return "Sorry, this experiment does not allow mobile browsers."

    def vars_for_template(self):
        pass

# page_sequence = [MyPage]
page_sequence = [Instructions, Decision, Results]


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'participant_label', 'uid' ,'choice', 'Payout_High', 'Payout_Middle', 'Payout_Low', 'Left_High', 'Left_Middle', 'Left_Low', 'Right_High', 'Right_Middle', 'Right_Low', 'Page_Time', 'Time_Started_UTC', 'Survey_ID']
    for p in players:
        participant = p.participant
        session = p.session
        yield [session.code, participant.code, participant.label, p.u_id, p.choice, p.pay_h, p.pay_m, p.pay_l, p.left_h, p.left_m, p.left_l, p.righ_h, p.righ_m, p.righ_l, p.page_time, participant.time_started_utc, p.survey_id]
