
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

def kpi3(literacy_df):
    literacy_df.loc[:, "Country/ States/ Union Territories Name"] = literacy_df[
    "Country/ States/ Union Territories Name"
].replace(state_name_mapping)
    literacy_df = literacy_df[
        literacy_df["Country/ States/ Union Territories Name"] != "INDIA"
    ]

    print(literacy_df["Country/ States/ Union Territories Name"].unique())
    # Step 1: Calculate total crimes for 2001 and 2011
    crimes_2001 = df[df["Year"] == 2001].groupby("STATE/UT")["Total crimes"].sum().reset_index()
    crimes_2011 = df[df["Year"] == 2011].groupby("STATE/UT")["Total crimes"].sum().reset_index()

    # Rename columns for clarity
    crimes_2001.rename(columns={"Total crimes": "Total crimes 2001"}, inplace=True)
    crimes_2011.rename(columns={"Total crimes": "Total crimes 2011"}, inplace=True)

    # Step 2: Prepare literacy df
    literacy_df = {
        "STATE/UT": literacy_df["Country/ States/ Union Territories Name"],
        "LR-2011": literacy_df["Literacy Rate (Persons) - Total - 2011"],
        "LR-2001": literacy_df["Literacy Rate (Persons) - Total - 2001"],
    }

    literacy_df = pd.dfFrame(literacy_df)

    # Step 3: Merge literacy df with crime df
    merged_df = pd.merge(literacy_df, crimes_2001, on="STATE/UT", how="left")
    merged_df = pd.merge(merged_df, crimes_2011, on="STATE/UT", how="left")

    # Step 4: Display the final dfFrame
    merged_df
    # Calculate correlations for 2001 and 2011
    correlation_2001 = merged_df["LR-2001"].corr(merged_df["Total crimes 2001"])
    correlation_2011 = merged_df["LR-2011"].corr(merged_df["Total crimes 2011"])

    # Display the results
    print("Correlation between Literacy Rate (2001) and Total crimes (2001):", correlation_2001)
    print("Correlation between Literacy Rate (2011) and Total crimes (2011):", correlation_2011)
  

    # Create scatter plots with regression lines for 2001 and 2011
    # 2001
    fig_2001 = px.scatter(merged_df, x="LR-2001", y="Total crimes 2001", 
                        title="Literacy Rate vs Total Crimes (2001)",
                        labels={"LR-2001": "Literacy Rate (2001)", "Total crimes 2001": "Total Crimes (2001)"})

    # Fit a linear regression model for 2001
    model_2001 = LinearRegression()
    model_2001.fit(merged_df[["LR-2001"]], merged_df["Total crimes 2001"])
    line_x_2001 = np.linspace(merged_df["LR-2001"].min(), merged_df["LR-2001"].max(), 100).reshape(-1, 1)
    line_y_2001 = model_2001.predict(line_x_2001)

    # Add the regression line to the figure
    fig_2001.add_trace(go.Scatter(x=line_x_2001.flatten(), y=line_y_2001, mode='lines', name='Regression Line', line=dict(color='red')))

    # 2011
    fig_2011 = px.scatter(merged_df, x="LR-2011", y="Total crimes 2011", 
                        title="Literacy Rate vs Total Crimes (2011)",
                        labels={"LR-2011": "Literacy Rate (2011)", "Total crimes 2011": "Total Crimes (2011)"})

    # Fit a linear regression model for 2011
    model_2011 = LinearRegression()
    model_2011.fit(merged_df[["LR-2011"]], merged_df["Total crimes 2011"])
    line_x_2011 = np.linspace(merged_df["LR-2011"].min(), merged_df["LR-2011"].max(), 100).reshape(-1, 1)
    line_y_2011 = model_2011.predict(line_x_2011)

    # Add the regression line to the figure
    fig_2011.add_trace(go.Scatter(x=line_x_2011.flatten(), y=line_y_2011, mode='lines', name='Regression Line', line=dict(color='red')))

    # Show the plots
    fig_2001.show()
    fig_2011.show()



state_name_mapping = {
    "Andhra Pradesh": "ANDHRA PRADESH",
    "Arunachal Pradesh": "ARUNACHAL PRADESH",
    "Assam": "ASSAM",
    "Bihar": "BIHAR",
    "Chhattisgarh": "CHHATTISGARH",
    "Goa": "GOA",
    "Gujarat": "GUJARAT",
    "Haryana": "HARYANA",
    "Himachal Pradesh": "HIMACHAL PRADESH",
    "Jammu & Kashmir": "JAMMU & KASHMIR",
    "Jharkhand": "JHARKHAND",
    "Karnataka": "KARNATAKA",
    "Kerala": "KERALA",
    "Madhya Pradesh": "MADHYA PRADESH",
    "Maharashtra": "MAHARASHTRA",
    "Manipur": "MANIPUR",
    "Meghalaya": "MEGHALAYA",
    "Mizoram": "MIZORAM",
    "Nagaland": "NAGALAND",
    "Odisha": "ODISHA",
    "Punjab": "PUNJAB",
    "Rajasthan": "RAJASTHAN",
    "Sikkim": "SIKKIM",
    "Tamil Nadu": "TAMIL NADU",
    "Tripura": "TRIPURA",
    "Uttar Pradesh": "UTTAR PRADESH",
    "Uttarakhand": "UTTARAKHAND",
    "West Bengal": "WEST BENGAL",
    "A & N Islands": "A & N ISLANDS",
    "Chandigarh": "CHANDIGARH",
    "D & N Haveli": "D & N HAVELI",
    "Daman & Diu": "DAMAN & DIU",
    "Lakshadweep": "LAKSHADWEEP",
    "NCT of Delhi": "DELHI",
    "Puducherry": "PUDUCHERRY",
}

