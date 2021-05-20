# -*- coding: utf-8 -*-
"""
Created on Thu May 20 07:11:32 2021

@author: myhom
"""

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
def write():
    
    st.header("The Property Comparison")
    st.markdown("First we download the data from the Redfin or Zillow, then we have a overview for our data")
    st.subheader("Multiple")
    st.markdown("Multiple is a ratio which indicates that a place should rent or buy. So it is also called price-to-rent ratio.")
    st.markdown("It is calculated by price divide by revenue---price divide by (occupancy times 365 times Daily Rate)")
    st.markdown("If it is 1 to 15 indicates much better to buy than rent")
    st.markdown("If it is 16 to 20 indicates typically better to rent than buy")
    st.markdown("If it is bigger than 21 indicates it is much better to rent than buy")
    col1,col2 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\san1.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au1.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown("We can see that in Santa Clara County there are places that better to rent, well, on the contrary, in Austin more places is better to buy")
    st.subheader("Daily Rate")
    st.markdown("Average Daily Rate is calculated by dividing the total revenue earned by the host for the entire reservation by the number of booked nights.")
    st.markdown("Here in Santa Clara, Daily Rate ranged from 124 to 543.6; But in Austin, it can range from 171.3 to 918.5 on average.")
    st.subheader("Occupancy")
    st.markdown("Santa Clara's occupancy is ranged from 0.33 to 0.78 on average, it ranged from 0.48 to 0.72 on average in Austin")
    st.subheader("Price")
    col1,col2 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\san2.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au2.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown("On average, the price in Santa Clara is much higher than the price in Austin")
    st.subheader("Dummy variable")    
    st.markdown("In statistics and econometrics, particularly in regression analysis, a dummy variable[a] is one that takes only the value 0 or 1 to indicate the absence or presence of some categorical effect that may be expected to shift the outcome.[2][3] They can be thought of as numeric stand-ins for qualitative facts in a regression model, sorting data into mutually exclusive categories (such as smoker and non-smoker)")
    st.markdown("Here we set the location for dummy variables to see if it can tell us more in geography")
    st.subheader("Data Visualization")
    #col1,col2 = st.beta_columns(2)
    
    original1 = Image.open(r"C:\Users\myhom\Desktop\san3.png")
    st.subheader("Santa Clara")
    st.image(original1, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au3.png")
    st.subheader("Austin")
    st.image(grayscale, use_column_width=True)
    st.markdown("We can find some very interesting conclusion from the chart above. The location Rancho Santa Tersea has a very close relationship with lot size. And the gilroy has a relationship with longtitude.")
    st.subheader("Top Correlated Variables")
    st.markdown("We list the top of them. Definitely, square feet has some relationships with baths!")
    col1,col2 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\san7.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au7.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.subheader("Linear relationship--lmplot")
    st.markdown("Here we use lmplot map to see their linear relationships between variables")
    col1,col2 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\san8.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au8.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.subheader("3D plot")
    st.markdown("Or we can use a 3D scatter plot to see their relationships more clearly")
    col1,col2 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\san9.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au9.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    
    st.title("Build Model")
    st.markdown("So now we need to build different models to test which model is we need to tell the price and predict the price")
    
    st.subheader("Linear Model")
    st.markdown("Here we fit linear model first to see its performance")
    col1,col2 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\san4.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au4.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown("It seems good when working on test data. Let's try other models now!")
    st.markdown("We tried lasso model, ridge model and elastic net model")
    col1,col2 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\san11.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\au11.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown("Finally we can see the result: Santa Clara data should choose elastic net model well Austin data should choose ridge model.")
    