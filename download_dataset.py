from datasets import load_dataset
import pandas as pd

def load_cyclone_data():
    dataset = load_dataset('torchgeo/tropical_cyclone', ignore_verifications=True)
    df_train = pd.DataFrame(dataset['train'])
    df_test = pd.DataFrame(dataset['test'])
    return df_train, df_test
