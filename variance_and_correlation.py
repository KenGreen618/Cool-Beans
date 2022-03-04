from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# trump data
trump_google_trends = pd.read_csv("./resources/csv/trump_gtrends.csv")
print(trump_google_trends)
trump_variance = trump_google_trends['trump: (Worldwide)'].var()
print(trump_variance)

# coffee data
coffee_google_trends = pd.read_csv("./resources/csv/coffee_gtrends.csv")
print(coffee_google_trends)
coffee_variance = coffee_google_trends['coffee: (Worldwide)'].var()
print(coffee_variance)

# robusta data
robusta_google_trends = pd.read_csv("./resources/csv/robusta_gtrends.csv")
print(robusta_google_trends)
robusta_variance = robusta_google_trends['robusta: (Worldwide)'].var()
print(robusta_variance)

# arabica data
arabica_google_trends = pd.read_csv("./resources/csv/arabica_gtrends.csv")
print(arabica_google_trends)
arabica_variance = arabica_google_trends['arabica: (Worldwide)'].var()
print(arabica_variance)

# correlation
arabica_search_frequency = arabica_google_trends['arabica: (Worldwide)']
robusta_search_frequency = robusta_google_trends['robusta: (Worldwide)']
arabica_robusta_correlation = arabica_search_frequency.corr(robusta_search_frequency)
print(arabica_robusta_correlation)

all_coffee_trends_data = pd.concat([coffee_google_trends, robusta_google_trends, arabica_google_trends], axis =1, ignore_index= True )
print(all_coffee_trends_data)
test_2 = pd.merge(coffee_google_trends, robusta_google_trends, on="Month")
print(test_2)
# test_3 = coffee_google_trends.join([robusta_google_trends, arabica_google_trends])
# print(test_3)
test_4 = pd.merge_ordered(test_2, arabica_google_trends,)
print(test_4)
print(test_4.corr())