# Infographics Dashboard
# Exploring Global Trends in Literacy, Government Expenditure, and Economic Growth

## Project Overview

This project analyzes and visualizes global trends in literacy rates, government expenditure on education, and GDP across various regions. The goal is to provide valuable insights into the relationships between these key indicators and contribute to informed decision-making in education and economic planning.

## Libraries Used

- Pandas: For data manipulation and analysis.
- NumPy: For numerical operations.
- Matplotlib and Seaborn: For data visualization.

  ## Files
- `dashboard.py` - Python script to generate the infographics dashboard
- `21079856.png` - Output infographic dashboard image
- `Literacy rate, youth total (% of people ages 15-24).csv` - Literacy rate data
- `Government expenditure on education, Total(% of government expenditure).csv` - Government education spending data 
- `school enrollment, primary and secondary(gross), gender parity index (GPI).csv` - School enrollment data
- `GDP current.csv` - GDP data

## Code Structure

### 1. Data Handling

- Utilizes Pandas for reading, cleaning, and selecting specific rows from multiple datasets.
- Defines a versatile `Read_data` function for efficient data loading.

### 2. Dashboard Overview

- Comprises four plots:
  - Bar plot: Literacy Rates by Country for different years.
  - Box plot: School Enrollment Rates over four years.
  - Scatter plot: GDP trends across Regions for four years.
  - Line plot: Government Expenditure on Education for various regions over time.

### 3. Interpretation of Plots

- Provides visual interpretations for each plot, highlighting trends and correlations.

### 4. Use Cases

- Education Policy Planning: Insights for governments to plan education policies.
- Economic Development: Understanding the relationship between literacy rates and GDP growth.
- International Comparisons: Analyzing government expenditure on education across regions.

## How to Run the Code

1. Ensure you have Python installed on your machine.
2. Install required libraries using `pip install pandas numpy matplotlib seaborn`.
3. Download the code files and datasets.
4. Run the code in a Python environment (e.g., Jupyter Notebook).

## Key Findings

- Strong positive correlations between literacy rates, school enrollment, and economic growth.
- Regions with high literacy rates tend to exhibit robust GDP growth and sustained government expenditure on education.

## Output

- The project generates a comprehensive PNG file ('21079856.png') encapsulating the dashboard for easy sharing and presentation.

## Impact

This project serves as a valuable resource for stakeholders interested in the intersection of education, government spending, and economic growth on a global scale. It provides actionable insights for policymakers, researchers, and businesses.
