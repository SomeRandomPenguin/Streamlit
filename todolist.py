import pandas as pd
import datetime as dt
import streamlit as st

class todolist_pd():
    
    def __init__(self):
        self.df = pd.DataFrame({'topic':['test'], 'body':['test body'],      #Table make
                       'date':[dt.datetime.now()],
                       'created_date':[dt.datetime.now()]})

    def create(self, topic, body, target_date):                                         #Make new 
        new_data = {'topic':topic, 'body':body, 'target_date':target_date,
                    'created_date':dt.datetime.now()}
        self.df = self.df.append(new_data, ignore_index=True)

    def read(self):                                                               #Read table
        return self.df
  
    def update(self, topic, body, target_date):                           #Change table
        select_row = self.df[self.df.topic ==topic].index
        self.df.loc[select_row,'body'] = body
        self.df.loc[select_row,'target_date'] = target_date

    def delete(self, topic):                                    #delete topic
        select_row = self.df[self.df.topic==topic].index
        st.write(select_row)
        self.df = self.df.drop(select_row)
    
    def save(self, file):
        self.df.to_csv(file)
    
    def load(self, file):
        df = pd.read_csv(file, index_col=0)
        return df
