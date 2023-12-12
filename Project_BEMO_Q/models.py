from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from Project_BEMO_Q.config import *
import random
import pandas as pd
import logging
import os
import random
import numpy as np
import csv

author = 'Neel Patel'

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


doc = """

"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    # initiate list of sure payoffs and implied switching row in first round
    # ------------------------------------------------------------------------------------------------------------
    def creating_session(self):
        # creating index denoting new App (e.g., Part 'index')
        dat = pd.read_csv("file/Tasks_68_Nov2023.csv")
        last_4_row = dat.tail(4)
        
        selected_row_index = np.random.choice(last_4_row.index)
        selected_row = dat.loc[selected_row_index].copy()
        
        dat = dat.drop(selected_row_index)
        dat = dat.sample(frac=1)
        dat = pd.concat([selected_row.to_frame().T, dat], ignore_index=True)
        dat = dat.reset_index(drop=True)
        
        self.session.vars["data"] = dat
        for p in self.get_players():
            df = self.session.vars["data"]
            p.participant.vars['uid']  = df['UID'].tolist()
            p.participant.vars['left_h'] = df['LEFT_High'].tolist()
            p.participant.vars['left_m'] = df['LEFT_Middle'].tolist()
            p.participant.vars['left_l'] = df['LEFT_Low'].tolist()
            p.participant.vars['right_h'] = df['RIGHT_High'].tolist()
            p.participant.vars['right_m'] = df['RIGHT_Middle'].tolist()
            p.participant.vars['right_l'] = df['RIGHT_Low'].tolist()
            p.participant.vars['payouts_h'] = df['PAYOUTS_High'].tolist()
            p.participant.vars['payouts_m'] = df['PAYOUTS_Middle'].tolist()
            p.participant.vars['payouts_l'] = df['PAYOUTS_Low'].tolist()
            # p.participant.vars['icl_time_sure_payoffs'] = [Constants.sure_payoff]
            # p.participant.vars['icl_switching_row'] = 2 ** Constants.num_choices
            # create Part index to show in templates' title (i.e., "Part <index>")
            # ------------------------------------------------------------------------------------------------------
            if "p.participant.vars['part_index']" not in globals():
                p.participant.vars['part_index'] = 1


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    # ----------------------------------------------------------------------------------------------------------------
    sure_payoff = models.FloatField()
    choice = models.StringField()
    switching_row = models.IntegerField()
    #payoff_ecu = models.FloatField()
    
    # Save values 
    # ----------------------------------------------------------------------------------------------------------------
    def set_sure_payoffs(self):
        #logging.info(self.choice)
        csv_file_path = 'output\output.csv'
        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        if self.choice == 'A':
            select_ui = self.participant.vars['uid'][self.round_number - 1]
            select_lh = self.participant.vars['left_h'][self.round_number - 1]
            select_lm = self.participant.vars['left_m'][self.round_number - 1]
            select_ll = self.participant.vars['left_l'][self.round_number - 1]
            select_ph = self.participant.vars['payouts_h'][self.round_number - 1]
            select_pm = self.participant.vars['payouts_m'][self.round_number - 1]
            select_pl = self.participant.vars['payouts_l'][self.round_number - 1]
            lst = [select_ui, self.choice, select_lh, select_lm, select_ll, select_ph, select_pm, select_pl]
            logging.info([self.choice, select_lh, select_lm, select_ll, select_ph, select_pm, select_pl, select_ui])
        elif self.choice == 'B':
            select_ui = self.participant.vars['uid'][self.round_number - 1]
            select_rh = self.participant.vars['right_h'][self.round_number - 1]
            select_rm = self.participant.vars['right_m'][self.round_number - 1]
            select_rl = self.participant.vars['right_l'][self.round_number - 1]
            select_ph = self.participant.vars['payouts_h'][self.round_number - 1]
            select_pm = self.participant.vars['payouts_m'][self.round_number - 1]
            select_pl = self.participant.vars['payouts_l'][self.round_number - 1]
            lst = [select_ui, self.choice, select_rh, select_rm, select_rl, select_ph, select_pm, select_pl]
            print([select_ui, self.choice, select_rh, select_rm, select_rl, select_ph, select_pm, select_pl, ])

        # df = pd.DataFrame({'Value': lst})
        # existing_df = pd.read_csv(csv_file_path) if pd.io.common.file_exists(csv_file_path) else pd.DataFrame()
        # merged_df = pd.concat([existing_df, df], axis=1)
        # merged_df.to_csv(csv_file_path, index=False, header=True)

        df = pd.DataFrame({'UID': lst[0], 'Choice':lst[1], 'High':lst[2], 'Middle':lst[3], 'Low':lst[4], 'Payout H':lst[5], 'Payout M':lst[6], 'Payout L':lst[7]}, index=[self.round_number])
        existing_df = pd.read_csv(csv_file_path) if pd.io.common.file_exists(csv_file_path) else pd.DataFrame()
        merged_df = pd.concat([existing_df, df], axis=0)
        merged_df.to_csv(csv_file_path, index=False, header=True)

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] += 1

