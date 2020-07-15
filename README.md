### 13th July 2020
# Explore US Bikeshare Data Project

This project is used to build an interactive environment in which users can select data filters to compute a variety of descriptive statistics about bike share usage patterns in the three US cities of Chicago, New York City, and Washington, DC.

## Files used
* bikeshare.py
* chicago.csv
* new_york_city.csv
* washington.csv

## Software used
* Python 3.6 using [Anaconda](https://www.anaconda.com/products/individual#windows) (NumPy and Panda are included)
* [Atom](https://atom.io/) text editor
* [Git](https://git-scm.com/download/win) Bash terminal application

## Detailed description

#### An Interactive Experience
The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
1. Would you like to filter the data by month, day, or not at all?
1. (If they chose month) Which month - January, February, March, April, May, or June?
1. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

#### Statistics Computed

**#1 Popular times of travel** *(i.e., occurs most often in the start time)*
* most common month
* most common day of week
* most common hour of day

**#2 Popular stations and trip**

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**

* total travel time
* average travel time

**#4 User info**

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)
