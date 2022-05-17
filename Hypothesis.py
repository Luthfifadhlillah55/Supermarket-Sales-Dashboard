import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    def get_data():
    
        return pd.read_csv('supermarket_sales_Dataclean.csv')
    df= get_data()
    df 

    data1 = df[["City", "Gross Income"]]
    data1

    
    st.title("Hypothesis Testing & Analysis")
    if st.checkbox('Show Data'):
        st.subheader('100 Sample of Data')
        st.write(df.head(100))
    
    st.subheader("1. Methodology")
    st.write("The chosen statistical testing for this analysis is ANOVA (Analysis of Variance) due to the purpose of this analysis which is to compare the gross income of each store branch. ANOVA is chosen because we have multiple categories of a categorical variable and a continuous variable. Asymmetrical distributions like the F and chi-square distributions have only one tail. This means that analyses such as ANOVA and chi-square tests do not have a “one-tailed vs. two-tailed” option, because the distributions they are based on have only one tail.")
    st.write("α = 0.05")
    st.write("H0: There are no significant differences between the average gross income amongst 3 store branches.") 
    st.write("H1: There are significant differences between the average gross income of 3 branches.")
    st.write("In this case, I want to know whether the Gross Income of each city differs significantly or not.")
    ax = data1.boxplot(by="City", column="Gross Income", figsize=(10, 7))
    ax.set_xlabel("City")
    ax.set_ylabel("Gross Income")
    plt.suptitle('')
    plt.title('Comparison Gross Income of 3 City')
    plt.tight_layout()
    st.pyplot()

    Yangon_grossincome = df[df.City == 'Yangon'].groupby('Date').sum()['Gross Income']
    Naypyitaw_grossincome = df[df.City == 'Naypyitaw'].groupby('Date').sum()['Gross Income']
    Mandalay_grossincome = df[df.City == 'Mandalay'].groupby('Date').sum()['Gross Income']

    st.subheader("2. Gross Income Average of 3 Cities")
    st.write("Gross Income Average of Yangon",Yangon_grossincome.mean())
    st.write("Gross Income Average of Naypyitaw",Naypyitaw_grossincome.mean())
    st.write("Gross Income Average of Mandalay",Mandalay_grossincome.mean())

    st.write("By using the ANOVA method, we can find out the average Gross Income of each city. Based on the average value of gross income for each city, there is a small gap, but can this be said to be insignificant? Let's check through p-value calculations.")

    st.subheader("3. Calculate P-Value")
    f_stat,p_value = stats.f_oneway(Yangon_grossincome, Naypyitaw_grossincome, Mandalay_grossincome)
    st.write('P-value:',p_value)
    st.write('F-Status:', f_stat)

    st.subheader("4. Conclusion")
    st.write("The P-Value based on the calcualtion is 0.867487447683447, this value is bigger than 0.05. Then we can conclude that the difference of gross income from Yangon,Naypyitaw and Mandalay is statistically not significant. Which means, H0 is accepted and H1 is rejected")

