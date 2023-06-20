# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Saikat Guria\Desktop\Python training\Project\Employee salary\ds_salaries.csv")
df = pd.DataFrame(data)

df.shape
df.columns

df.head()
del df["Unnamed: 0"]
df.info()
df.isnull().sum()
df.describe()

jobs = df.groupby('job_title').size().reset_index().sort_values(by=0,ascending = False)
jobs.head()


#Analysis of job title
plt.figure(figsize = (15,10))
sns.set_style("darkgrid")
sns.barplot(x='job_title',y=0,data = jobs[:10],palette = 'magma')
plt.title('Top Jobs Titles')
plt.xlabel('Job Title')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.show()

#highest earner for all data professions in USD in 2020

higher_earn_20 = df[df.work_year == 2020]
higher_earn_20 = higher_earn_20.groupby(['job_title','experience_level','company_size','company_location']).max()['salary_in_usd'].reset_index()
higher_earn_20=higher_earn_20.sort_values('salary_in_usd',ascending=False).head(10)
higher_earn_20


higher_earn_20.plot(kind='bar',x='job_title',y='salary_in_usd',
              title='Top 10 earners in 2020',
              figsize=(15,6))
plt.xticks(rotation=45)
plt.show()

#highest earner for all data professions in USD in 2021

higher_earn_21 = df[df.work_year == 2021]
higher_earn_21 = higher_earn_21.groupby(['job_title','experience_level','company_size','company_location']).max()['salary_in_usd'].reset_index()
higher_earn_21=higher_earn_21.sort_values('salary_in_usd',ascending=False).head(10)
higher_earn_21


higher_earn_21.plot(kind='bar',x='job_title',y='salary_in_usd',
              title='Top 10 earners in 2021',
              figsize=(15,6))
plt.xticks(rotation=45)
plt.show()

#highest earner for all data professions in USD in 2022

higher_earn_22 = df[df.work_year == 2022]
higher_earn_22 = higher_earn_22.groupby(['job_title','experience_level','company_size','company_location']).max()['salary_in_usd'].reset_index()
higher_earn_22=higher_earn_22.sort_values('salary_in_usd',ascending=False).head(10)
higher_earn_22

higher_earn_22.plot(kind='bar',x='job_title',y='salary_in_usd',
              title='Top 10 earners in 2022',
              figsize=(15,6))
plt.xticks(rotation=45)
plt.show()

#comparing experience level
df.experience_level.unique()

plt.figure(figsize = (15,10))
sns.catplot(x='experience_level',data = df,kind = 'count',palette = 'magma')
plt.show()

levels = df.experience_level.value_counts()
levels


#average earning per job title`

avg_earn=data.groupby('job_title').mean()['salary_in_usd'].reset_index()
avg_earn=avg_earn.sort_values('salary_in_usd',ascending=False).head(10)
avg_earn

avg_earn.plot(kind='bar',x='job_title',y='salary_in_usd',title='Average earning per job title',figsize=(15,8))

#average pay of job titles per region
#starting with the US:
    
payus=data[data.company_location=='US']
payus=payus.groupby('job_title').mean()['salary_in_usd'].reset_index()
payus=payus.sort_values('salary_in_usd',ascending=False).head(10)
payus

#comparing these values with the rest of the regions on the dataset
payout=data[data.company_location!='US']
payout=payout.groupby('job_title').mean()['salary_in_usd'].reset_index()
payout=payout.sort_values('salary_in_usd',ascending=False).head(10)
payout

compare = pd.merge(payus,payout[['job_title','salary_in_usd']],on='job_title', how='left').dropna().head(10)
compare

compare.plot(kind='bar',figsize=(15,8),x='job_title',title='Comparison of average pay per job title for US companies to other parts')
plt.xticks(rotation=45)

#average pay by company size in the US
compsizeUS=data[data.company_location=='US']
compsizeUS=compsizeUS.groupby('company_size').mean()['salary_in_usd'].reset_index()
compsizeUS=compsizeUS.sort_values('salary_in_usd',ascending=False)
compsizeUS

#average pay by company size outside the US
compsizeNOTUS=data[data.company_location!='US']
compsizeNOTUS=compsizeNOTUS.groupby('company_size').mean()['salary_in_usd'].reset_index()
compsizeNOTUS=compsizeNOTUS.sort_values('salary_in_usd',ascending=False)
compsizeNOTUS

sizecomp = pd.merge(compsizeUS,compsizeNOTUS[['company_size','salary_in_usd']],on='company_size', how='left')
sizecomp

sizecomp.plot(kind='bar',figsize=(15,8),x='company_size',title='salary_in_usd')


#employment type

df.employment_type.unique()
emp_type = df.employment_type.value_counts()
emp_type

plt.figure(figsize = (15,10))
sns.catplot(x='employment_type',data = df,kind = 'count',palette = 'magma')
plt.xlabel('Employement type')
plt.show()

