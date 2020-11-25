import pandas as pd
import os

def loop_directory(directory: str):
    for filename in os.listdir('/Users/ankushv/PycharmProjects/Heart-Attack-Prediction/Data/files/'):
        if filename("01911"):
            file_directory = os.path.join(directory, filename)
            print(filename)
            pd.read_csv(file_directory)

if __name__ == '__main__':
    loop_directory('/Users/ankushv/PycharmProjects/Heart-Attack-Prediction/Data/files/')

    test_list = ['dat', 'hea', 'qrs']
    for filename in os.listdir('/Volumes/Abhijit-Seagate/'):
    if any(ele in filename for ele in test_list):
    print(filename)