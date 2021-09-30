import numpy as np
import pandas as pd
import re
import string
from prepare_sentence import prepare_sentence

if __name__ == '__main__':
    dataframe = pd.read_csv("tombola.csv")
    theme = np.zeros(len(dataframe), int)
    print(dataframe)
    for i in range(len(dataframe)):
        str = dataframe.iloc[i, 2]
        if str == "Sport":
            theme[i] = 1
        elif str == "Culture":
            theme[i] = 2
        elif str == "Arts":
            theme[i] = 3
        elif str == "Social":
            theme[i] = 4
        elif str != "":
            theme[i] = 5
        else:
            theme[i] = 0
    print(theme)
    for i in range(len(dataframe)):
        dataframe.iloc[i, 0] = prepare_sentence(dataframe.iloc[i, 0])
        dataframe.iloc[i, 1] = prepare_sentence(dataframe.iloc[i, 1])
    print(dataframe)
        
        
