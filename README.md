# Association Rule Based Recommender System

![rs2](https://user-images.githubusercontent.com/111612847/225994138-edcd09dc-be18-4253-87ed-8a9d7eb2809c.jpg)

## Introduction about Apriori algorithm
The Apriori algorithm is a frequently used data mining technique for finding frequent itemsets in a dataset. It is used to discover which items (or items sets) occur together frequently in a dataset. The algorithm first finds the frequency of individual items in the dataset, and then proceeds to find combinations of these items, such as pairs, triples, and so on, until all combinations have been found. This process is repeated until no more combinations can be found. The Apriori algorithm can handle large datasets and is used in various fields such as data mining, market analysis, recommendation systems, and web page analysis.
#### Usage areas: 
* Market analysis
* Web page analysis
* Recommendation systems 
* Financial data analysis.

## Busıness Problem
Armut, Turkey's largest online service platform, brings service providers and those who want to receive services together. With just a few taps on their computer or smartphone, users can easily access services such as cleaning, renovation, and transportation. Using the dataset that includes users who have received services and the categories of services they received, an association rule learning-based product recommendation system is desired to be created.

## Dataset Story
The data set consists of the services customers receive and the categories of these services.Date and time of each service received contains information.


## Variables
* UserId: Customer number
* ServiceId: They are anonymized services belonging to each category.
* CategoryId: They are anonymized categories. (Example: Cleaning, transportation, renovation category)
* CreateDate: The date the service was purchased



## Tasks
* Task 1: Preparing the Data
* Task 2: Generate and Suggest Association Rules
