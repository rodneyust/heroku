# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:40:54 2021

@author: myhom
"""

import streamlit as st
import awesome_streamlit as ast
import intro1
import intro
import status
import status1
import conclusion

PAGES = {
    "Introduction-Santa Clara County": intro,
    "Introduction-Austin":intro1,
    "Rent Market Analysis":status,
    "Property Market Analysis":status1,
    "Conclusion": conclusion
    #"Gallery": src.pages.gallery.index,
    #"Vision": src.pages.vision,
    #"About": src.pages.about,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
if __name__ == "__main__":    
    main()