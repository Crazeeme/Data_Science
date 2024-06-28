# -*- coding: utf-8 -*-
"""Data Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fYX4r3sKZb-GoGmBirxFTe-RUlx4O2ry
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# %matplotlib inline

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

plt.plot(yield_apples)

plt.plot(yield_apples);  # add ';' to omit the output in []

years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

plt.plot(years, yield_apples);
plt.xlabel('years');
plt.ylabel('yield_of_apples');

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]

plt.plot(years, apples);
plt.plot(years, oranges);
plt.xlabel('years');
plt.ylabel('yield');
plt.title('Apples and oranges');
plt.legend(['apples', 'oranges']);

plt.plot(years, apples, c='b', marker='o', ls='--', lw=2, ms=5, mec='black', mfc='white', mew=2, alpha=1 );
plt.plot(years, oranges, 'o--b', lw=2, ms=5, mec='black', mfc='white', mew=2, alpha=0.4 );

# if linestyle is not specified , only markers will be plotted
plt.plot(years, oranges, 'or')
plt.title("Yield of Oranges (tons per hectare)");

plt.figure(figsize=(4, 6))

plt.plot(years, oranges, 'or')
plt.title("Yield of Oranges (tons per hectare)");

sns.set_style('whitegrid')   # can have 'darkgrid'

plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']);

# global code
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (9, 5)
plt.rcParams['figure.facecolor'] = '#00000000'

# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
print(flowers_df)

flowers_df['species'].unique()

plt.plot(flowers_df.sepal_length, flowers_df.sepal_width);

sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width);

# 2 methods to obtain the scatterplot:-

# 1
# sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100);

#2
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', s=100, data=flowers_df);


plt.title('Sepal Dimensions');

plt.hist(flowers_df.sepal_width);

# Specifying the number of bins
plt.hist(flowers_df.sepal_width, bins=5);

# Specifying the boundaries of each bin
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25));

# Bins of unequal sizes
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5]);

# creating separate df for species

setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.legend(['setosa', 'versicolor']);

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],
         bins=np.arange(2, 5, 0.25),
         stacked=True);

plt.title('sepal width of iris flowers');
plt.xlabel('sepal width (cm)');
plt.ylabel('count');
plt.legend(['sentosa', 'versicolor', 'virginica']);

print(years, oranges)
plt.bar(years, oranges);

print(apples)
plt.bar(years, apples)
plt.bar(years, oranges, bottom=apples);

tips_df = sns.load_dataset("tips");

tips_df

sns.barplot(x='day', y='total_bill', data=tips_df);

sns.barplot(x='day', y='total_bill',hue = 'sex', data=tips_df);

sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df);

flights_df = sns.load_dataset("flights").pivot(index="month", values="passengers", columns="year")

flights_df

plt.title('No. of passengers in 1000s');
sns.heatmap(flights_df);

sns.heatmap(flights_df, cmap='plasma', annot=True, fmt='d');

sns.heatmap(flights_df, cmap='inferno', annot=True, fmt='d');

sns.heatmap(flights_df, cmap='coolwarm', annot=True, fmt='d');

sns.heatmap(flights_df, cmap='viridis', annot=True, fmt='d');

from urllib.request import urlretrieve

urlretrieve('https://fileinfo.com/img/ss/xl/jpg_44-2.jpg', 'chart.jpg');

from PIL import Image

img = Image.open('chart.jpg')

img_array = np.array(img)

img_array.shape

plt.imshow(img);

plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img);

# by slicing the array, we can get part of the image

plt.grid(False)
plt.axis('off')
plt.imshow(img_array[125:325,105:305]);

#@title Plotting multiple charts in a grid

fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# Use the axes for plotting
axes[0,0].plot(years, apples, 's-b')
axes[0,0].plot(years, oranges, 'o--r')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Yield (tons per hectare)')
axes[0,0].legend(['Apples', 'Oranges']);
axes[0,0].set_title('Crop Yields in Kanto')


# Pass the axes into seaborn
axes[0,1].set_title('Sepal Length vs. Sepal Width')
sns.scatterplot(x=flowers_df.sepal_length,
                y=flowers_df.sepal_width,
                hue=flowers_df.species,
                s=100,
                ax=axes[0,1]);

# Use the axes for plotting
axes[0,2].set_title('Distribution of Sepal Width')
axes[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],
         bins=np.arange(2, 5, 0.25),
         stacked=True);

axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica']);

# Pass the axes into seaborn
axes[1,0].set_title('Restaurant bills')
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0]);

# Pass the axes into seaborn
axes[1,1].set_title('Flight traffic')
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1]);

# Plot an image using the axes
axes[1,2].set_title('Data Science Meme')
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xticks([])
axes[1,2].set_yticks([])

plt.tight_layout(pad=2);

sns.pairplot(flowers_df, hue='species')

sns.pairplot(tips_df, hue='sex');