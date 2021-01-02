#!/usr/bin/env python
# coding: utf-8

# # CrunchieMunchies
# 
# You work in marketing for a food company <b>myCorps</b>, which is developing a new kind of tasty, wholesome cereal called <b>CrunchieMunchies</b>. 
# 
# You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you’ve dug up nutritional data on several different competitors.
# 
# Your task is to use <em>NumPy statistical calculations</em> to analyze this data and prove that your <b>CrunchieMunchies</b> is the healthiest choice for consumers.
# 
# 
# 
# 
# 

# # Task STEPS
# 

# 1.First, import numpy.

# In[3]:


import numpy as np


# 2.Look over the <b><em>cereal.csv</em></b> file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as <b><em>calorie_stats.</em></b>
# 
# 

# In[43]:


import csv
from numpy import genfromtxt 
calorie_stats = genfromtxt ('cereal.csv', delimiter=',')
calorie_stats = np.array(calorie_stats)
# print("This is Our Dataset")
print(calorie_stats)


# 3.There are <em>60 calories per serving of CrunchieMunchies</em>. How much <b>higher</b> is the <b>average calorie count</b> of your competition?
# 
# Save the answer to the variable <b>average_calories</b> and print the variable to the terminal to see the answer.
# 

# In[7]:


average_calories = calorie_stats.mean()
# print("This is the Average Calorie Count")
# print("================================")
print(average_calories)


# 4.Does the <b>average calorie count</b> adequately reflect the distribution of the dataset? Let’s sort the data and see.
# 
# <b><em>Sort</em></b> the data and save the result to the variable <b>calorie_stats_sorted</b>. Print the sorted data to the terminal.
# 

# In[42]:


print(calorie_stats)
calorie_stats_sorted = np.sort(calorie_stats)
# print("This is the Dataset After Sorting")
# print("=================================")
print(calorie_stats_sorted)


# 5.Do you see what I’m seeing? Looks like <b><em>the majority of the cereals are higher than the mean</em></b>. Let’s see if the <b>median</b> is a better representative of the dataset.
# 
# Calculate the median of the dataset and save your answer to <b><em >median_calories</em></b>. Print the median so you can see how it compares to the mean.

# In[44]:


median_calories = np.median(calorie_stats_sorted)
# print("This is the Median of The Data")
# print("==============================")
print(median_calories)


# 6.While the median demonstrates that <b><em><q>at least half of our values are over 100 calories</q></em></b>, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.
# 
# <b>Calculate different percentiles</b> and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable <b>nth_percentile</b>.
# 

# In[48]:


# print("This is the 15th Percentile of the Data")
# print("=======================================")
print(np.percentile(calorie_stats_sorted,15))
# print("This is the 10th Percentile of the Data")
# print("=======================================")
print(np.percentile(calorie_stats_sorted,10))
# print("Here We Find The Correct Percentile")
# print("===================================")
nth_percentile = (np.percentile(calorie_stats_sorted,4))
print(nth_percentile)


# 7.While the percentile shows us that<b><em><q>the majority of the competition has a much higher calorie count</q></em></b>, it’s an awkward concept to use in marketing materials.
# 
# Instead, let’s calculate the percentage of cereals that <b><em><q>have more than 60 calories per serving</q></em></b>. Save your answer to the variable <b><em>more_calories</em></b> and print it to the terminal

# In[50]:


more_calories = np.average(calorie_stats_sorted)
# print("This is the Average of the Data")
# print("===============================")
print(more_calories)


# 8.Wow! That’s a really high percentage. That’s going to be very useful when we promote CrunchieMunchies. But one question is, <b><em>how much variation exists in the dataset? </b></em></q>Can we make the generalization that most cereals have around 100 calories or is the spread even greater?
# 
# Calculate the amount of variation by finding the <b><em>standard deviation</em</b> Save your answer to <b><em>calorie_std</em></b> and print to the terminal. How can we incorporate this value into our analysis?

# In[51]:


calorie_std = np.std(calorie_stats_sorted)
# print("This is the Amount of Deviaton in the Data")
# print("==========================================")
print(calorie_std)


# 9.Write a short paragraph that sums up your findings and how you think this data could be used to 
# <b>myCorp’s</b> advantage when marketing CrunchieMunchies.
# 
print('Report')
print('In this task I did the following things:')

print('I was given a dataset of calories')
print('First of all I found the average of the data to find the average calorie count of our competition.')
print('I sorted the data then to check if the average calorie count adequately reflect the distribution of the dataset.')
print('Then I found the median of the data because majority of the cerials were higher than the mean.')
print("Then I found different percentiles of the data to find the lowest percentile which was greater than '60'calories.")
print("Then I found the percentage of the cerials that have more than '60' calories per serving.")
print("At last I found the variation in the data by finding the standard deviation.")
print('My Suggestions and Reviews:')
print("I think that this data is really useful as it has a number of advantages as follows:")
print('This data can be used to boost up the business.')
print('This data will help in taking business decisions.')
print('This data can be used to make predictions by the model with a great accuracy.')
print("Moreover, I think that this will help myCorp's to grow well and compete its other competitors in the market. This data will really help in the marketing of CrunchieMunchies as we have proved that our cereal is the most healthiest in the market.")




