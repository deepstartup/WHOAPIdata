"""
WHO API call python package Odata protocol <code for humanity>
@arghadeep.chaudhury@gmail.com
Date: 10-02-2020
Source : https://www.who.int/data/gho/info/gho-odata-api
"""
import requests
import json
import pandas as pd
import whoami
from json2xml import json2xml
apistrs=whoami.whoAmI()
class whoApi:
    def getDimension(self,oparam='JSON'):
        dimresp=requests.get(apistrs.getDim)
        dimrespdata=json.loads(dimresp.content)
        if oparam=='JSON':
            return dimrespdata['value']
        elif oparam=='DF':
            return pd.DataFrame(dimrespdata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(dimrespdata['value']).to_xml()
        else:
            return 'Param missing'
    def DimensionValues(self,oparam='JSON'):
        DimensionValuesres=requests.get(apistrs.getDimValues)
        DimensionValuesresdata=json.loads(DimensionValuesres.content)
        if oparam=='JSON':
            return DimensionValuesresdata['value']
        elif oparam=='DF':
            return pd.DataFrame(DimensionValuesresdata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(DimensionValuesresdata['value']).to_xml()
        else:
            return 'Param missing'
    def IndicatorValue(self,oparam='JSON'):
        indicatorval=requests.get(apistrs.getIndValues)
        indicatorvaldata=json.loads(indicatorval.content)
        if oparam=='JSON':
            return indicatorvaldata['value']
        elif oparam=='DF':
            return pd.DataFrame(indicatorvaldata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(indicatorvaldata['value']).to_xml()
        else:
            return 'Param missing'
    def IndFilterlike(self,IndicatorNameVal,oparam='JSON'):
        apistr=apistrs.getIndFilterVal+IndicatorNameVal+"')"
        IndFilterVal=requests.get(apistr)
        IndFilterValdata=json.loads(IndFilterVal.content)
        if oparam=='JSON':
            return IndFilterValdata['value']
        elif oparam=='DF':
            return pd.DataFrame(IndFilterValdata['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(IndFilterValdata['value']).to_xml()
        else:
            return 'Param missing'
    def IndFilterSpec(self,Tindicator,oparam='JSON'):
        specstr=apistrs.getIndFilterSpecVal+Tindicator+"'"
        IndFilterSpecdata=requests.get(specstr)
        IndFilterSpecdatajson=json.loads(IndFilterSpecdata.content)
        if oparam=='JSON':
            return IndFilterSpecdatajson['value']
        elif oparam=='DF':
            return pd.DataFrame(IndFilterSpecdatajson['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(IndFilterSpecdatajson['value']).to_xml()
        else:
            return 'Param missing'
    def IndData(self,IndCode,oparam='JSON'):
        indstr=apistrs.getIndData+IndCode
        IndDataApi=requests.get(indstr)
        IndDataJson=json.loads(IndDataApi.content)
        if oparam=='JSON':
            return IndDataJson['value']
        elif oparam=='DF':
            return pd.DataFrame(IndDataJson['value'])
        elif oparam=='XML':
            return json2xml.Json2xml(IndDataJson['value']).to_xml()
        else:
            return 'Param missing'
    def IndAllData(self):
        dffnlalldata=pd.DataFrame()
        fndata=IndicatorValue()
        for fulldata in fndata:
            df=IndData(fulldata['IndicatorCode'])
            df=pd.DataFrame(df)
            dffnlalldata=pd.concat([dffnlalldata,df])