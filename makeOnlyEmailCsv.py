import pandas as pd
from settings import *

dataset = pd.read_csv(DATA_PATH)

df_email = dataset[EMAIL_LABEL]

df_email.to_csv('df_email.csv', index=False, header=False)