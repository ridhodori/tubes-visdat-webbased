
from bokeh.io import output_notebook, curdoc
from bokeh.plotting import figure
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import ColumnDataSource, GroupFilter, CDSView, HoverTool, Div
from bokeh.layouts import column, widgetbox
import pandas as pd
import numpy as np

#import data
df = pd.read_csv('./indexData.csv', parse_dates=['Date'])
df = df.rename(columns = {'Adj Close': 'Adj_Close'}, inplace = False)
df.head()

# #Sortir data

#sort data
source = ColumnDataSource(df)
filter_ny = [GroupFilter(column_name='Index', group='NYA')]
source_ny = CDSView(source=source,filters=filter_ny)
filter_ix = [GroupFilter(column_name='Index', group='IXIC')]
source_ix = CDSView(source=source,filters=filter_ix)
filter_gd = [GroupFilter(column_name='Index', group='GDAXI')]
source_gd = CDSView(source=source,filters=filter_gd)
filter_gs = [GroupFilter(column_name='Index', group='GSPTSE')]
source_gs = CDSView(source=source,filters=filter_gs)

#set circle info
circle_data = {'source': source, 'size': 4, 'alpha': 0.7, 'selection_color':'black'}
circle_ny = {'view': source_ny, 'color': 'red', 'legend_label': 'NYA'}
circle_ix = {'view': source_ix, 'color': 'green', 'legend_label': 'IXIC'}
circle_gd = {'view': source_gd, 'color': 'blue', 'legend_label': 'GDAXI'}
circle_gs = {'view': source_gs, 'color': 'yellow', 'legend_label': 'GSPTSE'}
# Figure Adj_Close

#create figur
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
fig1 = figure(title= 'Adj Close Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Adj Close',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)
              
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
fig2 = figure(title= 'High Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'High',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
fig3 = figure(title= 'Open data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Open',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
fig4 = figure(title= 'Open data',x_axis_label='Low', y_axis_label= 'High',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)
#add data circle
fig1.circle(x='Date', y='Adj_Close', **circle_data, **circle_ny)
fig1.circle(x='Date', y='Adj_Close', **circle_data, **circle_ix)
fig1.circle(x='Date', y='Adj_Close', **circle_data, **circle_gd)
fig1.circle(x='Date', y='Adj_Close', **circle_data, **circle_gs)
fig2.circle(x='Date', y='High', **circle_data, **circle_ny)
fig2.circle(x='Date', y='High', **circle_data, **circle_ix)
fig2.circle(x='Date', y='High', **circle_data, **circle_gd)
fig2.circle(x='Date', y='High', **circle_data, **circle_gs)

fig3.circle(x='Date', y='Open', **circle_data, **circle_ny)
fig3.circle(x='Date', y='Open', **circle_data, **circle_ix)
fig3.circle(x='Date', y='Open', **circle_data, **circle_gd)
fig3.circle(x='Date', y='Open', **circle_data, **circle_gs)

fig4.circle(x='Date', y='Open', **circle_data, **circle_ny)
fig4.circle(x='Date', y='Open', **circle_data, **circle_ix)
fig4.circle(x='Date', y='Open', **circle_data, **circle_gd)
fig4.circle(x='Date', y='Open', **circle_data, **circle_gs)
#add Hover
tooltips= [ ('Index','@Index'),('Adj_Close', '@Adj_Close') ]
hover_glyph = fig1.circle(x='Date', y= 'Adj_Close' , source=source,size=4, alpha=0, hover_fill_color='black', hover_alpha=0.5)
fig1.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

tooltips= [ ('Index','@Index'),('High', '@High') ]
hover_glyph = fig2.circle(x='Date', y= 'High' , source=source,size=4, alpha=0,hover_fill_color='black', hover_alpha=0.5)
fig2.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

tooltips= [ ('Index','@Index'),('Open', '@Open') ]
hover_glyph = fig3.circle(x='Date', y= 'Open' , source=source,size=4, alpha=0,hover_fill_color='black', hover_alpha=0.5)
fig3.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

tooltips= [ ('Index','@Index'),('Low', '@Low'), ('High', '@High')]
hover_glyph = fig4.circle(x='High', y= 'Low' , source=source,size=4, alpha=0,hover_fill_color='black', hover_alpha=0.5)
fig4.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))
#hide data via legend
fig1.legend.click_policy = 'hide'
fig1.legend.location= 'top_right'
fig2.legend.click_policy = 'hide'
fig2.legend.location= 'top_right'
fig3.legend.click_policy = 'hide'
fig3.legend.location= 'top_right'
fig4.legend.click_policy = 'hide'
fig4.legend.location= 'top_right'


#add title
isi = "stock movements from around the world with data collected from yahoo finance"
title = Div(text=isi)
#add widget panel and tab
fig1_panel = Panel(child=fig1, title='Adj Close Data')
fig2_panel = Panel(child=fig2, title='High Data')
fig3_panel = Panel(child=fig3, title='Open Data')
fig4_panel = Panel(child=fig4, title='high vs low')
tab = Tabs(tabs=[fig1_panel, fig2_panel, fig3_panel, fig4_panel])
#add layout
layout = column(title,tab)
curdoc().theme = 'dark_minimal'
curdoc().add_root(layout)