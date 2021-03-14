{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.8.5 64-bit ('covid': pipenv)",
   "metadata": {
    "interpreter": {
     "hash": "40f24880dc83019c30db16cc638ca1ae07502c8c6b3d9394a009f1d54cd49bf9"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "data1 = pd.read_excel ('weekly-deaths-by-location-age-group-sex-15-19.xlsx',\n",
    "        sheet_name='Data',\n",
    "        skiprows=4,\n",
    "        skipfooter=2,\n",
    "        usecols='A:F',\n",
    "        header=None,\n",
    "        names=['year','week','location','sex','age','deaths'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data1['cause'] = ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data2 = pd.read_excel ('weekly-deaths-by-location-age-sex.xlsx',\n",
    "        sheet_name='Data',\n",
    "        skiprows=4,\n",
    "        skipfooter=2,\n",
    "        usecols='A:F',\n",
    "        header=None,\n",
    "        names=['yearweek','location','sex','age','cause','deaths'])\n",
    "\n",
    "data2['year'] = data2.yearweek.str.slice(0,2).astype(int)\n",
    "data2['week'] = data2.yearweek.str.slice(3,5).astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data2['year'] = data2.yearweek.str.slice(0,2).astype(int)\n",
    "data2['week'] = data2.yearweek.str.slice(3,5).astype(int)\n",
    "\n",
    "del data2['yearweek']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "neworder =['year','week','location','sex','age','deaths','cause']\n",
    "data2 = data2.reindex(columns=neworder)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=data1.append(data2,ignore_index=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "w15 = data[data['year']==15]['week'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "w16 = data[data['year']==16]['week'].max()+w15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "w17 = data[data['year']==17]['week'].max()+w16"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "w18 = data[data['year']==18]['week'].max()+w17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "w19 = data[data['year']==19]['week'].max()+w18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "w20 = data[data['year']==20]['week'].max()+w19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.loc[data['year']==15,'week_abs']=data['week']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.loc[data['year']==16,'week_abs']=data['week']+w15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.loc[data['year']==17,'week_abs']=data['week']+w16"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.loc[data['year']==18,'week_abs']=data['week']+w17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.loc[data['year']==19,'week_abs']=data['week']+w18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.loc[data['year']==20,'week_abs']=data['week']+w19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.loc[data['year']==21,'week_abs']=data['week']+w20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby('week_abs').agg({'deaths':np.sum})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby('week_abs').agg({'deaths': np.sum,'week':np.min,'year':np.min})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby('week_abs').agg({'deaths': np.sum,'week':np.min,'year':np.min}).to_csv('weekly-2021-9.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}