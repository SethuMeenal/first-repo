import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#print(os.getcwd())
#print(os.listdir())
df = pd.read_csv("breastfeeding_dataset.csv",keep_default_na=False)
print(f"---Shape of Dataset loaded is")
print(df.shape)#12K rows and 19 columns
print(df.head())
print(f"---Datatype check & conversion")
print(df["breastfeeding_duration_months"].dtype)
#changing the datatypes to numeric wherever required(except id, all numeric value columns in dataset are listed here)
numeric_cols = [
    "mother_age",
    "mother_bmi",
    "parity",
    "child_age_months",
    "birth_weight_kg",
    "current_weight_kg",
    "breastfeeding_duration_months",
    "feeding_frequency_per_day",
    "gestational_age_weeks",
    "weight_for_age_zscore",
    "illness_episodes_last_3months"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
print(df[numeric_cols].dtypes)
print(f"---Null check")
print(df.isnull().sum())
missing_percent = (df.isnull().sum()/len(df))*100
missing_df = pd.DataFrame({
    'Missing Count': df.isnull().sum(),
    'Missing %': missing_percent
})
print(missing_df[missing_df['Missing Count']>0].sort_values('Missing %', ascending=False))
print(df['delivery_complications'].value_counts(dropna=False))
df["delivery_complications"] = df["delivery_complications"].fillna("None")
df['immunization_status'] = df['immunization_status'].replace('', 'None')
print(df.isnull().sum())
df = df.dropna()
print(df.shape)
print(df.isnull().sum())
print(f"---Duplicate check")
print(df.duplicated().sum())
print(df.info())
print(f"---checking outliers & removing invalids, replacing blanks in categorical columns")
print(df.describe().T)
num_cols = df.select_dtypes(include='number').columns
print(df[num_cols].describe().T)
for col in num_cols:
    print(col, round(df[col].skew(), 3))
#checking highest absolute skewness
skews = df[num_cols].skew()
print(skews.abs().sort_values(ascending=False))
top2_skewed = skews.abs().sort_values(ascending=False).head(2)
print(top2_skewed)
#IQR Calc
cols = ['current_weight_kg',
        'weight_for_age_zscore']
for col in cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[
        (df[col] < lower) |
        (df[col] > upper)
    ]
    print("\n", col)
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Outliers:", len(outliers))
print(f"---EDA")
#checking distribution on health status
#line plot
plt.figure(figsize=(8,5))
plt.plot(df.index,
         df['current_weight_kg'])
plt.title("Current Weight Trend")
plt.xlabel("Row Index")
plt.ylabel("Current Weight (kg)")
plt.savefig("lineplot_current_weight.png",
            bbox_inches='tight')
plt.show()
#histogram
sns.histplot(
    df['illness_episodes_last_3months'],
    bins=20
)
plt.title("Histogram of Illness Episodes")
plt.savefig("hist_skewed_variable.png",
            bbox_inches='tight')
plt.show()
#scatter plot
sns.scatterplot(
    data=df,
    x='child_age_months',
    y='current_weight_kg'
)
plt.title("Child Age vs Current Weight")
plt.savefig("scatter_age_weight.png",
            bbox_inches='tight')
plt.show()
print(df.groupby('child_age_months')['current_weight_kg'].agg(
    ['min','mean','max']))
bad_rows = df[
    (df['current_weight_kg'] <= 1.5) &
    (df['child_age_months'] > 4)
]
#removing bad rows where weight is 1.5 kg but child age is greater than or = to 8 months
print(bad_rows.shape)
print(bad_rows[['child_age_months',
                'birth_weight_kg',
                'current_weight_kg',
                'health_status']])
df = df[
    ~(
        (df['current_weight_kg'] <= 1.5) &
        (df['child_age_months'] > 4)
    )
]
print(df.shape)
#box plot
plt.figure(figsize=(8,5))
sns.boxplot(
    data=df,
    x='health_status',
    y='weight_for_age_zscore'
)
plt.title("Weight-for-Age Z-Score by Health Status")
plt.savefig("zscore_vs_health_status.png",
            bbox_inches="tight")
plt.show()
#bar chart
mean_illness = (
    df.groupby('immunization_status')
      ['illness_episodes_last_3months']
      .mean()
)
plt.figure(figsize=(8,5))
plt.bar(
    mean_illness.index,
    mean_illness.values,
    color=['lightgreen', 'orange', 'tomato']
)
plt.title('Average Illness Episodes by Immunization Status')
plt.xlabel('Immunization Status')
plt.ylabel('Mean Illness Episodes (Last 3 Months)')
plt.tight_layout()
plt.savefig(
    'bar_immunization_vs_illness.png',
    bbox_inches='tight'
)
plt.show()
print(f"---Correlation analysis")
plt.figure(figsize=(16,10))
sns.heatmap(
    df.select_dtypes(include='number').corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)
plt.title("Correlation Heatmap")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.subplots_adjust(left=0.25, bottom=0.20)
plt.savefig(
    "correlation_heatmap.png",
    bbox_inches="tight",
    dpi=300
)
plt.show()
df.to_csv(
    'cleaned_data.csv',
    index=False
)
print(f"---Saved to cleaned_data.csv file")


#understanding dataset
print(f"---suspecting the rows where 'formula only' feeding type but breastfed duration in months is also populated")
print(df[(df["feeding_type"] == "Formula Only") & (df["breastfeeding_duration_months"] > 0)].shape)
print(df[(df["feeding_type"] == "Formula Only") & (df["breastfeeding_duration_months"] > 0)][["child_age_months","feeding_type","breastfeeding_duration_months"]].head(20))
print(df.groupby("feeding_type")["breastfeeding_duration_months"].agg(["count", "mean", "min", "max"]))
print(df['mother_age'].describe())
print(df[df['mother_age'] < 18]['mother_age'].value_counts().sort_index())
print(df[df['mother_age'] < 18].shape)
print(df[df['mother_bmi'] > 40])
print(df['parity'].value_counts().sort_index())
print(df[df['current_weight_kg'] > 20][
    ['child_age_months','current_weight_kg']
])
print(df[df['current_weight_kg'] > 20].shape)
df = df[df['current_weight_kg'] <= 20]
print(df.shape)
print(df[df['illness_episodes_last_3months'] > 10])
print(f"---Summary stats")
print(df['health_status'].value_counts())
print(df['feeding_type'].value_counts())
print(df['immunization_status'].value_counts())
print(df['immunization_status'].unique())
print(f"---catching blanks")
for col in df.select_dtypes(include='object'):
    print(col)
    print(df[col].unique())
    print('-'*50)
print((df['delivery_complications'] == '').sum())
df['delivery_complications'] = df['delivery_complications'].replace('', 'None')
print(df['delivery_complications'].unique())
df['education_level'] = df['education_level'].replace('', 'No Education')
print(df['education_level'].unique())
sns.countplot(data=df, x='health_status')
plt.title('Distribution of Health Status')
plt.savefig('health_status_distribution.png',bbox_inches='tight')
plt.show()
plt.figure(figsize=(8,5))
#feeding type vs health status
sns.countplot(
    data=df,
    x='feeding_type',
    hue='health_status'
)
plt.title("Feeding Type vs Health Status")
plt.xticks(rotation=15)
plt.savefig("feeding_type_vs_health_status.png",bbox_inches="tight")
plt.show()
#immunization vs health status
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x='immunization_status',
    hue='health_status'
)
plt.title("Immunization Status vs Health Status")
plt.savefig("immunization_vs_health_status.png",
            bbox_inches="tight")
plt.show()
#current weight vs health status
plt.figure(figsize=(8,5))
sns.boxplot(
    data=df,
    x='health_status',
    y='current_weight_kg'
)
plt.title("Current Weight by Health Status")
plt.savefig("current_weight_vs_health_status.png",
            bbox_inches="tight")
plt.show()
print(df[
    (df['health_status'] == 'Healthy') &
    (df['current_weight_kg'] < 2)
][['child_age_months',
   'birth_weight_kg',
   'current_weight_kg',
   'weight_for_age_zscore',
   'health_status']])
#finding rows with label inconsistencies
print(df[
    (df['health_status'] == 'Healthy') &
    (df['current_weight_kg'] <= 1.6) &
    (df['child_age_months'] > 0)
].shape)
#removing rows as they are only 3 rows(neglible)
df = df[
    ~(
        (df['health_status'] == 'Healthy') &
        (df['current_weight_kg'] <= 1.6) &
        (df['child_age_months'] > 0)
    )]
print(df.shape)
#delivery complications vs health status
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x='delivery_complications',
    hue='health_status'
)
plt.title("Delivery Complications vs Health Status")
plt.savefig("delivery_complications_vs_health_status.png",
            bbox_inches="tight")
plt.show()
