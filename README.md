# **Caste-Based Crime Insights in India**

## **Introduction**  
This project provides a comprehensive platform for analyzing caste-based hate crimes across India. It visualizes crime patterns over the years, highlights correlations, and allows users to explore state-wise and category-wise data through an interactive and user-friendly interface. The platform aims to help identify areas requiring intervention to combat caste-based discrimination effectively.

---

## **Project Type**  
**Fullstack**  

---

## **Deployed App**  
- **Frontend:** [Website](https://crimeinsight.streamlit.app)  
- **Backend:** Not Applicable (handled via Streamlit)  
- **Database:** CSV files used as the primary data source  

---

## **Directory Structure**  
```
project/
├─ data/
│  ├─ crime_by_state_rt.csv
│  ├─ india_literacy_rate.csv
│  ├─ population_of_india.csv
├─ src/
│  ├─ app.py
│  ├─ dashboard_visualization.py (Interactive dashboard enabler code via Streamlit)
|  ├─ kpi_visualization.py (Key Performance Indicators metrics calculation code)
|  ├─ utils.py (Data handeling functions)
```

## Video Walkthrough of the Project
https://drive.google.com/file/d/1UZh5Zq7117zKJ76E_gt26Be-fc3s_QZV/view?usp=sharing

## Video Walkthrough of the Codebase
https://drive.google.com/file/d/1yX5H7YMAGqWXK77g_5EdYLGsRKLS2G7C/view?usp=sharing

## Features
- Dynamic Visualizations: 
Interactive charts, graphs, and heatmaps to analyze crime data effectively.
- Filter and Search Options: 
Advanced filters by year, state, crime category, and literacy rates for tailored insights.
- Comprehensive KPIs Dashboard: 
Key metrics and trends summarized for quick decision-making.


## Design Decisions or Assumptions
The project assumes the use of CSV files as the primary data source, with Pandas for data processing and Streamlit for a user-friendly, interactive frontend. It relies on static data that can be visualized with Plotly, Matplotlib, and Seaborn, providing state- and category-wise analysis. The platform is designed for users with basic data analysis knowledge, offering easy exploration of caste-based crime trends and key performance indicators. Deployment is handled through Streamlit Cloud, ensuring automatic updates via GitHub commits.

## Installation & Getting Started | Setup the project in VS Code from Github
Detailed instructions on how to install, configure, and get the project running:

### How to clone a github repository
```
git clone https://github.com/sakshitechworld/india_crime_analysis.git
```

### How to publish your changes to Github
```
git add .
git commit -m "[Message]"
git push
```
<br>

## Streamlit
### How to test your code with Streamlit Locally?
```
conda activate .conda/
streamlit run src/app.py
```
<br>

### Deployment | How does the code get deployed to Streamlit cloud?
Streamlit cloud is connected with `main` branch of github, hence as soon as the code is committed in the `main` branch, it will be deployed to the cloud and the app will be available at https://crimeinsight.streamlit.app
<br>

## Technology Stack
```
Frontend: Streamlit
Data Processing: Pandas
Visualization: Plotly, Matplotlib, Seaborn
Deployment: Streamlit Cloud
```
<br>
