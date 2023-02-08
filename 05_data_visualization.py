import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.dtypes.generic import ABCSeries

# Import Daten von Januar
resultsIPServer_old = pd.read_csv('exported_dataframes/results_comparison_jan.csv')
df_old = pd.DataFrame(resultsIPServer_old)

# Import Daten von Dezember
resultsIPServer_new = pd.read_csv('exported_dataframes/results_comparison_dec.csv')
df_new = pd.DataFrame(resultsIPServer_new)

# create compared Dataset
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8"]
df_both = pd.DataFrame(df_old['total_previous_ips'])
df_both = df_both.rename(columns={"total_previous_ips": 'January_Ips'})
df_both['December_Ips'] = df_new['total_previous_ips']
df_both['day'] = days
df_both['January_changePerc'] = df_new['total_growth_percentage']
df_both['December_changePerc'] = df_new['total_growth_percentage']
df_both['January_newPerc'] = df_new['portion_new_ips']
df_both['December_newPerc'] = df_new['portion_new_ips']

color1 = "#38761d"
color2 = "#212c4f"

### Methoden ###
def barPlotBothIps(df, title, savename):
    # Plot anlegen und Legende ausrichten
    ipChanges = df.plot.bar(x='day', y=["December_Ips", 'January_Ips'], rot=0, color={color1, color2})
    _ = ipChanges.legend(bbox_to_anchor=(0.4, -0.2), loc='lower center', ncol=3, fancybox=True, shadow=True)
    # ipChanges.get_legend().remove()
    ipChanges.set_title(title)
    ipChanges.set(xlabel=None)
    ipChanges.set(ylabel="Anzahl IP Adressen")

    # Speichern und Anzeigen des Plots
    plt.tight_layout()
    plt.savefig('plots/' + savename + '.png')
    plt.show()

# Erzeugt einen Barplot zum Vergleich der neuen IPs in Prozent pro Tag
def barPlotGrowthPercentage(df, title, savename, x , y, yRange, color):
    # Plot anlegen und Legende entfernen, da nur ein Wert in Legende
    newIps = df.plot(x=x, y=y, kind='bar', color=color)
    newIps.get_legend().remove()
    newIps.set_title(title)

    #Axen anoassen
    newIps.set(xlabel=None)
    plt.yticks(yRange)
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Speichern und Anzeigen des Plots
    plt.savefig('plots/' + savename + '.png')
    plt.show()

# Erzeugt einen Barplot zum Vergleich der neuen IPs in Prozent pro Tag
def barPlotNewIpsPercentage(df, title, savename, x , y, color):
    # Plot anlegen und Legende entfernen, da nur ein Wert in Legende
    newIps = df.plot(x=x, y=y, kind='bar', color=color)
    newIps.get_legend().remove()
    newIps.set_title(title)

    #Axen anoassen
    newIps.set(xlabel=None)
    plt.yticks(range(0, 16, 3))
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Speichern und Anzeigen des Plots
    plt.savefig('plots/' + savename + '.png')
    plt.show()

# verbindet die alten und neuen Daten in den gewünschten Kategorien
def compareDFs(names):
    # erzeugen zweier Listen mit den Mittelwerten
    old_averages = ['old']
    new_averages = ['new']
    for x in names:
        old_averages.append(df_old[x].mean())
        new_averages.append(df_new[x].mean())

    # erzeugen eines gemeinsamen DataFrames
    df_compare = pd.DataFrame(columns=names)
    df_compare.loc[0] = old_averages[1:]
    df_compare.loc[1] = new_averages[1:]

    # Dataframe anpassen damit Darstellung im Plot leichter wird
    df_compare = df_compare.T
    df_compare.insert(0, 'Kategory', names)
    return df_compare

# Erzeugt die plots zum Vergleich zwischen Januar und Dezember
def compareBarPlot(df, xLabels, title, savename):
    # Plot anlegen und Legende ausrichten
    compare = df.plot.bar(x='Kategory', y=[0, 1], color={color1, color2})
    L = plt.legend(loc="upper center")
    L.get_texts()[0].set_text('Daten von Januar')
    L.get_texts()[1].set_text('Daten von Dezember')

    # Axen und Titel
    compare.set_title(title)
    compare.set_xticklabels(xLabels, rotation=0)
    compare.set(xlabel=None)

    # Speichern und Anzeigen des Plots
    plt.tight_layout()
    plt.savefig('plots/' + savename + '.png')
    plt.show()

### Aufrufe zur Aufgabenlösung ####

# Nr. 1 Compare Total Jan & Dec
barPlotBothIps(df_both, "Number of IP addresses per day | January 2022", 'CompareJanDec')

# Nr. 2 January growth from day to day in Percentages
barPlotGrowthPercentage(df_old, 'January growth from day to day in Percentages', "JanGrowthPercent", 'date', 'total_growth_percentage', range(-6, 7, 2), color2)

# Nr. 3 December growth from day to day in Percentages
barPlotGrowthPercentage(df_new, 'December growth from day to day in Percentages', "DecGrowthPercent", 'date', 'total_growth_percentage', range(-17, 2, 3), color1)

# Nr. 4 New IP-Addresses in January from day to day in Percentages
barPlotNewIpsPercentage(df_old, 'New IP-Addresses in January from day to day in Percentages', "JanNewIpsPercent", 'date', 'portion_new_ips', color2)

# Nr. 5 New IP-Addresses in December from day to day in Percentages
barPlotNewIpsPercentage(df_new, 'New IP-Addresses in December from day to day in Percentages', "DecNewIpsPercent", 'date', 'portion_new_ips', color1)

# Nr. 6 Average Percentages new Ips and growth per day
namesT = 'total_growth_percentage', 'portion_new_ips'
xLabels_Percentage = ["Growth in Percentages", "New IPs in Percentages"]
compareBarPlot(compareDFs(namesT), xLabels_Percentage, "Compare January and December in Percentages", "comparePercentJanDec")
