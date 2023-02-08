# Erzeugt einen Barplot zum Vergleich der Anzahl der neuen Ips pro Tag
def barBlotNewIps(df, title, savename):
    # Plot anlegen und Legende entfernen, da nur ein Wert in Legende
    newIps = df.plot.bar(x='date', y='new_ips')
    newIps.get_legend().remove()
    newIps.set_title(title)

    # Axen anpassen
    newIps.set(xlabel=None)
    plt.yticks(range(0, 34, 3))
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Speichern und Anzeigen des Plots
    plt.savefig('plots/' + savename + '.png')
    plt.show()


barBlotNewIps(df_old, 'Anzahl neue IP Adressen pro Tag von Januar 2022', "3_2-newIpsJan22")
barBlotNewIps(df_new, 'Anzahl neue IP Adressen pro Tag von Dezember 2022', "3_4-newIpsDez22")

# Erzeugt einen horizontalen Barplot zum Vergleich der Anzahl von IP Adresse vom Vortag und aktuellen Tag
def barPlotIpChanges(df, title, savename):
    # Plot anlegen und Legende ausrichten
    ipChanges = df.plot.bar(x="date", y=["total_previous_ips"], rot=0)
    #_ = ipChanges.legend(bbox_to_anchor=(0.4, -0.2), loc='lower center', ncol=3, fancybox=True, shadow=True)
    ipChanges.get_legend().remove()
    ipChanges.set_title(title)
    ipChanges.set(xlabel=None)
    ipChanges.set(ylabel="Anzahl IP Adressen")

    # Speichern und Anzeigen des Plots
    plt.tight_layout()
    plt.savefig('plots/' + savename + '.png')
    plt.show()

# barPlotIpChanges(df_old, "Anzahl IP Adressen pro Tag im Januar 2022", '3_2-IPnumbersJan22')
# barPlotIpChanges(df_new, "Anzahl IP Adressen pro Tag im Dezember 2022", "3_4-IPnumbersDez22")

