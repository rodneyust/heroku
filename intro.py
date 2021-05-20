# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:57:37 2021

@author: myhom
"""

import streamlit as st
import streamlit.components.v1 as components


def write():
    
    st.header("The Rent in Santa Clara County")
    st.subheader("**Introduction**")
    #income1,immi1=st.beta_columns(2)
    st.markdown("Economy Part")
    income ="""https://datausa.io/profile/geo/santa-clara-county-ca/economy/income?viz=true"""
    components.iframe(income,width=1000,height=500,scrolling=True)
    #income1 = components.iframe(income,width=300,height=120,scrolling=True)
    st.markdown("Here we can see the foreign population has a huge percent in Santa Clara County compared to the other places in US")
    immi = """https://datausa.io/profile/geo/santa-clara-county-ca/demographics/foreign_born?viz=true"""
    components.iframe(immi,width=1000,height=500,scrolling=True)
    #immi1 = components.iframe(immi,width=300,height=120,scrolling=True)
    #income1,immi1=st.beta_columns(2)
    propertyvalue = """https://datausa.io/profile/geo/santa-clara-county-ca/housing/property_value?viz=true"""
    components.iframe(propertyvalue,width=1000,height=2500,scrolling=True)
    pv="https://datausa.io/profile/geo/santa-clara-county-ca/housing/household_income?viz=true" 
    components.iframe(pv,1000,500,True)
    rentvsown = "https://datausa.io/profile/geo/santa-clara-county-ca/housing/rent_own?viz=true"
    components.iframe(rentvsown,width=1000,height=500,scrolling=True)
    
    #html_temp = """<div class='tableauPlaceholder' id='viz1620738274887' style='position: relative'><noscript><a href='https:&#47;&#47;www.linkedin.com&#47;in&#47;obyali&#47;'><img alt='Santa Clara County Home Market@Oby Ali Real Estate Services 415-608-1859 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SantaClaraCountyMapPrices&#47;Sheet2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SantaClaraCountyMapPrices&#47;Sheet2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SantaClaraCountyMapPrices&#47;Sheet2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-Hans' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620738274887');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    #components.html(html_temp,1000,500,scrolling=True)
    temp2 = """<div class='tableauPlaceholder' id='viz1620738379905' style='position: relative'><noscript><a href='#'><img alt='Santa Clara County ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;BT&#47;BTM39PF2D&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;BTM39PF2D' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;BT&#47;BTM39PF2D&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-Hans' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620738379905');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1366px';vizElement.style.height='795px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(temp2,width=1000,height=500,scrolling=True)
    temp3 = "<div class='tableauPlaceholder' id='viz1620858690143' style='position: relative'><noscript><a href='https:&#47;&#47;www.linkedin.com&#47;in&#47;obyali&#47;'><img alt='Santa Clara County Home Market@Oby Ali Real Estate Services 415-608-1859 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SantaClaraCountyMapPrices&#47;Sheet2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SantaClaraCountyMapPrices&#47;Sheet2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SantaClaraCountyMapPrices&#47;Sheet2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-Hans' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620858690143');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(temp3,1000,500,True)
    temp4 = "<div class='tableauPlaceholder' id='viz1620858756097' style='position: relative'><noscript><a href='#'><img alt='Airbnb Listing Analysis 2008 -2018 Santa Clara County Dataset from Inside Airbnb ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Z4&#47;Z43SFQNQ6&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;Z43SFQNQ6' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Z4&#47;Z43SFQNQ6&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-Hans' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620858756097');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(temp4,1000,500,True)
    
    
    #rent = "https://opengov.civicdashboards.com/embed/c13b26"
    #components.iframe(rent,1000,500,True)


    
