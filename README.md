## Vaccination-Analysis

# Hi and welcome to the Vaccination analysis application!

This application compares two countries in terms of vaccination data, you can select the vaccination numbers you would
like to compare between the countries. For each country or two countries you can analyse the following columns.

These dataflags shows latest values for countries specified: <br/>

total_vaccinations, <br/>
people_fully_vaccinated, <br/>
total_vaccinations_per_hundred, <br/>
people_fully_vaccinated_per_hundred <br/>

This dataflag shows the mean/average vaccination for the countries specified: <br/>

daily_vaccinations <br/>


If you need additional information such as the sources for each individual country then you can find them in the excel-document. 

The different columns stated above can be sorted and compared for two countries in a simple bar-chart. For some help enter -h. 

# Instructions!

Download or clone repository. Use pip install -r requirements.txt. What to enter into the terminal? 
    
    python main.py -c1 country1 -c2 country2 -d dataflag 
    
If you only want to analyse just one country then don't enter the -c2.


