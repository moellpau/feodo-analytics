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
* AWS DynamoDB
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

**Task 3.2 and 3.5** <br>
In general, we choose bar charts because all other kinds of charts would not work. A line graph would suggest that there is data between the dates. But it is only one 
data point per day. A graph with points would have the same logic as the bar charts, hower it is more confusing and not that clearly arranged. Pie Charts does not work 
at all for our data, because we do not have data split. 

**IP address changes**

We created one plot to show the difference of total IP addresses between January and December. Because of less data for December there is no bar for days 5 to 8. 

![](plots/CompareJanDec.png)

**Change of total IP addresses per day in percentages**

To show the difference numbers per day of each data set, we created a barchart for each dataset.

![](plots/JanGrowthPercent.png)

![](plots/DecGrowthPercent.png)



**New IP Addresses per Day in Percentages**

Every day the IP adresses are changing. The following diagrams shows the difference per day for each dataset.

![](plots/JanNewIpsPercent.png)
![](plots/DecNewIpsPercent.png)

**Compare Average Percentages between Datasets**

To see the differences in one shot, we calculated the averages and put them into one graph.

![](plots/comparePercentJanDec.png)

**Task 3.6 Wordcloud** <br>
Two word clouds visualize in with countries most of the C&Cs can be found. To demonstrate the countries the different country codes are used

January:

![](plots/3_6-WordcloudJanuar.png)

December:

![](plots/3_6-WordcloudDezember.png)
