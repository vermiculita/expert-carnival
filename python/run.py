#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

# load dataframes from oakland's format
def load_oakland_data(dirname):
    individual = pd.read_csv("%s/ballot-sheet.csv" % (dirname), skiprows=2)
    individual.rename(columns={
        "Absentee": "D.Absentee",
        "Election": "D.Election",
        "Total Votes": "D.Total",
        "Absentee.1": "R.Absentee",
        "Election.1": "R.Election",
        "Total Votes.1": "R.Total",
        }, inplace=True)
    
    straight = pd.read_csv("%s/straight-sheet.csv" % (dirname), skiprows=2)
    straight.rename(columns={
        "Absentee": "D.Absentee",
        "Election": "D.Election",
        "Total Votes": "D.Total",
        "Absentee.1": "R.Absentee",
        "Election.1": "R.Election",
        "Total Votes.1": "R.Total",
        }, inplace=True)

    return (individual, straight)

# load dataframes from our format
def load_our_data(dirname):
    individual = pd.read_csv("%s/data.csv" % (dirname))    
    straight = pd.read_csv("%s/data.csv" % (dirname))
    straight.rename(columns={
        "R.Total": "R.Total.Ind",
        "D.Total": "D.Total.Ind",
        "D.Total.Str": "D.Total",
        "R.Total.Str": "R.Total",
        }, inplace=True)

    return (individual, straight)

def build_plots(i,s):
    return pd.DataFrame({
        'frac_r': i['R.Total'] / i['Total'],
        'frac_d': i['D.Total'] / i['Total'],
        'frac_sr': s['R.Total'] / i['Total'],
        'frac_ir': (i['R.Total']-s['R.Total']) / i['Total'],
        'frac_sd': s['D.Total'] / i['Total'],
        'frac_id': (i['D.Total']-s['D.Total']) / i['Total'],
        })

def run():
    (oakland_i, oakland_s) = load_oakland_data('../source-data/oakland-mi-11-11-2020/')

    cons = build_plots(oakland_i, oakland_s)

    plt.figure(1)
    ax = plt.gca()
    cons.plot(kind='scatter', x='frac_r', y='frac_sr', color='red', ax=ax, label='Fraction Straight Ticket')
    cons.plot(kind='scatter', x='frac_r', y='frac_ir', color='blue', ax=ax, label='Fraction Individual')
    plt.legend();
    plt.title('Oakland County, Republican Votes')
    
    plt.figure(2)
    ax = plt.gca()
    cons.plot(kind='scatter', x='frac_d', y='frac_sd', color='red', ax=ax, label='Fraction Straight Ticket')
    cons.plot(kind='scatter', x='frac_d', y='frac_id', color='blue', ax=ax, label='Fraction Individual')
    plt.legend();
    plt.title('Oakland County, Democrat Votes')    

    (bay_i, bay_s) = load_our_data('../source-data/bay-county-mi-11-13-2020/')
    bay_cons = build_plots(bay_i, bay_s)

    plt.figure(3)
    ax = plt.gca()
    bay_cons.plot(kind='scatter', x='frac_r', y='frac_sr', color='red', ax=ax, label='Fraction Straight Ticket')
    bay_cons.plot(kind='scatter', x='frac_r', y='frac_ir', color='blue', ax=ax, label='Fraction Individual')
    plt.legend();
    plt.title('Bay County, Republican Votes')

    plt.figure(4)
    ax = plt.gca()
    bay_cons.plot(kind='scatter', x='frac_d', y='frac_sd', color='red', ax=ax, label='Fraction Straight Ticket')
    bay_cons.plot(kind='scatter', x='frac_d', y='frac_id', color='blue', ax=ax, label='Fraction Individual')
    plt.legend();
    plt.title('Bay County, Democrat Votes')
    
    plt.show()

    
