# Explore a world of health data (THE GLOBAL HEALTH OBSERVATORY) python Library for world health organization API

This is a python package having multiple utilities. 
[Github-flavored Markdown](https://github.com/deepstartup/WHOAPIdata/)
[Source : https://www.who.int/data/gho/info/gho-odata-api]
1.whoApi.getDimension() : Retrieving the list of available dimensions
2.whoApi.DimensionValues() : Retrieving a list of available values for a specific dimension
3.whoApi.IndicatorValue() : Retrieving the indicators list
4.whoApi.IndFilterlike(IndicatorNameVal) : To select only the indicators which contain a specific text.Retrieving the indicators list
5.whoApi.IndFilterSpec(Tindicator) : To select only the indicators that have a specific title,Retrieving the indicators list
6.whoApi.IndData(IndCode) : Specify an indicator to download by specifying the indicator code. 
This will return all associated data for that specific indicator.
Retrieving indicator data
7.whoApi.IndAllData():Retrieving All Ind data in pandas dataframe,
Warning : Please set our context memory size before calling this function

#Data Returns in three format:
JSON,DF(DataFrame),XML. Default Format is : JSON