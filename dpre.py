import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import load
import eda
import vis
df = load.p()

### CLeaning

df['Age'].fillna(df['Age'].mean(), inplace=True)

df.dropna(subset=['Embarked'], inplace=True)

df.drop('Cabin', axis=1, inplace=True)


### Discretization

age_bins = [0, 15, 30, 50, 80]  
age_labels = ['Child', 'Young Adult', 'Middle-Aged', 'Senior']
fare_bins = [-0.001, 10, 50, 100, 600] 
fare_labels = ['Low', 'Moderate', 'High', 'Very High']
df['Age_Bins'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)
df['Fare_Bins'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels)


numerical_columns = ['Age', 'Fare']
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])


### Reduction

df.drop('Name',axis=1,inplace = True)
df.drop('Fare',axis=1,inplace = True)


df.to_csv('res_dpre.csv')

eda(df)
vis(df)