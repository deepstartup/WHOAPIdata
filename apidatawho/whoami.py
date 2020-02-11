class whoAmI:
    def __init__(self):
        self.getDim='https://ghoapi.azureedge.net/api/Dimension'
        self.getDimValues='https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues'
        self.getIndValues='https://ghoapi.azureedge.net/api/Indicator'
        self.getIndFilterVal='https://ghoapi.azureedge.net/api/Indicator?$filter=contains(IndicatorName,'
        self.getIndFilterSpecVal='https://ghoapi.azureedge.net/api/Indicator?$filter=IndicatorName eq '
        self.getIndData='https://ghoapi.azureedge.net/api/'