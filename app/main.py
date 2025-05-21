import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

from utils import load_data

df = load_data()

st.title("Cross-Country Solar Irradiance Comparison")
st.markdown("Compare GHI, DNI, and DHI across Benin, Sierra Leone, and Togo.")

# Sidebar options
country_options = st.sidebar.multiselect(
    "Select Countries",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

metric = st.sidebar.selectbox("Select Metric", options=['GHI', 'DNI', 'DHI'])

filtered_df = df[df['Country'].isin(country_options)]

# Summary statistics
st.subheader("Summary Statistics")
st.dataframe(
    filtered_df.groupby('Country')[[metric]].agg(['mean', 'median', 'std']).round(2)
)

# Boxplot
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x='Country', y=metric, hue='Country', dodge=False)
st.pyplot(fig)

# Bar plot of average metric
st.subheader(f"Average {metric} by Country")
avg_metric = filtered_df.groupby('Country')[metric].mean().sort_values(ascending=False)
st.bar_chart(avg_metric)

# ANOVA test
if len(country_options) >= 2:
    st.subheader("ANOVA Test")
    group_values = [filtered_df[filtered_df['Country'] == c][metric] for c in country_options]
    f_stat, p_value = f_oneway(*group_values)
    st.write(f"F-statistic: {f_stat:.2f}")
    st.write(f"P-value: {p_value:.4f}")
    if p_value < 0.05:
        st.success("Significant difference detected (p < 0.05).")
    else:
        st.info("No significant difference detected.")
else:
    st.info("Select at least 2 countries to run ANOVA.")
