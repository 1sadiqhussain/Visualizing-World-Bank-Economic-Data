# Infographics Dashboard
This project generates an infographics dashboard to visualize global trends in literacy, government education spending, school enrollment, and economic growth. 

## Files
- `dashboard.py` - Python script to generate the infographics dashboard
- `21079856.png` - Output infographic dashboard image
- `Literacy rate, youth total (% of people ages 15-24).csv` - Literacy rate data
- `Government expenditure on education, Total(% of government expenditure).csv` - Government education spending data 
- `school enrollment, primary and secondary(gross), gender parity index (GPI).csv` - School enrollment data
- `GDP current.csv` - GDP data

## Usage
The `dashboard.py` script imports Pandas, NumPy, Matplotlib, and Seaborn to generate the dashboard. It defines a function `Read_data()` to read in the data files, clean the data, and select specific rows. 

The main script calls this function to read in each data file and store in a DataFrame. It then generates a matplotlib figure with subplots for each visualization:

- Bar plot for literacy rate by country over time
- Box plot for school enrollment by year 
- Scatter plot for GDP by country and year
- Line plot for government education spending by country over time

Finally, it adds a conclusion text and saves the figure as a high resolution PNG image.

To use, simply run `python dashboard.py`. This will generate and save the `21079856.png` dashboard image.

## Requirements
- Pandas 
- NumPy
- Matplotlib
- Seaborn 
