# Big Data Analytics

Authors: Eric Beier, Friederike Marby and Paula Möller <br>
Date: 2023-02-09

## Description
This project is part of the module Big Data Analytics at HTW Berlin - Master Wirtschaftsinformatik.

#### Source Code <br>
* Clean Code
* Code conventions
* KISS/YAGNI
* runnable on every machine/ possible to deploy in a cloud environment - Tip: AWS Lambda!

#### Rough overview of the technologies used
* architecture diagram (draw.io) > https://aws.amazon.com/de/architecture/icons/
* Readme/ HowTo (*.md) > https://www.makeareadme.com

#### GitLab
A clean way of working in GitLab. Plan your work, use the function to estimate the amount of work and time invested.

#### Project tasks
##### A3.1 -  Data preparation & standardization
Please bring all files into a uniform structure. For the use of a NoSQL database there are extra points.

##### A3.2 - How big is the difference in the list / What % of IPs change per day?
only changing the IPs is enough (sometimes the port changes or other things).

##### A3.3 - 5 days current data from the Feodotracker
https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json
extra points for an automation script.

##### A3.4 - What is the difference in the IP lists from January 2022 to the current ones? / What % of IPs change per day in the current files?
only changing the IPs is enough (sometimes the port changes or other things)

##### A3.5 - Visual Report for A3.4
Here you have a free hand and can let off steam: Bar charts, time series or a map, etc. is fine here. Explain briefly why you have used this type of visualization.

##### A3.6 Create a wordcloud
Please create two word clouds with the country codes where most of the C&Cs can be found. 1x for January 2022 and once a current representation.

## Archicture diagram and used technologies
![Architecture diagram](/visuals/architecture_diagram.png)*Architecture diagram*

#### Used technologies
* AWS DynanmoDB
* AWS Lambda
* Local Python scripts

## How to execute & run

Before you can execute and run our code you need to install Python and the following library.

* Boto3
```
pip install boto3
```

In this project we used AWS Lambda as an event-driven, serverless computing platform provided by Amazon as part of Amazon Web Services. Therefore we defined and used the following Lambda functions.

**Lambda Functions**
* AutomatedQueryFeodoDaily - https://oxc77jgxqgt4pv77ojwz22icbq0hcpsx.lambda-url.eu-central-1.on.aws/
* dataExportDynamoDB - https://j6a7cppundv7t2fsdwke3tpkiu0qwyoo.lambda-url.eu-central-1.on.aws/

Our code is runnable on every machine (Win, Linux, Mac).

## Results and visualizations
**Aufgabe 3.2** 
Für die Betrachtung der Unterschiede der IP Listen im Januar wurden 3 Plots angefertigt. Einer der für jeden Tag die Anzahl der IP-Adressen anzeigt und zum Vergleich die vom Vortag. 
Darauf ist zu erkennen, dass sich die Anzahl der IP-Adressen immer im Bereich der 300 bewegt. Es wurde sich für ein horizontales Balkendiagramm entschieden, da dieses übersichtlich 
sowohl das Datuum als auch die Unterschiede in der Anzahl gut sichtbar darstellt. Die Skalierungen wurde so gewählt, dass dieses Diagramm mit dem Diagramm der neueren Daten 
verglichen werden kann.

![](plots/3_2-IPnumbersJan22.png)


Der zweite Plot zeigt die Anzahl der neuen IP Adressen über die Tage. Hier wurde sich für ein Balkendiagramm entschieden. Diese Darstellung ermöglicht auf einen schnellen Blick, die 
Unterschiede der Tage zu erfassen. Des Weiteren ist dies keine Zeitreihe, bei der die Daten des Vortages eine Rolle für die Daten des aktuellen Tages spielen. Daher würde ein 
Liniendiagramm eventuell verwirren, da diese oft für Zeitreihendaten verwendet werden, wo die Tage einen Einfluss aufeinander haben. Die Labels der X-Achse wurden rotiert, damit
diese besser lesbar sind und sich nicht gegenseitig überlappen. Die Skalierungen wurde so gewählt, dass dieses Diagramm mit dem Diagramm der neueren Daten verglichen werden kann. 

![](plots/3_2-newIpsJan22.png)


Der dritte Plot stellt die prozentualen Veränderungen der neuen IP-Adressen dar. Auch bietet sich das Balkendiagramm wieder am besten an. Zwar handelt es sich um Prozentwerte, 
jedoch stehen diese auch wieder für sich selbst und sind somit nicht in einem Kuchendiagramm darstellbar. Die Skalierungen wurde so gewählt, dass dieses Diagramm mit dem Diagramm der 
neueren Daten verglichen werden kann. 

![](plots/3_2-newIpsProzentJan22.png)


**Aufgabe 3.4**
Der erste Teil und somit die ersten 3 Plots wurden aus den selbigen Gründen wie Aufgabe 3.2 gewählt. Dadurch ist direkt schon eine Vergleich möglich. Des Weiteren wurden 2 Diagramme 
angefertigt, die die Durchschnittswerte des Januar-Datasets und des Dezember-Datasets vergleichen. Dort wurden ebenfalls Balkendiagramme gewählt, da hier am übersichtlichsten die 
Unterschiede der einzelnen Datensätze erkennbar sind. 

![](plots/3_4-IPnumbersDez22.png) ![](plots/3_4-newIpsDez22.png) ![](plots/3_4-newIpsProzentDez22.png)

Die folgenden Diagramme zeigen die Unterschiede der Daten von Januar und Dezember. Hier zu sehen ist die Anzahl(links) der neuen IPs pro Tag und in Prozent(rechts). Die Skala zeigt 
die Anzahl an, sowie auch die IPs in Prozent, da sich beide im Bereich von 3-30 oder 3%-30% bewegen. 

![](plots/3_4-VglAnzahlIpsJan-Dez.png)


Im letzten Diagramm sind die Anzahlen aller IP-Adressen zu sehen. Auch hier war ein Balkendiagramm am sinnvollsten, da nur dieses einen gut erkennbaren Überblick über alle 
drei Kennzahlen ermöglicht.

![](plots/3_4-VglAnzahlneueIPsJan-Dez.png)


**Aufgabe 3.6 Wordcloud**

Janurary:

![](plots/3_6-WordcloudJanuar.png)

December:

![](plots/3_6-WordcloudDezember.png)