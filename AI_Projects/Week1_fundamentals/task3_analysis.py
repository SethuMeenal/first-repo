import pandas as pd
import numpy as np
#task-1
df = pd.read_csv("C:/Users/sethum/data/TrendPulseConverted.csv")
print(f"first 5 rows preview ");
print(df.head(5))
print(f"shape of the dataframe is {df.shape}")
print(f"average of score across all stories: {df['score'].mean()}")
print(f"average of num_comments across all stories: {df['num_comments'].mean()}")
#task-2
avg_score = np.mean(df['score'])
median_score = np.median(df['score'])
std_deviation_score = np.std(df['score'])
min_score = np.min(df['score'])
max_score = np.max(df['score'])
print(f"average score is {avg_score}")
print(f"median of scores is {median_score}")
print(f"std deviation of scores is {std_deviation_score}")
print(f"min score is {min_score} and max score is {max_score}")
max_stories_category = df['category'].value_counts()
print(f"categories with max num of stories is {max_stories_category.idxmax()}")
max_comments_num = np.max(df['num_comments'])
#printing only when there is significant num of comments. if all are none, then nothing gets printed reg this
if max_comments_num > 0:
    max_commented_title = df.loc[df['num_comments'] == max_comments_num,'title']
    print(f"story with max # comments is having {max_comments_num} comments and title of story is {max_commented_title}")
df["is_popular"] = df["score"]>avg_score
df["engagement"] = df["num_comments"] / (df["score"] + 1)
print(f"two columns added")
#task-4
df.to_csv("data/trends_analysed.csv", index=False)
# Confirmation message
print(f"CSV file saved successfully at data/trends_analysed.csv with {len(df)} rows")
