import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

countryCodesDecember = pd.read_csv('exported_dataframes/country_codes_dec.csv')
countryCodesJanuary = pd.read_csv('exported_dataframes/country_codes_jan.csv')

# CountrieCodes into CountryNames
# def changeCodeToCountry(codes):
#     # import List of Countrycodes and Countries
#     countryCodesToCountryList = pd.read_csv('exported_dataframes/CodesTranslation.csv')
#     transCodes = countryCodesToCountryList['CountryCode']
#     translationOfCodes = countryCodesToCountryList['Country']
#
#     # check every CountryCode
#     countries = []
#     for x in codes:
#         count = 0
#         # save the Name of the country for the given Code
#         for y in transCodes:
#             if x == y:
#                 countries.append(translationOfCodes[count])
#             count = count + 1
#
#     # return a list of the country names
#     return countries
def createWordCloud(list, savename):
    # transform into String list
    words = ' '.join(list)

    # generate Wordcloud
    cloudCountryDec = WordCloud(width=640, height=480, colormap="Blues").generate(words)

    # print Wordcloud
    plt.imshow(cloudCountryDec, interpolation='bilinear')
    plt.axis('off')

    # Speichern und Anzeigen des Plots
    plt.savefig('plots/' + savename + '.png')
    plt.show()

# start WordCloudGenerator
createWordCloud(countryCodesJanuary['country'], "3_6-WordcloudJanuar")
createWordCloud(countryCodesDecember['country'], "3_6-WordcloudDezember")

