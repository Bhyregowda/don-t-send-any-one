from requests import Session
import pandas as pd
import numpy as np 
df = pd.DataFrame(
 np.random.randn(5, 3),
 index=['a', 'c', 'f', 'n', 'x'],
 columns=['bangalore', 'mysore', 'delhi'])