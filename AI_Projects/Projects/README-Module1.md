What is this dataset about?
The dataset has information about infant's (less than 2 yrs old) health & feeding patterns.
Few key columns include Feeding types(exclusive breastfed / formula/mixed), child's birth weight and current weight, weight for age z scale metric (provided by WHO)value, health status and their immunization , illness frequency reported on last 3 months, mothers age and bmi, child's gender,etc..
This was downloaded from kaggle. 
link -> https://www.kaggle.com/datasets/enochdonkor/breastfeeding-impact/data

Why I chose this?
I am a mother of two year old. So I could relate to breastfeeding and its impact on their future health. So I took it up to find more interesting observations and patterns about it.

What am I looking to do with this?
Though this dataset has scope to do both regression as well as classification(with the health status column as target)
As a first timer, I'm not doing regression with the weight_for_age_zscore continuous column, and metrics will also be more
the standard weight for age zscale is a metric by WHO and it could indicate whether a kid (less than 5 yrs) is moving towards obese, underweight or normal.
I referred this https://www.who.int/tools/child-growth-standards/standards/weight-for-age

So, choosing classification here.


What I doubted initially about the data?
I saw few rows having incorrect meaning like 
feeding type is formula feed but breastfeeding months is 1.0 also the child age is 1 month.
Ideally the feeding type should have been written as mixed instead of formula only.
But the number of rows like this is really less and wherever the child age is greater than breastfed duration 
and feeding type is formula only, the maximum number of months they were breastfed is only 3 and average is 1.
so I could infer that feeding type column means current feeding type and
even if they were previously breastfed during the first month(during the survey) 
so I'm considering this as valid data not deleting anything.

What have I done for cleaning?
First I saw The column delivery_complications contained 54.88% missing values. 
in excel, I saw out of 6640 rows showing NaN, only 19 rows are blanks. other 6621 rows are "None".
so I changed the file loading line like "keep_default_na=False"
Also changed numeric value columns to numeric type instead of str.
Since missingness likely represents the absence of complications rather than 
unavailable information, missing values were replaced with the category "None".

For the other columns (both numeric and non numeric), 
The dataset contained a small number of missing values (<1%) across most columns. 
Since the dataset consisted of more than 12,000 rows, missing values rows were removed to avoid imputation. 
after removal, latest num of rows are 11995.

No duplicates were there in dataset.

Skewness for numeric columns:
+ve skew: Long tail toward larger values.
Mean > Median.
Extreme high values pull the mean upward.
Median is preferred for imputation.

-ve skew: long tail towards smaller values.
Mean < Median.
Extreme low values pull mean towards downward.
Median is preferred for imputation.

Finding & Handling outliers:

Outliers were identified using the IQR method for 2 main columns. 
Outliers on other below columns were also retained because as they represent genuine biological variation.

1. Mother age range starts from 13. 
between 13 to 18 are totally 855 records. but not removed as they are biologically possible(in adolescence)

2. Mother bmi > 40 
biologically possible, so data retained.

3. parity max value is 12.
biologically possible, so data retained.
observation: wherever parity is greater than 5, mostly children are at risk & unhealthy(99%).

4. Ten rows were identified with impossible child weights 
(25–28 kg for younger than 24 months). These records were treated as data-entry errors 
and removed prior to analysis.

5. immunization was blank(empty strings) for 7 rows. they were replaced with None(meaning not receiving vaccinations)


Label inconsistencies were found inbetween distribution plots like babies with weight less than 1.5 kg 
but age greater then 1 months were termed healthy in health_status column. 
so they were removed as its biologically incorrect.

Minute EDA observations(excluding obvious ones) from correlation matrix that require further investiigations:
0.From the scatter plot, A visible discontinuity in average child weight after 12 months of age is seen. 
The mean current weight increased from birth to 12 months (9.16 kg at 12 months), 
but dropped sharply at 13 months (6.15 kg), 
may be the dataset may have been generated using different weight distributions for infants (0–12 months) and toddlers (13–24 months). 
the observations were retained and the issue is documented as a dataset limitation.

Four rows were identified where children older than four months had a current weight of approximately 1.5 kg. 
As these values were considered biologically imppossible, they were treated as data-quality errors 
and removed from the dataset prior to analysis.
1. from the bar chart, It is evident that immunization doesnt bring frequent illness(due to antibodies injected), it just keeps children more safe.
It can also be interpreted like may be because of other chronic illness from birth, some children were not vaccinated at all.

2.more than birth weight, current weight of child depends on breastfeeding duration.
3.higher parity is always associated with lesser child health.
4.maternal age and child health outcomes are having weak positive correlation.
5.no severe multicollinearity between any two columns(>0.8)

---Note: Run until line 182 in Module1.py file, below line num 182, all are done for my own undertanding and practice(not mentioned in Q1 tasks of capstone)
