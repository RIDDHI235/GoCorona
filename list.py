import pandas as pd
import numpy as np
from pandas import DataFrame

s = {'Most Common': pd.Series(['fever', 'dry', 'cough', 'tiredness']),
     'Least Common': pd.Series(['aches and pains', 'sore throat', 'diarrhoea', 'conjunctivitis', 'headache', 'loss of taste or smell', 'a rash on skin', 'discolouration of fingers or toes']),
     'Serious': pd.Series(['difficulty breathing', 'shortness of breath', 'chest pain', 'pressure', 'loss of speech',  'loss of movement'])}

p = {'Prevention': pd.Series(['Clean your hands often',
                              'Use soap,water or an alcohol-based hand rub.',
                              'Maintain social distancing.',
                              'Wear a mask during mass gathering.',
                              'Don’t touch your eyes, nose or mouth.',
                              'Cover your nose and mouth with your bent elbow.',
                              'Cover face with tissue when you cough or sneeze.',
                              'Stay home if you feel unwell.',
                              'If you have any symptoms seek medical attention.'])}

class Symptoms_Prevention:

    def choose_input(self):
        choose = int(input("What would you like to refer?\n 0: Symptoms \n 1: Preventions \n-->"))
        if choose == 0:
            self.chosen_symptom()
        elif choose == 1:
            self.chosen_prevention()
        else:
            print("Please enter a valid input.")


    def chosen_symptom(self):
        print("The following symptoms have been discovered for Corona Virus:\n")
        df = pd.DataFrame(s)
        print(df)


    def chosen_prevention(self):
        print("The following are the preventive measures for Corona Virus:\n")
        df1 = pd.DataFrame(p)
        print(df1)


sp = Symptoms_Prevention()
sp.choose_input()


