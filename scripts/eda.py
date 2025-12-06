# eda.py
# author: Gloria Yi
# date: 2025-12-05
# code reference: https://github.com/ttimbers/breast-cancer-predictor/blob/2.0.0/scripts/eda.py

import os
import click
import altair as alt
import pandas as pd


FEATURE_COLS = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]


@click.command()
@click.option(
    "--processed-training-data",
    type=str,
    required=True,
    help="Path to processed maternal health training data (CSV).",
)
@click.option(
    "--plot-to",
    type=str,
    required=True,
    help="Path to directory where the EDA plots will be written to.",
)
def main(processed_training_data, plot_to):
    """
    Create EDA plots for the maternal health training data:

    1. Correlation heatmap between numeric features.
    2. Density plots of each feature, faceted by feature and colored by RiskLevel.

    All plots are saved to the directory given by --plot-to.
    """

    train_df = pd.read_csv(processed_training_data)

    corr_matrix = train_df[FEATURE_COLS].corr()
    corr_long = corr_matrix.reset_index().melt(id_vars="index")
    corr_long.columns = ["Feature 1", "Feature 2", "Correlation"]

    # visualize correlation heatmap
    corr_plot = (
        alt.Chart(corr_long)
        .mark_rect()
        .encode(
            x=alt.X("Feature 1:O", sort=FEATURE_COLS),
            y=alt.Y("Feature 2:O", sort=FEATURE_COLS),
            color=alt.Color("Correlation:Q", scale=alt.Scale(scheme="viridis")),
            tooltip=[
                "Feature 1",
                "Feature 2",
                alt.Tooltip("Correlation:Q", format=".2f"),
            ],
        )
        .properties(
            width=300,
            height=300,
            title="Correlation heatmap of maternal health features",
        )
    )

    corr_plot.save(
        os.path.join(plot_to, "correlation_heatmap.png"), scale_factor=2.0
    )

    mh_train_melted = train_df.melt(
        id_vars=["RiskLevel"],
        value_vars=FEATURE_COLS,
        var_name="feature",
        value_name="value",
    )

    mh_train_melted["feature"] = (
        mh_train_melted["feature"]
        .str.replace("BP", " BP")  
    )

    # visualize feature distributions by risk level
    dist_plot = (
        alt.Chart(mh_train_melted, width=150, height=100)
        .transform_density(
            "value",
            groupby=["RiskLevel", "feature"],
        )
        .mark_area(opacity=0.7)
        .encode(
            x="value:Q",
            y=alt.Y("density:Q", stack=False),
            color="RiskLevel:N",
        )
        .facet(
            "feature:N",
            columns=3,
        )
        .resolve_scale(y="independent")
        .properties(title="Feature distributions by maternal risk level")
    )

    dist_plot.save(
        os.path.join(plot_to, "feature_densities_by_risklevel.png"), scale_factor=2.0
    )


if __name__ == "__main__":
    main()
