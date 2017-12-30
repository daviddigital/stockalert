import re
values = re.sub('(^,+|,+$)', '', input_data['values'])
values = re.sub(',+', ',', values)
firstchar = values.index('Last')
startchar = firstchar + 5
lastchar = values.index('Change') - 3
stockpricestr = values[startchar:lastchar]
stockprice = float(stockpricestr)
return {'stockprice' : stockprice}
