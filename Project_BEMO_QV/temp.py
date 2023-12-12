import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib.patches as mpatches
df = pd.read_csv("file/Tasks_68_Nov2023.csv")


def draw_circle(ax, center, radius, color):
    circle = plt.Circle(center, radius, color=color, fill=True)
    ax.add_patch(circle)

def plot(uid, prob_a, prob_b, prob_c, text, pay_h, pay_m, pay_l):
    print(uid)
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([-22, 39])
    ax.set_ylim([-22, 29])

    # Set the number of rows and columns
    rows, columns = 4, 5

    # Set the size of the square box and circle radius
    box_size = 30
    circle_radius = 5

    counter_a = int(prob_a * 20)
    counter_b = int(prob_b * 20)
    counter_c = int(prob_c * 20)
    counter = 1
    # Loop to draw 20 circles in a 5x4 grid
    for row in range(rows):
        for column in range(columns):
            x = column * (2 * circle_radius + 2) - (box_size / 2)
            y = row * (2 * circle_radius + 2) - (box_size / 2)
            center = (x, y)
            if counter in range(1, counter_a+1):
                if pay_h == '$100':
                    color = '#FFA500' #Orange
                    draw_circle(ax, center, circle_radius, color)
                elif pay_h == '$250':
                    color = '#FF0000' #Red
                    draw_circle(ax, center, circle_radius, color)
                elif pay_h == '$50':
                    color = '#008000' #Green
                    draw_circle(ax, center, circle_radius, color)
            elif counter in range(counter_a+1, counter_a+counter_b+1):
                if pay_m == '$50':
                    color = '#008000' #Green
                    draw_circle(ax, center, circle_radius, color)
                elif pay_m == '$100':
                    color = '#FFA500' #Orange
                    draw_circle(ax, center, circle_radius, color)
                elif pay_m == '$75':
                    color = '#FFFF00' #Yellow
                    draw_circle(ax, center, circle_radius, color)
                elif pay_m == '$20':
                    color = '#0000FF' #Blue
                    draw_circle(ax, center, circle_radius, color)
            else:
                if pay_l == '$50':
                    color = '#008000' #Green
                    draw_circle(ax, center, circle_radius, color)
                elif pay_l == '$20':
                    color = '#0000FF' #Blue
                    draw_circle(ax, center, circle_radius, color)
                elif pay_l == '$10':
                    color = '#A020F0' #Purple
                    draw_circle(ax, center, circle_radius, color)
            counter += 1

    # Set axis labels and display the plot
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_xlabel('X-axis')
    # ax.set_ylabel('Y-axis')
    # plt.title('Circles in a Square Box')
    if pay_h == '$100':
        blue_patch = mpatches.Patch(color='#FFA500', label='$100')
    elif pay_h == '$250':
        blue_patch = mpatches.Patch(color='#FF0000', label='$250')
    elif pay_h == '$50':
        blue_patch = mpatches.Patch(color='#008000', label='$50')
    
    if pay_m == '$50':
        green_patch = mpatches.Patch(color='#008000', label='$50')
    elif pay_m == '$100':
        green_patch = mpatches.Patch(color='#FFA500', label='$100')
    elif pay_m == '$75':
        green_patch = mpatches.Patch(color='#FFFF00', label='$75')
    elif pay_m == '$20':
        green_patch = mpatches.Patch(color='#0000FF', label='$20')
    if pay_l == '$50':
        orange_patch = mpatches.Patch(color='#008000', label='$50')
    elif pay_l == '$20':
        orange_patch = mpatches.Patch(color='#0000FF', label='$20')
    elif pay_l == '$10':
        orange_patch = mpatches.Patch(color='#A020F0', label='$10')

    plt.legend(handles=[orange_patch, green_patch, blue_patch], loc='lower center', ncol=3, bbox_to_anchor=(0.5, -0.1))
    plt.subplots_adjust(bottom=0.1)
    plt.grid(False)
    text_path = text+'.png'
    path = os.path.join('c:\\Users\\NP\\Downloads\\myproject\\otree_psm-master\\otree_psm-master_1\\Project_BEMO_TEST\\', text_path)
    plt.savefig(path)
    #plt.show()
    print('Text',text+'.png')
    print('Figure')

for i, j in df.iterrows():
    uid = j['UID']
    prob_a = j['LEFT_High']
    prob_b = j['LEFT_Middle']
    prob_c = j['LEFT_Low']
    pay_h = j['PAYOUTS_High']
    pay_m = j['PAYOUTS_Middle']
    pay_l = j['PAYOUTS_Low']
    text = uid + '_Left'
    plot(uid, prob_a, prob_b, prob_c, text, pay_h, pay_m, pay_l)

    prob_a = j['RIGHT_High']
    prob_b = j['RIGHT_Middle']
    prob_c = j['RIGHT_Low']
    text = uid + '_Right'
    plot(uid, prob_a, prob_b, prob_c, text, pay_h, pay_m, pay_l)
    