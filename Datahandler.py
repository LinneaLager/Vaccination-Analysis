# import matplotlib and pandas
import pandas as pd
import matplotlib.pyplot as mpl
from matplotlib.ticker import FormatStrFormatter

class plot_vaccinations():
    def __init__(self, country1, country2, dataflag):
        """ Visualise two countries on the dataflag specified in a line chart over time.

        Args:
            country1 (str, required): Country 1 on chart
            country2 (str, optional): Country 2 on chart
            dataflag (str, required): Data to be visualised
        """
        # Capitalize country names
        self.country1 = country1.capitalize()
        self.country2 = country2.capitalize()
        self.dataflag = dataflag

        # Retrieve dataframe with country summary on specific dataflag
        df = _extract_country_data(self.country1,self.country2,self.dataflag)
        # Call method to draw visualisation
        drawbarchart(df,dataflag)


def _extract_country_data(country1,country2,dataflag):
    """ Method that retrieves and summarises the data of the two countries specified. 

    Args:
        country1 (str, required): Country 1 on chart
        country2 (str, required): Country 2 on chart
        dataflag (str, required): Column to be summarised and retrieved
    """
        
    countries = [country1, country2]
    df = pd.read_csv('vaccination_data.csv')
    newdf = df[df['country'].isin(countries)]
    newdf = newdf.groupby(['country'])[dataflag].agg('sum')
    print(newdf)
    return newdf

def drawbarchart(df,dataflag):
    """ Method that uses the summarised dataframe and visualises it in a bar chart

    Args:
        df (dataframe, required): Dataframe that has the requried 2 columns to be visualised (countries and summarised numbers)
        dataflag (str, required): Data to be visualised, just used in this method to add chart title
    """
       
    #draw plot nbased on dataframe values
    ax = df.plot.bar(stacked=True,figsize=(8, 10), color='#86bf91', zorder=2, width=0.85)

    #set title
    ax.set_title(dataflag)
    
    # customise ticks
    ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
    mpl.yticks(rotation='horizontal')
    mpl.xticks(rotation='horizontal')
    vals = ax.get_xticks()
    
    for tick in vals:
        ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
    
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))
    
    # displays the set up graph
    mpl.show()