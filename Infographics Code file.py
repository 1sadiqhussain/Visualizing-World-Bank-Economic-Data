# Importing the Pandas library 
import pandas as pd

# Importing the NumPy library
import numpy as np

# Importing the Matplotlib library 
import matplotlib.pyplot as plt

# Import the Seaborn library
import seaborn as sns

# defining a Read_data function for reading all the datasets at the same time and with selected list of rows
def Read_data (filename, rows=None):
    data = pd.read_csv(filename,header=[2]) # Reads the csv file while skipping the first 2 rows
    data = data.fillna(0) # Fills the na values with 0
    data = data.iloc[:,[0,60,61,62,63]]  # Selects only the necessary columns
    if rows is not None: # Creating if statement for selecting the rows
        data = data.iloc[rows]
    print(data) # Printing the data
    return data

# Calling the  Read_data function to read the file selecting the list of rows
literacy=Read_data("D:\code files\infographics assignment\Literacy rate, youth total (% of people ages 15-24).csv",rows=[1,3,7,36,63,65,134,153])
government_spending=Read_data("D:\code files\infographics assignment\Government expenditure on education, Total(% of government expenditure).csv",rows=[1,3,7,36,63,65,134,153])
school_enrollement=Read_data("D:\code files\infographics assignment\school enrollment, primary and secondary(gross), gender parity index (GPI).csv",rows=[1,3,7,36,63,65,134,153])
gdp_current=Read_data("D:\code files\infographics assignment\GDP current.csv",rows=[1,3,7,36,63,65,134,153])

# Setting the plot style and font size
sns.set(style="whitegrid")
plt.rcParams.update({'font.size': 10})

# Creating the figure with required dimensions and fig size and dpi set to 300 as instructed and subplots
fig, axes = plt.subplots(2, 2, figsize=(22, 22), dpi=300)
fig.subplots_adjust(wspace=0.4, hspace=0.4)

# Adding the Title for the dashboard
plt.suptitle('"Exploring Global Trends in Literacy, Government Expenditure, and Economic Growth: A Comprehensive Dashboard"\nS J Hussain Kareemulla Sha Khadari Shaik(21079856)', fontsize = 20, fontweight = 'bold', color = 'green', horizontalalignment='center')

# Creating Bar plot for Literacy Rate by country for all years
bar_width = 0.2 # Determining the bar width
years = literacy.columns[1:] # Creating a list of years by selecting all the columns of the 'literacy' dataframe starting from the second column
x = np.arange(len(literacy['Country Name'])) # Creating a range of values from 0 to the number of countries in the 'literacy' dataframe

# Iterate over each year in the 'years' list and assign an index to 'i'
for i, year in enumerate(years):
    axes[0, 0].bar(x + i * bar_width, literacy[year], width=bar_width, label=year) # Using the 'literacy[year]' column as the height of each bar

# Adding text above the barplot for explaination 
axes[0, 0].text(0.5, 1.07, 'This bar plot shows the literacy rate for selected Regions over time.\nThe x-axis shows the countries, and the y-axis shows the literacy rate.\nEach color of bars indicates a year.\n', fontsize=16, fontweight='bold', color='blue', transform=axes[0, 0].transAxes, horizontalalignment='center')
axes[0, 0].set_xticks(x + bar_width * (len(years) - 1) / 2) # Setting the x-ticks at the center of each group of bars
axes[0, 0].set_xticklabels(literacy['Country Name'], rotation=20, ha='right') # Setting the labels of the x-ticks to the country names, rotated by 20 degrees and aligned to the right
axes[0, 0].set_xlabel('Region', fontsize=15) # Determining the name of X_label with a fontsize of 15
axes[0, 0].set_ylabel('Literacy Rate (%)', fontsize=15) # Determining the name of Y_label with a fontsize of 15
axes[0, 0].legend(title="Year",loc='lower right') # Adding a legend to the plot with title as year and placed at lower right corner of the plot
axes[0, 0].set_title('Literacy Rate by Country for All Years', fontsize=16, fontweight='bold') # Determining the title of the barplot with fontsize of 15 and in bold letters 

# Creating the Box plot for the school enrollment
# Creates a list of years by selecting all the columns of the 'school_enrollment' dataframe
years = school_enrollement.columns[1:]

# Reshaping the 'school_enrollment' dataframe from wide format to long format
# Use 'Country Name' as the identifier variable, 'years' as the measured variables, and 'Enrollment' as the value variable
school_enrollement_melted = pd.melt(school_enrollement, id_vars=['Country Name'], value_vars=years, var_name='Year', value_name='Enrollment')

# Creating a box plot using seaborn with Year column as X-axis and Enrollement as Y-axis
box_plot = sns.boxplot(ax=axes[0, 1], x='Year', y='Enrollment', data=school_enrollement_melted)

# Calculate and display median values for each box
# Iterate over each year in the 'years' list and assign an index to 'i'
for i, year in enumerate(years):
    # Calculating the median enrollment rate for the current year
    median = school_enrollement_melted[school_enrollement_melted['Year'] == year]['Enrollment'].median()
    # Adding the median value as text on the box
    axes[0, 1].text(i, median, f'{median:.2f}', ha='center', va='bottom', fontweight='bold', color='black')

# Adding text above the box plot for explaination 
axes[0, 1].text(1.9, 1.07, 'This box plot shows the school Enrollement rate for Selected Regions over the span of four years.\nThe x-axis shows the Years, and the y-axis shows the Enrollement rate.\nWe Can observe that the median is same over the years that is near to 0.98 \nwhich is advantageous for the selected Regions in many aspects', fontsize=16, fontweight='bold', color='blue', transform=axes[0, 0].transAxes, horizontalalignment='center')
axes[0, 1].set_xticklabels(years, rotation=0, ha='right') # Setting the labels of the x-ticks to the Years, aligned to the right
axes[0, 1].set_xlabel('Year', fontsize=15) # Determining the name of X_label with a fontsize of 15
axes[0, 1].set_ylabel('Enrollement Rate', fontsize=15) # Determining the name of Y_label with a fontsize of 15
axes[0, 1].set_title('School Enrollment for All Years', fontsize=16, fontweight='bold') # Determining the title of the box plot with fontsize of 16 and in bold letters 

# Creating a Scatter plot for GDP current for different years and regions
# Iterate over the last four columns of the 'gdp_current' dataframe using negative indices
for year_idx in range(-4, 0):
    # Creating a scatter plot using country name as X-axis variable and current negative index as the y-axis variable
    axes[1, 0].scatter(gdp_current['Country Name'], gdp_current.iloc[:, year_idx], label=gdp_current.columns[year_idx], s=70)

# Adding text above the Scatter plot for explaination 
axes[1, 0].text(0.5, 1.06, 'This scatter plot shows the GDP for the Regions over four years.\nThe x-axis shows the countries, and the y-axis shows the GDP.\nEach color of the points indicates the year.\n we can observe how increase in Literacy rates helps in GDP growth over the years', fontsize=16, fontweight='bold', color='blue', transform=axes[1, 0].transAxes, horizontalalignment='center')
axes[1, 0].set_xticks(np.arange(len(gdp_current['Country Name']))) # Set the x-ticks to evenly spaced values from 0 to the number of regions in the 'gdp_current' dataframe
axes[1, 0].set_xticklabels(gdp_current['Country Name'], rotation=25, ha='right') # Setting the labels of the x-ticks to the country names, rotated by 25 degrees and aligned to the right
axes[1, 0].set_xlabel('Region', fontsize=15) # Determining the name of X_label with a fontsize of 15
axes[1, 0].set_ylabel('GDP Current', fontsize=15) # Determining the name of Y_label with a fontsize of 15
axes[1, 0].legend(title="Year") # Adding a legend to the plot with title as year 
axes[1, 0].set_title('GDP Current', fontsize=16, fontweight='bold') # Determining the title of the box plot with fontsize of 16 and in bold letters

# Creating a Line Plot for the Government Expenditure on Education for all years
# Iterate over the rows of the 'government_spending' dataframe using the 'iterrows()' method
for i, country in government_spending.iterrows():
    # Plotting the values in the current row against the 'years' list with linewidth of 3 and marksersize of 10
    axes[1, 1].plot(years, country[1:], marker='o', label=country['Country Name'], linewidth=3, markersize=10)

# Adding text above the Line plot for explaination 
axes[1, 1].text(0.5, 1.06, 'This line plot shows the government expenditure on education sector for the Regions over time.\nThe x-axis shows the years, and the y-axis shows the percentage of expenditure.\nEach line represents a country, and the markers indicate the data points for each year.\n', fontsize=16, fontweight='bold', color='blue', transform=axes[1, 1].transAxes, horizontalalignment='center')
axes[1, 1].set_xticks(years) # Set the x-ticks to the 'years'
axes[1, 1].set_xticklabels(years) # Setting the labels of the x-ticks to the 'years'
axes[1, 1].set_xlabel('Year', fontsize=15) # Determining the name of X_label with a fontsize of 15
axes[1, 1].set_ylabel('Government Expenditure on Education (%)', fontsize=15) # Determining the name of Y_label with a fontsize of 15
axes[1, 1].legend(title="Regions",loc='center left', bbox_to_anchor=(1.0, 0.5))  # Adding a legend to the plot with title as Regions and it is placed at center left besides the plot
axes[1, 1].set_title('Government Expenditure on Education sector', fontsize=16, fontweight='bold') # Determining the title of the Line plot with fontsize of 16 and in bold letters

# Adding the conclusion text
conclusion = """In conclusion, this dashboard provides valuable insights into the relationships
                between Literacy, Government Expenditure, and GDP across various Regions. We can observe how 
                high literacy rates and high school enrollment rates can contribute to the growth of the economy and development of the regions.
                By analyzing these trends, anyone can make informed decisions to foster Educational Advancement and Economic Growth"""

# Positioning the text with fontsize of 18 on bottom with bold letters
plt.text(0.7, 0.03, conclusion, fontsize=18, ha='center', va='bottom', fontweight='bold', wrap=True, transform=fig.transFigure)

# Save the figure as a PNG file with 300 dpi as recommended
fig.savefig('21079856.png', dpi=300, bbox_inches='tight')

# Shows the plots
plt.show()
