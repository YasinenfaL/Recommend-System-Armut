#################################################
# Armut-Association Rule Based Recommender System
#################################################


#################################################
# İmporting Libraries
#################################################
import pandas as pd
from datetime import datetime
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
from mlxtend.frequent_patterns import apriori, association_rules

#################################################
# Data Prep.
#################################################

df_ = pd.read_csv("datasets/armut_data.csv")
df = df_.copy()


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe().T)


check_df(df)

# Create a new variable about Service
df["Hizmet"] = df["ServiceId"].astype(str) + "_" + df["CategoryId"].astype(str)
df["New_Date"] = pd.to_datetime(df["CreateDate"]).dt.to_period("M")
df["Sepet_ID"] = df["UserId"].astype(str) + "_" + df["New_Date"].astype(str)

check_df(df)

# Creating pivot table

new_df = pd.pivot_table(df, index="Sepet_ID", columns="Hizmet", values="CategoryId", aggfunc="count"). \
    fillna(0). \
    applymap(lambda x: 1 if x > 0 else 0)

#################################################
# Association Rule Learning
#################################################

frequent_itemsets = apriori(new_df, min_support=0.01, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)

sorted_rules = rules.sort_values("confidence", ascending=False)


# Use the arl_recommender function to recommend a service to a user who last received the 2_0 service

def arl_recommendation_list(sorted_rules, service_id):
    sorted_rules = rules.sort_values("confidence", ascending=False)
    recommendation_list = []
    for i, service in enumerate(sorted_rules["antecedents"]):
        for j in service:
            if j == service_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"]))
    return recommendation_list


arl_recommendation_list(sorted_rules, "2_0")
