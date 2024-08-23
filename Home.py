import streamlit as st

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="🤖",
)

st.markdown(
    """
# Hello!
            
Welcome to my FullstackGPT Portfolio!
            
Here are the apps I made:
            
- [ ] [DocumentGPT](/DocumentGPT)
- [ ] [PrivateGPT](/PrivateGPT)
- [ ] [QuizGPT](/QuizGPT)
- [ ] [SiteGPT](/SiteGPT)
- [ ] [MeetingGPT](/MeetingGPT)
- [ ] [InvestorGPT](/InvestorGPT)
"""
)


with st.sidebar:
    st.title("About")
    st.text_input("Your name", "Type Here ...")


tab_one, tab_two, tab_three = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab_one:
    st.write("This is the first tab")

with tab_two:
    st.write("This is the second tab")

with tab_three:
    st.write("This is the third tab")
