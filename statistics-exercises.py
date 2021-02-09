#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd



np.random.seed(123)


# ## 1. How likely is it that you roll doubles when rolling two dice?

# In[12]:


# the number of times to run the same simulation.
number_of_simulations = nrows = 10**5
#how many dice rolls in each simulation
number_of_dice_rolled = ncols = 2

#each side of a dice
choice = [1,2,3,4,5,6]
#picks random options from the 'dice' amoun of times specified, 
#reshapes the output in rows and columns based on our amount of simulations and rolls per trial
rolls = np.random.choice(choice, nrows * ncols).reshape(nrows, ncols)

#convertsthe rolls to dataframe
rolls_df = pd.DataFrame(rolls)

#applies a function to check if the two dice rolls match, and takes the average of times this occurs
prob = rolls_df.apply(lambda row: row[0] == row[1], axis=1).mean()
print("The probability of rolling doubles when you roll two die is", prob)


# ## 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# In[17]:


number_trials = nrows = 10000
number_coins = ncols = 8

flips = np.random.choice([1, 0], nrows * ncols).reshape(nrows, ncols)
#now add the row total
trial = flips.sum(axis=1)
# then get the average of those where the sum is 3
three_heads=(trial==3).mean()
print("The probability of rolling exactly 3 heads is", three_heads)


# In[18]:


greater_than_three=(trial> 3).mean()
print("The probability of rolling more than 3 heads is", greater_than_three)


# ## 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# In[21]:


prob= [.75, .25]
billboard = np.random.choice(["WD", "DS"], size=10000, p=prob)
data = (billboard == "DS").mean()
total_ds=data**2
print("The probability of driving by two Codeup Data Science Students is", total_ds)


# ## 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

# In[28]:


poptarts_per_week = np.random.randint(low=8, high=23, size=10000)

poptarts_left = 17 - poptarts_per_week
friyay=(poptarts_left>=1).mean()
print("The probability of being able to buy some poptarts Friday afternoon is", friyay)


# ## 5. Compare Heights
# <ul>
# <li>Men have an average height of 178 cm and standard deviation of 8cm.
# <li>Women have a mean of 170, sd = 6cm.
# <li>If a man and woman are chosen at random, P(woman taller than man)?

# In[29]:


# make a sample of 10000 men and 10000 women with heights within 1 stdev of mean
men = np.random.normal(loc=178, scale=8, size=10000)
women = np.random.normal(loc=170, scale=6, size=10000)

# subtract men - women, if result is negative then the woman is taller
tallest = men - women

# find average where tallest is negative
men_or_women=(tallest<0).mean()
print("The probability of a woman being taller than a man is", men_or_women )


# ## 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 

# ### What are the odds that after having 50 students download anaconda, no one has an installation issue? 

# In[38]:


# 1/250 chance of corruption to percent success and percent fail
probabilities = [.996, .004]
# generate 10,000 trails in sets of 50 students
installer = np.random.choice(["Install", "Corruption"], size=(10000, 50), p=probabilities)
# find average where fail in the set of 50
# convert to df to apply lambda to look for corruption in set
installed = pd.DataFrame(installer)
# apply lambda function and average row where corruption present subtract % corruption from 1 to get % all insta;;
all_install = 1 - (installed.apply(lambda row: "Corruption" in row.values, axis=1).mean())
print("The probability that no one has an installation issue with 50 students is", all_install)


# ### 100 students?

# In[37]:


# generate 10,000 trails in sets of 100 students
installer = np.random.choice(["Install", "Corruption"], size=(10000, 100), p=probabilities)
# find average where corruption in the set of 100
# convert to df to apply lambda to look for corruption in set
installed = pd.DataFrame(installer)
# apply lambda function and average row where corruption present subtract % corruption  from 1 to get % all install
all_install = 1 - (installed.apply(lambda row: "Corruption" in row.values, axis=1).mean())
print("The probability that no one has an installation issue with 100 students is", all_install)


# ### What is the probability that we observe an installation issue within the first 150 students that download anaconda?

# In[41]:


# generate 10,000 trails in sets of 150 students
installer = np.random.choice(["Install", "Corruption"], size=(10000, 150), p=probabilities)
# find average where corruption in the set of 150
# convert to df to apply lambda to look for corruption in set
installed = pd.DataFrame(installer)
# apply lambda function and average row where corruption  present subtract % corruption  from 1 to get % all install
all_install =installed.apply(lambda row: "Corruption" in row.values, axis=1).mean()
print("The probability that someone has an installation issue within the first 150 students is", all_install)


# ### How likely is it that 450 students all download anaconda without an issue?

# In[43]:


# generate 10,000 trails in sets of 100 students
installer = np.random.choice(["Install", "Corruption"], size=(10000, 450), p=probabilities)
# find average where corruption in the set of 100
# convert to df to apply lambda to look for corruption in set
installed = pd.DataFrame(installer)
# apply lambda function and average row where corruption present subtract % corruption  from 1 to get % all install
all_install = 1 - (installed.apply(lambda row: "Corruption" in row.values, axis=1).mean())
print("The probability that no one has an installation issue with 450 students is", all_install)


# ## 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?

# In[44]:


unlikely = sum(np.random.binomial(3, 0.7, 20000)==0)/20000
print("The probability that you havent seen a food truck in three days is", unlikely)


# ### How likely is it that a food truck will show up sometime this week?

# In[45]:


likely = 1-(sum(np.random.binomial(7, 0.7, 20000)==0)/20000)
print("The probability that a food truck will show up sometime this week is", likely)


# ## 8. If 23 people are in the same room, what are the odds that two of them share a birthday? 

# In[50]:


birthday = np.random.randint(1, 366, (10_000, 23))
twenty_three_birthday=(pd.DataFrame(birthday).nunique(axis=1) < 23).mean()
print("The odds of 2 in 23 people sharing a birthday are", twenty_three_birthday)


# ### What if it's 20 people?

# In[51]:


birthday = np.random.randint(1, 366, (10_000, 20))
twenty_birthday= (pd.DataFrame(birthday).nunique(axis=1) < 20).mean()
print("The odds of 2 in 20 people sharing a birthday are", twenty_birthday)


# ### 40?

# In[52]:


birthday = np.random.randint(1, 366, (10_000, 40))
forty_birthday=(pd.DataFrame(birthday).nunique(axis=1) < 40).mean()
print("The odds of 2 in 40 people sharing a birthday are", forty_birthday)

