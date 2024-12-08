import pandas as pd

def main():

    station = pd.read_csv('Group 2 US101SB\Stations_US101.csv')
    id_list = station['ID'].tolist()
    print(id_list)

if main():
    print('done')
