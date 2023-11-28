import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv('beer-and-diaper.csv')
print("Dataset:")
print(data)

te = TransactionEncoder()
te_ary = te.fit(data['item'].apply(lambda x:
x.split(',')).tolist()).transform(data['item'].apply(lambda x:
x.split(',')).tolist())
df = pd.DataFrame(te_ary, columns=te.columns_)


# frequent_itemsets
min_support = 0.3
frequent_itemsets = apriori(df, min_support=min_support,
use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)


# closed frequent_itemsets
closed_itemsets = frequent_itemsets.copy()
for i, itemset in frequent_itemsets.iterrows():
    for j, compare_itemset in frequent_itemsets.iterrows():
        if i != j and set(itemset['itemsets']).issubset(set(compare_itemset['itemsets'])):
            closed_itemsets = closed_itemsets.drop(i, axis=0)
            break

print("\nClosed Frequent Itemsets:")
print(closed_itemsets)


# maximal frequent_itemsets
maximal_itemsets = frequent_itemsets.copy()
for i, itemset in frequent_itemsets.iterrows():
    for j, compare_itemset in frequent_itemsets.iterrows():
        if i != j and set(itemset['itemsets']).issubset(set(compare_itemset['itemsets'])):
            maximal_itemsets

print("\nMaximal Frequent Itemsets:")
print(maximal_itemsets)