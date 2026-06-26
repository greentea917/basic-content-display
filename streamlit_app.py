import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# Formatting with Markdown
st.write("**Boston college**: *Data Visualization and Storytelling*")  

# Display an image
st.write(Image.open('bc.jpg'))

# Display a DataFrame
st.write(cars) 

# Display an interactive chart
st.write(alt.Chart(cars).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive())
