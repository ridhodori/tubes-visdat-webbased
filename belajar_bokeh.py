#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bokeh.plotting import figure,  show
from bokeh.models import ColumnDataSource
from bokeh.io import output_notebook, show 
from bokeh.io import curdoc
from bokeh.models import NumeralTickFormatter, DatetimeTickFormatter
from bokeh.models.widgets import Dropdown


# In[2]:


df = pd.read_csv('./GGRM.csv', parse_dates= ['date'])
df2 = df[['date','open_price']]
df3 = df[['date', 'close']]


# In[3]:


df2_cds= ColumnDataSource(df2)
df3_cds= ColumnDataSource(df3)


# In[4]:


p = figure(x_axis_type='datetime',
          plot_height=700, sizing_mode="stretch_width",
          title="GGRM Open Price over time", x_axis_label="Date",
          y_axis_label="Price")
#apply theme
curdoc().theme = "dark_minimal"

#render line
p.step('date','open_price', color='blue', legend_label='open_price',
      source = df2_cds)
p.step('date','close', color='red', legend_label='close_price',
      source = df3_cds)

#format ticks
p.x_range.range_padding = 0.05
p.xaxis.ticker.desired_num_ticks = 40
p.xaxis.major_label_orientation = 3.14 / 4
p.xaxis.formatter=DatetimeTickFormatter(
days=["%d-%m-%Y"],
months=["%d-%m-%Y"],
years=["%d-%m-%Y"],
)

#legend location
p.legend.location = 'top_left'

show(p)

