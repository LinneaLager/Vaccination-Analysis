## Vaccination-Analysis

# Instructions

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
    
If you enter just one country after -c1 the result should look like this: 

![Figure_1](https://user-images.githubusercontent.com/89390286/137326365-2d79d46c-961d-4b44-a05c-1c4ff113a497.png)

If you enter two countries the result should look like this:


![Figure_2](https://user-images.githubusercontent.com/89390286/137326962-acc77445-bd1f-4174-9838-ced85458ced4.png)



