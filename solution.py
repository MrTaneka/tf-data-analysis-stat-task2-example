from scipy.stats import chi2
import numpy as np


chat_id = 919511341

def solution(p: float, x: np.array) -> tuple:
    sum = 0.0
    for i in range(0, len(x)):
        sum = sum + (x[i] - np.mean(x))*(x[i] - np.mean(x))
    sum = sum/(len(x)-1)
    left = chi2.ppf(1-p/2, df=len(x)-1)
    right = chi2.ppf(p/2, df=len(x)-1)
    return sum/(23*left), sum/(23*right)
