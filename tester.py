import altair as alt
import pandas as pd

data = pd.DataFrame({'name': ['a', 'b'], 'value': [4, 10]})

alt.Chart(data).mark_bar(size=10).encode(
    x='name:O',
    y='value:Q'
)
