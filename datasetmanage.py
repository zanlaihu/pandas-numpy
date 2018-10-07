import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)




def question_1():

    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country', 'Total.1': 'Total_Medals'}, inplace=True)

    merged = merged.head(5)
    print(merged)


def question_2():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country'}, inplace=True)
    # Same as the question_1()


    merged = merged.set_index(['Country'])

    print(merged.head(1))

def question_3():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country'}, inplace=True)
    # Same as the question_1()

    merged = merged.drop(columns=['Rubish'])

    print(merged.head(5))


def question_4():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country'}, inplace=True)
    # Same as the question_1()

    merged = merged.dropna(how='any')
    print(merged.tail(10))

def question_5():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country', 'Gold_x': 'Gold_summer'}, inplace=True)

    # Same as the question_1()


    merged = merged.sort_values(by=["Gold_summer"], ascending=False)

    print(merged.iat[1, 0] + ' won the the most gold medals in summer games.')

def question_6():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country', 'Gold_x': 'Gold_summer'}, inplace=True)

    # Same as the question_1()
    merged['Gold_Different'] = abs(merged.Gold_summer - merged.Gold_y)

    merged = merged.sort_values(by=["Gold_Different"], ascending=False)


    print(merged.iat[1, 0] + ' had the biggest difference between their summer and winter gold medal')

def question_7():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country', 'Gold_x': 'Gold_summer', 'Total.1': 'Total of medals'}, inplace=True)

    # Same as the question_1()

    merged = merged.sort_values(by=["Total of medals"], ascending=False)
    print('The first country: ')
    print(merged[1:2])
    print('\n')
    print('The last five countries:')
    print(merged.tail(5))

def question_8():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1, thousands=',')
    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')

    merged = pd.merge(summer, winter, on='Unnamed: 0')
    merged.rename(columns={'Unnamed: 0': 'Country', 'Gold_x': 'Gold_summer', 'Total.1': 'Total of medals'}, inplace=True)

    # Same as the question_1()

    merged = merged.sort_values(by=["Total of medals"], ascending=False)

    merged = merged[['Country', 'Total_x', 'Total_y']]
    merged = merged[1:10]
    merged = merged.groupby('Country').sum().plot.barh(stacked=True, title="Medals for Winter and Summer Games")
    merged.legend(['Summer', 'Winter'])
    plt.tight_layout()
    plt.show()


def question_9():

    winter = pd.read_csv('Olympics_dataset2.csv', skiprows=1, thousands=',')
    winter.rename(columns={'Unnamed: 0': 'Country'}, inplace=True)

    # Same as the question_1()



    winter = winter[['Country','Gold', 'Silver', 'Bronze']]
    winter = winter.iloc[[143,6,52,70,97]]

    winter = winter.groupby('Country').sum().plot.bar(title="Winter Games")
    winter.legend(['Gold', 'Silver', 'Bronze'], ncol=4)
    # merged.legend(['Summer', 'Winter'])
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    print('question1: ')
    question_1()
    print('\n------------------\n')
    print('question2: ')
    question_2()
    print('\n------------------\n')
    print('question3: ')
    question_3()
    print('\n------------------\n')
    print('question4: ')
    question_4()
    print('\n------------------\n')
    print('question5: ')
    question_5()
    print('\n------------------\n')
    print('question6: ')
    question_6()
    print('\n------------------\n')
    print('question7: ')
    question_7()
    print('\n------------------\n')
    print('question8: ')
    question_8()
    print('\n------------------\n')
    print('question9: ')
    question_9()
