
'''
DocString
'''

import pandas as pd
import numpy as np


def generate_covariants(data: pd.DataFrame) -> np.ndarray:
    '''
    Generates covariants based on a dataframe
    '''

    inprod = data[['Unnamed: 0', 'produto']]

    names = inprod['produto'].to_numpy()

    indices = inprod['Unnamed: 0'].to_numpy()

    df = pd.read_csv('covariancia_classico.csv')

    return df.loc[indices, names].to_numpy()
