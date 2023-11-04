
def eda(dataset):

    df = dataset



    insight_1 = "The average age of the individuals in the dataset is {:.2f} years.".format(df['Age'].mean())  

    insight_2 = "There are {} unique classes in the 'Pclass' column.".format(df['Pclass'].nunique()) 

    correlation = df['SibSp'].corr(df['Parch'])
    insight_3 = "There is a correlation of {:.2f} between 'SibSp' and 'Parch'.".format(correlation)

    with open('eda-in-1.txt', 'w') as f:
        f.write(insight_1)

    with open('eda-in-2.txt', 'w') as f:
        f.write(insight_2)

    with open('eda-in-3.txt', 'w') as f:
        f.write(insight_3)