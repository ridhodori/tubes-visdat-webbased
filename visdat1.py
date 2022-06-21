# -*- coding: utf-8 -*-
# 

from bokeh.io import output_notebook, curdoc
from bokeh.plotting import figure
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import ColumnDataSource, GroupFilter, CDSView, HoverTool, Div
from bokeh.layouts import column, widgetbox
import pandas as pd
import numpy as np

#import data
df = pd.read_csv('./stock_market.csv', parse_dates=['Date'])
df = df.rename(columns = {'Adj Close': 'Adj_Close'}, inplace = False)
df.head()

"""#Sortir data """

#sort data
source = ColumnDataSource(df)
filter_hs = [GroupFilter(column_name='Name', group='HANG SENG')]
source_hs = CDSView(source=source,filters=filter_hs)

filter_nk = [GroupFilter(column_name='Name', group='NIKKEI')]
source_nk = CDSView(source=source,filters=filter_nk)

filter_ns = [GroupFilter(column_name='Name', group='NASDAQ')]
source_ns = CDSView(source=source,filters=filter_ns)

#set circle info
circle_data = {'source': source, 'size': 3, 'alpha': 0.7, 'selection_color':'black'}

circle_hs = {'view': source_hs, 'color': 'red', 'legend_label': 'HANG SENG'}

circle_nk = {'view': source_nk, 'color': 'green', 'legend_label': 'NIKKEI'}

circle_ns = {'view': source_ns, 'color': 'blue', 'legend_label': 'NASDAQ'}

"""#Figure Adj_Close"""

#create figur
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
fig1 = figure(title= 'Adj Close Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Adj Close',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
fig1.circle(x='Date', y='Adj_Close', **circle_data, **circle_hs)
fig1.circle(x='Date', y='Adj_Close', **circle_data, **circle_nk)
fig1.circle(x='Date', y='Adj_Close', **circle_data, **circle_ns)

#add Hover
tooltips= [ ('Name','@Name'),('Adj_Close', '@Adj_Close') ]
hover_glyph = fig1.circle(x='Date', y= 'Adj_Close' , source=source,size=3, alpha=0, hover_fill_color='black', hover_alpha=0.5)
fig1.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

#hide data via legend(Level 3)
fig1.legend.click_policy = 'hide'
fig1.legend.location= 'top_right'

"""#Figure Volume (level2)"""

#create figur
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
fig2 = figure(title= 'Volume Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Volume',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
fig2.circle(x='Date', y='Volume', **circle_data, **circle_hs)
fig2.circle(x='Date', y='Volume', **circle_data, **circle_nk)
fig2.circle(x='Date', y='Volume', **circle_data, **circle_ns)

#add Hover
tooltips= [ ('Name','@Name'),('Volume', '@Volume') ]
hover_glyph = fig2.circle(x='Date', y= 'Volume' , source=source,size=3, alpha=0,hover_fill_color='black', hover_alpha=0.5)
fig2.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

#hide data via legend(Level 3)
fig2.legend.click_policy = 'hide'
fig2.legend.location= 'top_right'

"""#Figure Day_Perc_Change (level2)"""

#create figur
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
fig3 = figure(title= 'Day_Perc_Change Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Day_Perc_Change',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
fig3.circle(x='Date', y='Day_Perc_Change', **circle_data, **circle_hs)
fig3.circle(x='Date', y='Day_Perc_Change', **circle_data, **circle_nk)
fig3.circle(x='Date', y='Day_Perc_Change', **circle_data, **circle_ns)

#add Hover
tooltips= [ ('Name','@Name'),('Day_Perc_Change', '@Day_Perc_Change') ]
hover_glyph = fig3.circle(x='Date', y= 'Day_Perc_Change' , source=source,size=3, alpha=0,hover_fill_color='black', hover_alpha=0.5)
fig3.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

#hide data via legend(Level 3)
fig3.legend.click_policy = 'hide'
fig2.legend.location= 'top_right'

"""#Configure Panel"""

#add title
isi = """<h1>Visualisasi Data Interaktif Fluktuasi Harga Saham</h1>
<h3><i>Click Legend to HIDE Data</i><h3>"""
title = Div(text=isi)
#add widget panel and tab
fig1_panel = Panel(child=fig1, title='Adj Close Data')
fig2_panel = Panel(child=fig2, title='Volume Data')
fig3_panel = Panel(child=fig3, title='Day_Perc_Change Data')
tab = Tabs(tabs=[fig1_panel, fig2_panel, fig3_panel])
#add layout
layout = column(title,tab)
curdoc().theme = 'dark_minimal'
curdoc().add_root(layout)