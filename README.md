# Big Data Analytics

Authors: Eric Beier, Friederike Marby and Paula Möller <br>
Date: 2023-01-26

## Description
This project is part of a module Big Data Analytics at HTW Berlin - Master Wirtschaftsinformatik.

#### Source Code <br>
* Clean Code
* Code conventions
* KISS/YAGNI
* runnable on every machine/ possible to deploy in a cloud environment - fuer den Cloud Einsatz gibt es extra Punkte. Tipp: AWS Lambda!

#### Rough overview of the technologies used
* architecture diagram (draw.io) > https://aws.amazon.com/de/architecture/icons/
* Readme/ HowTo (*.md) > https://www.makeareadme.com

#### GitLab
Eine saubere Arbeitsweise in GitLab. Plant eure Arbeit, verwenden die Funktion zum abschätzen des Arbeitsaufwandes und der investierten Zeit.

#### Project tasks
##### A3.1 -  Datenaufbereitung & Vereinheitlichung
Bitte alle Files in eine einheitliche Struktur bringen. Fuer den Einsatz einer NoSQL Datenbank es extra Punkte.

##### A3.2 - Wie groß ist der Unterschied in der Liste? / Wie viel % der IPs verändern sich am Tag?
nur die Änderung der IPs ist ausreichend(manchmal ändert sich der Port oder andere Dinge).

##### A3.3 - 5 Tage die Aktuellen Daten von dem Feodotracker
https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json
fuer ein Automatisierungsskript gibt es extra Punkte.

##### A3.4 - Wie groß ist der Unterschied in den IP Listen vom Januar 2022 zu den aktuellen? / Wie viel % der IPs verändern sich am Tag in den aktuellen files?
nur die Änderung der IPs ist ausreichend(manchmal ändert sich der Port oder andere Dinge).

##### A3.5 - Visual Report fuer A3.4
hier habt ihr freie Hand und könnt euch austoben: Balkendiagramme, Zeitreihen oder eine Map, etc. ist hier fein. Erklärt kurz warum ihr die Art der Visualisierung verwendet habt.

##### A3.6 Erstellt eine Wordcloud
Bitte erstellt zwei Wordcouds mit mit den Laendercodes wo die meisten C&Cs zu finden sind. 1x fuer Januar 2022 und einmal eine aktuelle Darstellung.

## Archicture diagram and used technologies
![Architecture diagram](/visuals/architecture_diagram.png)*Architecture diagram*

#### Used technologies
* Dynanmo DB
* AWS Lambda
* Local Python scripts

## How to execute & run

Explain how to run and execute our code, installed/used libraries and lambda function
Runnable on every machine (Win, Linux, Mac)