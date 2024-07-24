# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:37:25 2024

@author: Laiba Binta Tahir
"""

#Naives bayes theorm 
import pandas as pd

# 1- Define Data
data = {
    'Day': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14'],
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temp.': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# 2. prior Prob
def prior_Prob(df):
    total = len(df)
    decision_counts = df['Decision'].value_counts()
    yes_count = decision_counts.get('Yes', 0)
    no_count = decision_counts.get('No', 0)
    
    prior_yes = yes_count / total
    prior_no = no_count / total
    
    return prior_yes, prior_no

prior_yes, prior_no = prior_Prob(df)
print("\n")
print("---------------------------------------")
print("Prior Probabilities:")
print("---------------------------------------")
print("Prior Prob of 'Yes':", prior_yes)
print("Prior Prob of 'No':", prior_no)
print("\n")

# 3. Posterior Probability Calculation
def posterior_prob(df):
    total_yes = df[df['Decision'] == 'Yes'].shape[0]
    total_no = df[df['Decision'] == 'No'].shape[0]
    
    # -------------------- Outlook --------------------
    sunny_yes = df[(df['Outlook'] == 'Sunny') & (df['Decision'] == 'Yes')].shape[0]
    overcast_yes = df[(df['Outlook'] == 'Overcast') & (df['Decision'] == 'Yes')].shape[0]
    rain_yes = df[(df['Outlook'] == 'Rain') & (df['Decision'] == 'Yes')].shape[0]
    
    sunny_no = df[(df['Outlook'] == 'Sunny') & (df['Decision'] == 'No')].shape[0]
    overcast_no = df[(df['Outlook'] == 'Overcast') & (df['Decision'] == 'No')].shape[0]
    rain_no = df[(df['Outlook'] == 'Rain') & (df['Decision'] == 'No')].shape[0]
    
    post_sunny_yes = sunny_yes / total_yes 
    post_overcast_yes = overcast_yes / total_yes 
    post_rain_yes = rain_yes / total_yes 
    
    post_sunny_no = sunny_no / total_no 
    post_overcast_no = overcast_no / total_no 
    post_rain_no = rain_no / total_no 

    # --------------------Temp------------------
    hot_yes = df[(df['Temp.'] == 'Hot') & (df['Decision'] == 'Yes')].shape[0]
    mild_yes = df[(df['Temp.'] == 'Mild') & (df['Decision'] == 'Yes')].shape[0]
    cool_yes = df[(df['Temp.'] == 'Cool') & (df['Decision'] == 'Yes')].shape[0]
    
    hot_no = df[(df['Temp.'] == 'Hot') & (df['Decision'] == 'No')].shape[0]
    mild_no = df[(df['Temp.'] == 'Mild') & (df['Decision'] == 'No')].shape[0]
    cool_no = df[(df['Temp.'] == 'Cool') & (df['Decision'] == 'No')].shape[0]
    
    post_hot_yes = hot_yes / total_yes 
    post_mild_yes = mild_yes / total_yes 
    post_cool_yes = cool_yes / total_yes 
    
    post_hot_no = hot_no / total_no 
    post_mild_no = mild_no / total_no 
    post_cool_no = cool_no / total_no 

    # -------------------- Humidity --------------------
    high_yes = df[(df['Humidity'] == 'High') & (df['Decision'] == 'Yes')].shape[0]
    normal_yes = df[(df['Humidity'] == 'Normal') & (df['Decision'] == 'Yes')].shape[0]
    
    high_no = df[(df['Humidity'] == 'High') & (df['Decision'] == 'No')].shape[0]
    normal_no = df[(df['Humidity'] == 'Normal') & (df['Decision'] == 'No')].shape[0]
    
    post_high_yes = high_yes / total_yes 
    post_normal_yes = normal_yes / total_yes 
    
    post_high_no = high_no / total_no 
    post_normal_no = normal_no / total_no 

    #-------------------- Wind --------------------
    weak_yes = df[(df['Wind'] == 'Weak') & (df['Decision'] == 'Yes')].shape[0]
    strong_yes = df[(df['Wind'] == 'Strong') & (df['Decision'] == 'Yes')].shape[0]
    
    weak_no = df[(df['Wind'] == 'Weak') & (df['Decision'] == 'No')].shape[0]
    strong_no = df[(df['Wind'] == 'Strong') & (df['Decision'] == 'No')].shape[0]
    
    post_weak_yes = weak_yes / total_yes 
    post_strong_yes = strong_yes / total_yes 
    
    post_weak_no = weak_no / total_no 
    post_strong_no = strong_no / total_no 

    return {
        'Outlook': {'Sunny': (post_sunny_yes, post_sunny_no), 'Overcast': (post_overcast_yes, post_overcast_no), 'Rain': (post_rain_yes, post_rain_no)},
        'Temp.': {'Hot': (post_hot_yes, post_hot_no), 'Mild': (post_mild_yes, post_mild_no), 'Cool': (post_cool_yes, post_cool_no)},
        'Humidity': {'High': (post_high_yes, post_high_no), 'Normal': (post_normal_yes, post_normal_no)},
        'Wind': {'Weak': (post_weak_yes, post_weak_no), 'Strong': (post_strong_yes, post_strong_no)}
    }

posterior = posterior_prob(df)
print("---------------------------------------")
print("Posterior Probabilities:")
print("---------------------------------------")

for key, value in posterior.items():
    print("\n{}:".format(key))
    for sub_key, sub_value in value.items():
        print("- {}: Yes - {:.2f}, No - {:.2f}".format(sub_key, sub_value[0], sub_value[1]))

# 4. Test Data
def predict_instance(instance, posterior):
    p_yes = (
        posterior['Outlook'][instance['Outlook']][0] * 
        posterior['Temp.'][instance['Temp.']][0] * 
        posterior['Humidity'][instance['Humidity']][0] * 
        posterior['Wind'][instance['Wind']][0]
    )
    
    p_no = (
        posterior['Outlook'][instance['Outlook']][1] * 
        posterior['Temp.'][instance['Temp.']][1] * 
        posterior['Humidity'][instance['Humidity']][1] * 
        posterior['Wind'][instance['Wind']][1]
    )
    
    if p_yes > p_no:
        return 'Yes'
    else:
        return 'No'
# 4 - predict function
def predict(test_data, posterior):
    predictions = []
    for _, instance in test_data.iterrows():
        predictions.append(predict_instance(instance, posterior))
    return predictions

# 5- Test data
def test_data(test_data, posterior):
    test_data['Predicted'] = predict(test_data, posterior)
    print(test_data)

test_data_df = pd.DataFrame({
    'Outlook': [ 'Overcast'],
    'Temp.': [ 'Mild'],
    'Humidity': ['Normal'],
    'Wind': [ 'Strong']
})

print("\n-----------------------------------------------")
print("Test Data:")
print("-------------------------------------------------")
test_data(test_data_df, posterior)