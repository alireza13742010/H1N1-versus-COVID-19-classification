import pandas as pd 
import numpy as np 

def Preprocesing(df):
  fatigue =[]
  d = df['Fatigue '].value_counts()
  for x in d.index:
    fatigue.append(x)
  Gastrointestinal =[]
  d = df['Gastrointestinal '].value_counts()
  for x in  d.index:
    Gastrointestinal.append(x)
  fever = []
  d =df['Fever'].value_counts()
  for x in  d.index:
    fever.append(x)
  Sore_throat = ['Yes','No','throat(Yes)','throat(No)','throat(Unk)']
  Running_Nose = ['Yes','No','running nose(Yes)','running nose(No)','running nose(Mild)','running nose(None)','running nose(Unk)','running nose(4)']
  Hyper_Tension = ['No','Yes','chills(Yes)','chills(No)','chills(Unk)','nausea(Yes)']
  Headache = ['Yes','No','aches(Yes)','headache(None)','headache(Mild)','headache(Severe)','headache(Moderate)',
            'headache(4)','aches(No)','aches(Unk)','headache(Yes)','headache(Not reported)',
            'headache(TRUE)','throat(ukn)']
  Dry_Cough = ['Yes','No','cough(Yes)','cough(None)','cough(Mild)','cough(4)','cough(TRUE)',
             'cough(Moderate)','cough(No)','cough(Not reported)','chills(Yes)']
  Breathing_Problem = ['Yes','No','dyspnea(No)"','dyspnea(Yes)"','dyspnea(Unk)"']
  for x in fatigue:
    if x=='Yes' :
      i=np.where(df['Fatigue ']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([1])
    if x=='fatigue(Yes)"' :
      i=np.where(df['Fatigue ']== 'fatigue(Yes)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([1])
    if x=='fatigue(Yes)' :
      i=np.where(df['Fatigue ']== 'fatigue(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([1])
    if x=='No' :
      i=np.where(df['Fatigue ']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([0])
    if x=='fatigue(No)' :
      i=np.where(df['Fatigue ']== 'fatigue(No)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([0])
    if x=='fatigue(Moderate)' :
      i=np.where(df['Fatigue ']== 'fatigue(Moderate)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([2])
    if x=='fatigue(Mild)' :
      i=np.where(df['Fatigue ']== 'fatigue(Mild)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([2])
    if x=='fatigue(Mild)"' :
      i=np.where(df['Fatigue ']== 'fatigue(Mild)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([2])
    if x=='fatigue(Moderate)"' :
      i=np.where(df['Fatigue ']== 'fatigue(Moderate)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([2])
    if x=='fatigue(Severe)' :
      i=np.where(df['Fatigue ']== 'fatigue(Severe)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([3])
    if x=='fatigue(4)' :
      i=np.where(df['Fatigue ']== 'fatigue(4)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([2])
    if x=='fatigue(EH)"' :
      i=np.where(df['Fatigue ']== 'fatigue(EH)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([2])
    if x=='fatigue(None)' :
      i=np.where(df['Fatigue ']== 'fatigue(None)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,11]=np.array([-1])
    else:
      for x in df['Fatigue '].value_counts().index[5:]:
        i=np.where(df['Fatigue '] == x)
        i1=[[x for x in j]for j in i ]
        df.iloc[i1,11]=np.array([-1])

  for x in Gastrointestinal:
    if x=='Yes' :
      i=np.where(df['Gastrointestinal ']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,12]=np.array([1])
    if x=='diarrhea(Yes)' :
      i=np.where(df['Gastrointestinal ']== 'diarrhea(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,12]=np.array([1])
    else :
      i=np.where(df['Gastrointestinal ']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,12]=np.array([0])

  for x in fever:
    if x=='Yes' :
      i=np.where(df['Fever']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([1])
    elif x=='fever(Yes)' :
      i=np.where(df['Fever']== 'fever(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([1])
    elif x=='fever(TRUE)"' :
      i=np.where(df['Fever']== 'fever(TRUE)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([1])
    elif x=='fever(Yes)"' :
      i=np.where(df['Fever']== 'fever(Yes)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([1])
    elif x=='No' :
      i=np.where(df['Fever']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([0])
    elif x=='fever(No)' :
      i=np.where(df['Fever']== 'fever(No)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([0])
    elif x=='fever(None)' :
      i=np.where(df['Fever']== 'fever(None)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([-1])
    elif x=='fever(None)"' :
      i=np.where(df['Fever']== 'fever(None)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([-1])
    elif x=='temperature(101.84)' :
      i=np.where(df['Fever']== 'temperature(101.84)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='high_temp_home(101.7)' :
      i=np.where(df['Fever']== 'high_temp_home(101.7)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='temperature(100.2)' :
      i=np.where(df['Fever']== 'temperature(100.2)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='temperature(100.1)' :
      i=np.where(df['Fever']== 'temperature(100.1)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='temperature(101.66)' :
      i=np.where(df['Fever']== 'temperature(101.66)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='high_temp_home(101.12)' :
      i=np.where(df['Fever']== 'high_temp_home(101.12)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='temperature(101.66)' :
      i=np.where(df['Fever']== 'temperature(101.66)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='temperature(100.8)"' :
      i=np.where(df['Fever']== 'temperature(100.8)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='fever(Mild)' :
      i=np.where(df['Fever']== 'fever(Mild)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='fever(Moderate)' :
      i=np.where(df['Fever']== 'fever(Moderate)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    elif x=='temperature(100.8)"' :
      i=np.where(df['Fever']== 'temperature(100.8)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,1]=np.array([2])
    else:
      for x in df['Fever'].value_counts().index[4:10]:
        i=np.where(df['Fever'] == x)
        i1=[[x for x in j]for j in i ]
        df.iloc[i1,1]=np.array([4])
      for x in df['Fever'].value_counts().index[4:-6]:
        i=np.where(df['Fever'] == x)
        i1=[[x for x in j]for j in i ]
        df.iloc[i1,1]=np.array([2])
      for x in df['Fever'].value_counts().index[4:]:
        i=np.where(df['Fever'] == x)
        i1=[[x for x in j]for j in i ]
        df.iloc[i1,1]=np.array([4])

  for x in Sore_throat:
    if x=='Yes' :
      i=np.where(df['Sore throat']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,3]=np.array([1])
    if x=='throat(Yes)' :
      i=np.where(df['Sore throat']== 'throat(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,3]=np.array([1])
    if x=='No' :
      i=np.where(df['Sore throat']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,3]=np.array([0])
    if x=='throat(No)' :
      i=np.where(df['Sore throat']== 'throat(No)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,3]=np.array([0])
    if x=='throat(Unk)' :
      i=np.where(df['Sore throat']== 'throat(Unk)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,3]=np.array([-1])

  for x in Running_Nose:
    if x=='Yes' :
      i=np.where(df['Running Nose']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([1])
    if x=='running nose(Yes)' :
      i=np.where(df['Running Nose']== 'running nose(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([1])
    if x=='No' :
      i=np.where(df['Running Nose']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([0])
    if x=='running nose(No)' :
      i=np.where(df['Running Nose']== 'running nose(No)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([0])
    if x=='running nose(None)' :
      i=np.where(df['Running Nose']== 'running nose(None)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([-1])
    if x=='running nose(Unk)' :
      i=np.where(df['Running Nose'] == 'running nose(Unk)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([-1])
    if x=='running nose(4)' :
      i=np.where(df['Running Nose'] == 'running nose(4)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([3])
    if x=='running nose(Mild)' :
      i=np.where(df['Running Nose'] == 'running nose(Mild)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,4]=np.array([2])

  for x in Hyper_Tension:
    if x=='Yes' :
      i=np.where(df['Hyper Tension']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,10]=np.array([1])
    if x=='No' :
      i=np.where(df['Hyper Tension']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,10]=np.array([0])
    if x=='chills(Yes)' :
      i=np.where(df['Hyper Tension']== 'chills(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,10]=np.array([1])
    if x=='chills(No)' :
      i=np.where(df['Hyper Tension']== 'chills(No)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,10]=np.array([0])
    if x=='chills(Unk)' :
      i=np.where(df['Hyper Tension']== 'chills(Unk)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,10]=np.array([-1])
    if x=='nausea(Yes)' :
      i=np.where(df['Hyper Tension']== 'nausea(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,10]=np.array([-1])

  for x in Headache:
    if x=='Yes' :
      i=np.where(df['Headache']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([1])
    if x=='aches(Yes)' :
      i=np.where(df['Headache']== 'aches(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([1])
    if x=='headache(TRUE)' :
      i=np.where(df['Headache']== 'headache(TRUE)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([1])
    if x=='headache(Yes)' :
      i=np.where(df['Headache']== 'headache(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([1])
    if x=='headache(Moderate)' :
      i=np.where(df['Headache']== 'headache(Moderate)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([2])
    if x=='headache(Mild)' :
      i=np.where(df['Headache']== 'headache(Mild)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([2])
    if x=='headache(Severe)' :
      i=np.where(df['Headache']== 'headache(Severe)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([3])
    if x=='headache(4)' :
      i=np.where(df['Headache']== 'headache(4)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([3])
    if x=='No' :
      i=np.where(df['Headache']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([0])
    if x=='aches(No)' :
      i=np.where(df['Headache']== 'aches(No)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([0])
    if x=='headache(None)':
      i=np.where(df['Headache']== 'headache(None)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([-1])
    if x=='aches(Unk)' :
      i=np.where(df['Headache']== 'aches(Unk)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([-1])
    if x=='headache(Not reported)' :
      i=np.where(df['Headache']== 'headache(Not reported)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([-1])
    if x=='throat(ukn)' :
      i=np.where(df['Headache']== 'throat(ukn)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,7]=np.array([-1])


  for x in Dry_Cough:
    if x=='Yes' :
      i=np.where(df['Dry Cough']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([1])
    if x=='cough(Yes)' :
      i=np.where(df['Dry Cough']== 'cough(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([0.8])
    if x=='cough(TRUE)' :
      i=np.where(df['Dry Cough']== 'cough(TRUE)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([0.8])
    if x=='cough(Mild)' :
      i=np.where(df['Dry Cough']== 'cough(Mild)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([2])
    if x=='cough(Moderate)' :
      i=np.where(df['Dry Cough']== 'cough(Moderate)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([2])
    if x=='cough(4)' :
      i=np.where(df['Dry Cough']== 'cough(4)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([3])
    if x=='No' :
      i=np.where(df['Dry Cough']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([0])
    if x=='cough(No)' :
      i=np.where(df['Dry Cough']== 'cough(No)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([0])
    if x=='cough(None)' :
      i=np.where(df['Dry Cough']== 'cough(None)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([-1])
    if x=='cough(Not reported)' :
      i=np.where(df['Dry Cough']== 'cough(Not reported)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([-1])
    if x=='chills(Yes)' :
      i=np.where(df['Dry Cough']== 'chills(Yes)')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,2]=np.array([-1])

  for x in Breathing_Problem:
    if x=='Yes' :
      i=np.where(df['Breathing Problem']== 'Yes')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,0]=np.array([1])
  for x in Breathing_Problem:
    if x=='dyspnea(Yes)"' :
      i=np.where(df['Breathing Problem']== 'dyspnea(Yes)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,0]=np.array([1])
  for x in Breathing_Problem:
    if x=='No' :
      i=np.where(df['Breathing Problem']== 'No')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,0]=np.array([0])
  for x in Breathing_Problem:
    if x=='dyspnea(No)"' :
      i=np.where(df['Breathing Problem']== 'dyspnea(No)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,0]=np.array([0])
  for x in Breathing_Problem:
    if x=='dyspnea(Unk)"' :
      i=np.where(df['Breathing Problem']== 'dyspnea(Unk)"')
      i1=[[x for x in j]for j in i ]
      df.iloc[i1,0]=np.array([-1])
  return df


