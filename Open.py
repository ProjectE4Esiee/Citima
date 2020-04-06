import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import csv
import dask.dataframe as dd

df = dd.read_csv("valeursfoncieres-2018.csv", sep="|",header=None,na_values="")



df = pd.read_csv("valeursfoncieres-2018.csv", sep="|", na_values="", encoding="latin1")                                            
g = df.groupby('Code departement')
for key in g.groups.keys(): 
    	     dfmin = g.get_group(key)  
    	     dfmin.to_csv("tab_"+str(key)+'.csv') 