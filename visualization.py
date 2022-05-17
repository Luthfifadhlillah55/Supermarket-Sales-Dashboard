import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

def app():
    def get_data():
    
        return pd.read_csv('supermarket_sales_Dataclean.csv')
    df= get_data()
    df 

    st.title("Data Visualization")
    st.write("Before looking at the data, please provide information about your age.")
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

    st.title("Main Board For Observation")
    pilihan = st.radio(
     "What kind of data visualization do you want to observe?",
     ('Sales from Different Cities', 'Customer Type by Gender', 'Most Products Purchased', 'COGS (Cost of Goods Sold)', 'Types of payments'))
    if pilihan == 'Sales from Different Cities':
     st.subheader("Percentage of Sales from Different Cities")
     plt.figure(figsize = (16,9))
     City = df.City.value_counts().reset_index()
     plt.pie(City.City, labels = City['index'],autopct='%1.1f%%')
     plt.title("Sales From Different Cities")
     st.pyplot()
    elif pilihan == 'Customer Type by Gender':
     plt.figure(figsize = (16,9))
     Gd = df.Gender.value_counts().reset_index()
     plt.pie(Gd.Gender, labels = Gd['index'],autopct='%1.1f%%')
     plt.title("Sales From Different Genders")
     st.pyplot()
    elif pilihan == 'Most Products Purchased':
     plt.figure(figsize = (20,10))
     Product = df.groupby('Product Category').size().to_frame(name = "count").reset_index()
     sns.barplot(y = 'count', x='Product Category', data = Product )
     plt.title("Sales of Different Kinds of Products")
     plt.xlabel("Product Category")
     plt.ylabel("Count")
     st.pyplot()
     st.write("Fashion accessories are the most purchased products, while Health & Beauty is the lowest in terms of sales.")
    elif pilihan == 'COGS (Cost of Goods Sold)':
     df['Date'] = df['Date'].astype('datetime64[ns]')
     sorted_data = df.sort_values(by='Date',ascending=True).groupby('Date').sum()
     fig, axes = plt.subplots()
     sorted_data = sorted_data['COGS'].plot(kind='line',ax=axes)
     st.pyplot()
     st.write("There were fluctuations for the COGS value in the period January 2019 to March 2019. In the middle of the month there was always a decrease which would then increase at the end of the month.")
    else:
     plt.figure(figsize = (16,9))
     sns.countplot(y ='Gender', hue = "Payment", data = df) 
     plt.xlabel('Count')
     plt.ylabel('Gender')
     st.pyplot()
     st.write("The data shows that female customers prefer to use the cash payment method, while male customers prefer to use e-wallet.")

    st.subheader("Overall of Data Visualization")
    st.subheader("1. Percentage of Sales from Different Cities")
    plt.figure(figsize = (16,9))
    City = df.City.value_counts().reset_index()
    plt.pie(City.City, labels = City['index'],autopct='%1.1f%%')
    plt.title("Sales From Different Cities")
    st.pyplot()
    Cit = st.radio(
     "Select Data",
     ('Yangon', 'Mandalay', 'Naypyitaw'))
    if Cit == 'Yangon':
        st.write("Percentage of Sales of Yangon is 34%.")
    elif Cit == 'Mandalay':
        st.write("Percentage of Sales of Mandalay is 33.2%.")
    else:
        st.write("Percentage of Sales of Naypyitaw is 32.8%.")
    st.write("A branch is generating most number of sales is Yangon. The least is generated by Naypyitaw branch. The use of Pie Chart aims to make it easier to see which city dominates in percentage terms.")

    st.subheader("2. Customer Type by Gender")
    plt.figure(figsize = (16,9))
    Gd = df.Gender.value_counts().reset_index()
    plt.pie(Gd.Gender, labels = Gd['index'],autopct='%1.1f%%')
    plt.title("Sales From Different Genders")
    st.pyplot()
    Gen = st.radio(
     "Select Data",
     ('Male', 'Female'))
    if Gen == 'Male':
        st.write("Percentage of Sales by Male is 50.1%")
    else:
        st.write("Percentage of Sales by Female is 49.9%.")
    st.write("We can also find out the comparison between male customers and female customers using the gender column. In fact, men and women are almost equal, even though the current stigma says that women prefer shopping than men.")

    st.subheader("3. The Most Products Purchased")
    plt.figure(figsize = (20,10))
    Product = df.groupby('Product Category').size().to_frame(name = "count").reset_index()
    sns.barplot(y = 'count', x='Product Category', data = Product )
    plt.title("Sales of Different Kinds of Products")
    plt.xlabel("Product Category")
    plt.ylabel("Count")
    st.pyplot()
    st.write("Fashion accessories are the most purchased products, while Health & Beauty is the lowest in terms of sales.")

    st.subheader("4. Total COGS (Cost of Goods Sold) Value in 3 Months")
    df['Date'] = df['Date'].astype('datetime64[ns]')
    sorted_data = df.sort_values(by='Date',ascending=True).groupby('Date').sum()
    fig, axes = plt.subplots()
    sorted_data = sorted_data['COGS'].plot(kind='line',ax=axes)
    st.pyplot()
    st.write("There were fluctuations for the COGS value in the period January 2019 to March 2019. In the middle of the month there was always a decrease which would then increase at the end of the month.")

    st.subheader("5. Types of payments by gender")
    plt.figure(figsize = (16,9))
    sns.countplot(y ='Gender', hue = "Payment", data = df) 
    plt.xlabel('Count')
    plt.ylabel('Gender')
    st.pyplot()
    st.write("The data shows that female customers prefer to use the cash payment method, while male customers prefer to use e-wallet.")

 
    


