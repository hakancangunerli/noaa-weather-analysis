# %%
from noaa_sdk import NOAA
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
from IPython.display import HTML
import kaleido

plt.rcParams["figure.figsize"] = (20,10)
n = NOAA()
res = n.get_forecasts('30609', 'US', type='forecastHourly')


endTime =[]
startTime = []
temperature = []
for i in res:
    temperature.append(i['temperature'])
    endTime.append(i['endTime'][-14:])
    startTime.append(i['startTime'][-14:])

endTimeFormatted = []
startTimeFormatted = []
# temperature
for i in range(len(temperature)):
    endTimeFormatted.append(endTime[i][0:5])
    startTimeFormatted.append(startTime[i][0:5])
    

# %%

#box plot to give average 
fig1 = px.box(endTimeFormatted, temperature, points=False, title='Temperature Box Plot')
#fig.show()
fig1.write_html("./fig1.html")
fig1.write_image("./fig1.svg")



# %% [markdown]
# ![]<img src="./fig1.svg">


