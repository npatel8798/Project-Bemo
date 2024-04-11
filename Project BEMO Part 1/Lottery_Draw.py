import pandas as pd
import random

csv_file_path = r"d:\Neel\Neel - Master's\RA - OTree\serene-basin-02107\serene-basin-02107\Project_BEMO_Q_2023-12-28.csv"
response_sheet = r"d:\Neel\Neel - Master's\RA - OTree\serene-basin-02107\serene-basin-02107\Project BEMO Response Sheet (Responses) - Form Responses 1.csv"

final_result = 'final_result.csv'
df = pd.read_csv(csv_file_path)
target_column = 'participant_label'

#Reading Participant_label from the csv
response = pd.read_csv(response_sheet)
response_list = response.values.tolist()
count = 1
#Selecting Random Question from the Response Sheet
for i in response_list:
    print('Student ID', i[4])
    filtered_rows = df[df[target_column] == i[4]]
    result_list = filtered_rows.values.tolist()
    random_number = random.choice(result_list)
    question_sel = random_number[3]
    choice_sel = random_number[4]
    p_high = random_number[5]
    p_middle = random_number[6]
    p_low = random_number[7]
    print('Question Selected',question_sel)
    print('Choice Selected',choice_sel)
    print('Payout High', p_high)
    print('Payout Middle', p_middle)
    print('Payout Low', p_low)
    if random_number[4] == 'A':
        high = random_number[8]
        middle = random_number[9]
        low = random_number[10]
        print('High', high)
        print('Middle', middle)
        print('Low', low)
    elif random_number[4] == 'B': 
        high = random_number[11]
        middle = random_number[12]
        low = random_number[13]
        print('High', high)
        print('Middle', middle)
        print('Low', low)
    
    #Selecting Random Number Between range 0 to 1 
    random_float = random.uniform(0.00000, 1.00000)
    print('Random Number Selected: -', random_float)
    if 0.0 <= random_float <= high:
        win = p_high
    elif high <= random_float <= middle + high:
        win = p_middle
    elif middle+high <= random_float <= 1.0:
        win = p_low    
        
    print('Payout Selected: -', win)


    result_df = pd.DataFrame({'Student ID': i[4], 'Question Selected':question_sel, 'Choice Selected':choice_sel, 'Payout High':p_high, 'Payout Middle':p_middle, 'Payout Low':p_low, 'High':high, 'Middle':middle, 'Low':low, 'Random Number':random_float, 'Winning Amount':win}, index=[count])
    existing_df = pd.read_csv(final_result) if pd.io.common.file_exists(final_result) else pd.DataFrame()
    merged_df = pd.concat([existing_df, result_df], axis=0)
    merged_df.to_csv(final_result, index=False, header=True)
    count += 1