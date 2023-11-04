import matplotlib.pyplot as plt
def vis(dataset):
    df = dataset

    plt.hist(df['Age'].dropna(), bins=10, color='red')  
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Distribution')

    plt.savefig('vis.png')
