"""
    The home page of the Streamlit app.
"""
import streamlit as st

st.set_page_config(
    page_title="Streamlit App: Home",
    page_icon="🏠",
    layout="wide",
)

st.header("🏠 Welcome!")
st.subheader("Home Page")

st.markdown("""
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.

    **👈 Select a demo from the sidebar on the left** to see some examples
    of what Streamlit can do!

    ### Want to learn more?

    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community forums](https://discuss.streamlit.io)

    ### See more complex demos

    - Use a neural net to [analyze the Udacity Self-driving Car Image Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
""")
