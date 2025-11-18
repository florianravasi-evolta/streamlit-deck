# plots.py
import plotly.graph_objects as go

def make_price_vs_dispatch_figure(df_prices, df_dispatch, title: str = "Example day"):
    fig = go.Figure()
    fig.add_scatter(
        x=df_prices["datetime"],
        y=df_prices["price"],
        name="RTM price",
        mode="lines",
    )
    fig.add_scatter(
        x=df_dispatch["datetime"],
        y=df_dispatch["discharge_mw"],
        name="Battery discharge (MW)",
        mode="lines",
        yaxis="y2",
    )
    fig.update_layout(
        title=title,
        xaxis_title="Time",
        yaxis_title="Price [$]",
        yaxis2=dict(
            title="Discharge [MW]",
            overlaying="y",
            side="right",
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig