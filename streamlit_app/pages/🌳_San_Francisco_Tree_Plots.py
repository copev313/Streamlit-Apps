"""
    San Francisco Tree Plots page -- displays a variety of charts and graphs
    available in Streamlit.
"""
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Streamlit App: Tree Plots",
    page_icon="🌳",
    layout="wide",
)

st.title("🌳 San Francisco Trees")
st.write(
    "This demo analyzes San Francisco's tree data provided by the SF DPW."
)


@st.experimental_memo
def get_data(filename: str):
    trees_df = pd.read_csv(
        "https://raw.githubusercontent.com/tylerjrichards/"
        f"Streamlit-for-Data-Science//main/trees_app/{filename}"
    )
    return trees_df


def main_tree_page():
    trees_df = get_data("trees.csv")
    st.subheader("Streamlit Charts")
    df_dbh_grouped = pd.DataFrame(
        trees_df.groupby("dbh").count()["tree_id"]
    )

    df_dbh_grouped.columns = ["tree_count"]

    # Display a variety of Streamlit native graphs:
    st.line_chart(df_dbh_grouped)
    st.bar_chart(df_dbh_grouped)
    st.area_chart(df_dbh_grouped)

    trees_df.dropna(
        subset=["longitude", "latitude"],
        inplace=True
    )
    st.map(trees_df.sample(n=1000))


def altair_tree_page():
    import altair as alt

    trees_df = get_data("trees.csv")
    st.subheader("Altair Charts")
    # Create a DF for Caretakers:
    caretakers_df = trees_df.groupby(["caretaker"]).count()["tree_id"]\
                                                    .reset_index()

    caretakers_df.columns = ["caretaker", "tree_count"]
    fig = alt.Chart(caretakers_df).mark_bar().encode(
        x="caretaker",
        y="tree_count"
    )

    # Display the chart:
    st.altair_chart(fig, use_container_width=True)
    # Display the raw data:
    fig_b = alt.Chart(trees_df).mark_point().encode(
        x="caretaker",
        y="count(*):Q"
    )
    st.altair_chart(fig_b, use_container_width=True)


def bokeh_tree_page():
    from bokeh.plotting import figure

    trees_df = get_data("trees.csv")
    st.subheader("Bokeh Chart")

    # Create Bokeh scatterplot:
    scatterplot = figure(title="Scatterplot")
    scatterplot.scatter(trees_df["dbh"], trees_df["site_order"])
    # Label the axes:
    scatterplot.xaxis.axis_label = "DBH"
    scatterplot.yaxis.axis_label = "Site Order"
    # Display the plot:
    st.bokeh_chart(scatterplot)

# ----------------------------------------------------------------------------

# Map each demo's logic to a dropdown option:
page_names_to_funcs = {
    "Streamlit Built-in Data Viz": main_tree_page,
    "Altair Plot": altair_tree_page,
    "Bokeh Plot": bokeh_tree_page,
    # "DataFrame Demo": data_frame_demo
}

# Display a dropdown menu in the sidebar:
demo_name = st.sidebar.selectbox(
    label="Choose Data Visualization: ",
    options=page_names_to_funcs.keys()
)
# Run page's logic:
page_names_to_funcs[demo_name]()
