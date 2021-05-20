# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:06:24 2021

@author: myhom
"""

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
def write():
    
    st.header("The Rent Comparison")
    #st.subheader("**Introduction**")
    #income ="<div class='tableauPlaceholder' id='viz1619951865647' style='position: relative'><noscript><a href='#'><img alt='仪表板 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ph&#47;Phoenixdata&#47;1_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Phoenixdata&#47;1_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ph&#47;Phoenixdata&#47;1_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-Hans' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1619951865647');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    #components.html(income,width=1000,height=500,scrolling=True)
    st.title("Review from the Airbnb")
    
    col1, col2 = st.beta_columns(2)

    #original = Image.open(r"C:\Users\myhom\Desktop\下载.png")
    #col1.header("Santa Clara")
    #col1.image(original, use_column_width=True)

   # grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin.png")
    #col2.header("Austin")
    #col2.image(grayscale, use_column_width=True)
    
    col3,col4 = st.beta_columns(2)
    
    original = Image.open(r"C:\Users\myhom\Desktop\下载 (1).png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin2.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    
    col5,col6 = st.beta_columns(2)
    original = Image.open(r"C:\Users\myhom\Desktop\下载3.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)
    st.markdown("The room type in two places & The price distribution")
    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin3.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.title("How many bedrooms in your room?")
    col7, col8 = st.beta_columns(2)

    original = Image.open(r"C:\Users\myhom\Desktop\下载4.png")
    col7.header("Santa Clara")
    col7.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin4.png")
    col8.header("Austin")
    col8.image(grayscale, use_column_width=True)
    st.markdown("It seems that the Santa Clara has less bedrooms than Austin")
    st.title("Added Listing")
    col1, col2 = st.beta_columns(2)

    original = Image.open(r"C:\Users\myhom\Desktop\下载7.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin7.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    col1, col2 = st.beta_columns(2)

    original = Image.open(r"C:\Users\myhom\Desktop\下载8.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin8.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown('Which month has the most listings in Santa Clara and Austin?')
    st.markdown("Summer is both Santa CLara and Austin's peak season")
    col1, col2 = st.beta_columns(2)

    original = Image.open(r"C:\Users\myhom\Desktop\下载9.png")
    col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin9.png")
    col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown('Estimated supply as well as the demand in two places')
    st.markdown("Austin has more demands")
    col1, col2 = st.beta_columns(2)

    original = Image.open(r"C:\Users\myhom\Desktop\下载10.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin10.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown("review number per month")
    col1, col2 = st.beta_columns(2)
    original = Image.open(r"C:\Users\myhom\Desktop\下载11.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin11.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown("Average nightly rent trends")
    col1, col2 = st.beta_columns(2)
    original = Image.open(r"C:\Users\myhom\Desktop\下载12.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin12.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.markdown("Projected Inflation in 2021 in USA - 2.24%")
    st.markdown("Mean Price Increase YoY in Santa Clara -  9.26503 %")
    st.markdown("Mean Price Increase YoY in Austin -  37.20839 %")
    st.header("Review Analysis")
    original = Image.open(r"C:\Users\myhom\Desktop\下载13.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin13.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    
    original = Image.open(r"C:\Users\myhom\Desktop\下载14.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin14.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    
    original = Image.open(r"C:\Users\myhom\Desktop\下载17.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\Austin17.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    st.title("Predicting sentiment from traveller reviews")
    st.markdown("")
    st.markdown("We expore logistic regression and feature engineering to achieve it")
    st.markdown("Now, we will assign comments with a rating higher than 25 percentile to be positive reviews, while the ones with rating lower than 25 percentile are negative. For the sentiment column, we use +1 for the positive class label and -1 for the negative class label. A good way is to create an anonymous function that converts a rating into a class label and then apply that function to every element in the rating column.")
    st.markdown("Let's perform a train/test split with 80% of the data in the training set and 20% of the data in the test set.")
    st.header("Train a sentiment classifier with logistic regression")
    col1,col2 = st.beta_columns(2)
    original = Image.open(r"C:\Users\myhom\Desktop\1.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\2.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)
    
    st.markdown("Here we can see the our model perform pretty well")
    st.title("Making predictions with logistic Regression")
    st.markdown("")
    st.markdown("We test our model on our samples,then compute the classifier accuracy")
    st.markdown("We will now evaluate the accuracy of the trained classifier.")
    #st.markdown('$$\mbox{accuracy} = \frac{\mbox{# correctly classified examples}}{\mbox{# total examples}}$$')

    st.markdown('This can be computed as follows:')

    st.markdown('* **Step 1:** Use the trained model to compute class predictions (**Hint:** Use the `predict` method)')
    st.markdown( '* **Step 2:** Count the number of data points when the predicted class labels match the ground truth labels (called `true_labels` below).')
    st.markdown('* **Step 3:** Divide the total number of correct predictions by the total number of data points in the dataset.')

    st.markdown('Complete the function below to compute the classification accuracy:")')
    #st.markdown("Let us inspect the weights (coefficients) of the simple_model. First, build a table to store (word, coefficient) pairs.")
    st.markdown("Sort the data frame by the coefficient value in descending order.")
    col11,col12= st.beta_columns(2)
    original = Image.open(r"C:\Users\myhom\Desktop\3.png")
    col11.header("Santa Clara")
    col11.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\4.png")
    col12.header("Austin")
    col12.image(grayscale, use_column_width=True)
    
    col1,col2= st.beta_columns(2)
    original = Image.open(r"C:\Users\myhom\Desktop\7.png")
    #col1.header("Santa Clara")
    col1.image(original, use_column_width=True)

    grayscale = Image.open(r"C:\Users\myhom\Desktop\8.png")
    #col2.header("Austin")
    col2.image(grayscale, use_column_width=True)