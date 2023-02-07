import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.dtypes.generic import ABCSeries

# Import Daten von Januar
resultsIPServer_old = pd.read_csv('exported_dataframes/results_comparison_jan.csv')
df_old = pd.DataFrame(resultsIPServer_old)

# Import Daten von Dezember
resultsIPServer_new = pd.read_csv('exported_dataframes/results_comparison_dec.csv')
df_new = pd.DataFrame(resultsIPServer_new)


### Methoden ###

# Erzeugt einen horizontalen Barplot zum Vergleich der Anzahl von IP Adresse vom Vortag und aktuellen Tag
def barPlotIpChanges(df, title, savename):
    # Plot anlegen und Legende ausrichten
    ipChanges = df.plot.barh(x="date", y=["total_previous_ips", "total_current_ips"], rot=0)
    _ = ipChanges.legend(bbox_to_anchor=(0.4, -0.2), loc='lower center', ncol=3, fancybox=True, shadow=True)
    ipChanges.set_title(title)
    ipChanges.set(ylabel=None)

    # Speichern und Anzeigen des Plots
    plt.tight_layout()
    plt.savefig('plots/' + savename + '.png')
    plt.show()

# Erzeugt einen Barplot zum Vergleich der Anzahl der neuen Ips pro Tag
def barBlotNewIps(df, title, savename):
    # Plot anlegen und Legende entfernen, da nur ein Wert in Legende
    newIps = df.plot.bar(x='date', y='new_ips')
    newIps.get_legend().remove()
    newIps.set_title(title)

    # Axen anoassen
    newIps.set(xlabel=None)
    plt.yticks(range(0, 34, 3))
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Speichern und Anzeigen des Plots
    plt.savefig('plots/' + savename + '.png')
    plt.show()

# Erzeugt einen Barplot zum Vergleich der neuen IPs in Prozent pro Tag
def barPlotNewIpsPercentage(df, title, savename):
    # Plot anlegen und Legende entfernen, da nur ein Wert in Legende
    newIps = df.plot(x='date', y='portion_new_ips', kind='bar')
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
    compare = df.plot.bar(x='Kategory', y=[0, 1])
    L = plt.legend(loc="upper right")
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

#3.2
barPlotIpChanges(df_old, "IP Adressen Änderungen von Januar 2022", '3_2-IPnumbersJan22')
barBlotNewIps(df_old, 'Anzahl neue IP Adressen pro Tag von Januar 2022', "3_2-newIpsJan22")
barPlotNewIpsPercentage(df_old, 'Neue IP Adressen in Prozent von Januar 2022', "3_2-newIpsProzentJan22")

#3.4 a) Vergeleiche einzelne Tage Datenset Dezember
barPlotIpChanges(df_new, "IP Adressen Änderungen von Dezember 2022", "3_4-IPnumbersDez22")
barBlotNewIps(df_new, 'Anzahl neue IP Adressen pro Tag von Dezember 2022', "3_4-newIpsDez22")
barPlotNewIpsPercentage(df_new, 'Neue IP Adressen in Prozent von Dezember 2022', "3_4-newIpsProzentDez22")

#3.4b) vergleichen zwischen Datensets Januar und Dezember
# Aufteilung des DataFrames in sinnvolle Kategorien zur Untersuchung der Daten im Vergleich Januar zu Dezember
names_newIps = ['new_ips', 'portion_new_ips']
names_basicIpValues = ['total_previous_ips', 'total_current_ips', 'same_ips']

# Erzeugen der DataFrames nach Kategorien
compareIP = compareDFs(names_newIps)
compareIpPercentage = compareDFs(names_basicIpValues)

# Plotten der Barcharts die die Daten Januar und Dezember vergleichen
xLabels_Percentage = ["Anzahl neue IPs", "Neue IPs in Prozent"]
compareBarPlot(compareIP, xLabels_Percentage, "Vergleich der Durchschnittsanzahl von IPs im Januar und Dezember",
               "3_4-VglAnzahlIpsJan-Dez")

xLabels_basic = ["Anzahl IPs Vortag", "Anzahl IPs Heute", "Gleiche IPs zum Vortag"]
compareBarPlot(compareIpPercentage, xLabels_basic, "Vergleich der neuen IPs in Anzahl und Prozent von Januar und Dezember",
               "3_4-VglAnzahlneueIPsJan-Dez")