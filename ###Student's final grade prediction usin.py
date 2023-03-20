###Student's final grade prediction using python and machine learning###
     # This Python 3 environment comes with many helpful analytics libraries installed
     # It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
     # For example, here's several helpful packages to load

     #This code is for importing two important libraries numpy and pandas for importing and manipulating
     #data. np is numerical python and pd is data manipulation library
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

     # Input data files are available in the read-only "../input/" directory
     # For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

     # You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
     # You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
###performed by Ghayur Hamza_19221_ECE###
/kaggle/input/d/datasets/larsen0966/student-performance-data-set/student-por.csv
##DATA INPUT
data=pd.read_csv("/kaggle/input/d/datasets/larsen0966/student-performance-data-set/student-por.csv") #path of the dataset for students performance in portuguese language class
#code for dataset loading or reading , here data is a name , can be given any name to a read a dataset
# we are trying to read the dataset by running this code
data.head()
#data visualization using matplotlib and seaborn
import seaborn as sns 
import matplotlib.pyplot as plt
b=sns.countplot(data['G3']) #counts the number of students for a grade recieved
b.axes.set_title('Final grade of students',fontsize=30) #title of the plot
b.set_xlabel('Final Grade',fontsize=20) # x axis
b.set_ylabel('Count',fontsize=20)#y axis
plt.show