#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

# load dataframes from oakland's format
def load_michigan_data(dirname):
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

# compute the total vote counts from both types of ballot
def compute_totals(i,s):
    return pd.DataFrame({
        'total_d': i['D.Total'] + s['D.Total'],
        'total_r': i['R.Total'] + s['R.Total'],
        'total_v': i['Total'] + s['Total']
        })

def build_plots(i,s,t):
    return pd.DataFrame({
        'frac_r': t['total_r'] / t['total_v'],
        'frac_d': t['total_d'] / t['total_v'],
        'frac_sr': s['R.Total'] / t['total_v'],
        'frac_ir': i['R.Total'] / t['total_v'],
        'frac_sd': s['D.Total'] / t['total_v'],
        'frac_id': i['D.Total'] / t['total_v'],
        })

def run():
    (oakland_i, oakland_s) = load_michigan_data('../source-data/oakland-mi-11-11-2020/')

    oakland_totals = compute_totals(oakland_i, oakland_s)

    cons = build_plots(oakland_i, oakland_s, oakland_totals)

    plt.figure(1)
    ax = plt.gca()
    cons.plot(kind='scatter', x='frac_r', y='frac_sr', color='red', ax=ax)
    cons.plot(kind='scatter', x='frac_r', y='frac_ir', color='blue', ax=ax)

    plt.figure(2)
    ax = plt.gca()
    cons.plot(kind='scatter', x='frac_d', y='frac_sd', color='red', ax=ax)
    cons.plot(kind='scatter', x='frac_d', y='frac_id', color='blue', ax=ax)
    plt.show()

    
