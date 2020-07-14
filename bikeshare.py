import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_options = ['january', 'february', 'march', 'april', 'may', 'june']
day_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filter_values(selection, question, options):
    """
    Validates city, month and/or day user selections.

    Returns:
        (str) selection - month/day filter
        (str) question - interactive question asking user about month/day choices
        (str) options - list of valid months/days
    """
    reentry = True

    while reentry == True:
        output = input(question).lower()
        if output in options:
            reentry = False
            return output
        else:
            print('Please enter a valid input.')
            
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    ques_month = 'Which month - January, February, March, April, May, or June?\n'
    ques_day = 'Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n'
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        # Get user input for city (chicago, new york city, washington). 
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        if city.lower() in CITY_DATA:
            break
        else:
            print('Please enter a valid city name.')
                
    while True:
        # Get user selection of month, day, both or none filters.    
        input_filter = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter.\n')
        
        if input_filter.lower() == 'month':
            # Get user input for month (all, january, february, ... , june)
            month = get_filter_values('month',ques_month,month_options)
            day = 'all'
            break
        elif input_filter.lower() == 'day':
            # Get user input for day of week (all, monday, tuesday, ... sunday)
            day = get_filter_values('day',ques_day,day_options)
            month = 'all'
            break
        elif input_filter.lower() == 'both':
            # Get user input for month (all, january, february, ... , june)
            month = get_filter_values('month',ques_month,month_options)
            
            # Get user input for day of week (all, monday, tuesday, ... sunday)
            day = get_filter_values('day',ques_day,day_options)
            break    
        elif input_filter.lower() == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            print('Please select a valid filter.')        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month_options.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_freq_month = df['month'].mode()[0]
    
    # Display the most common day of week
    most_freq_day = df['day_of_week'].mode()[0]

    # Display the most common start hour
    most_freq_hour = df['Start Time'].dt.hour.mode()[0]

    print('\nThe most frequent month is %s' % most_freq_month)
    print('The most frequent day is %s' % most_freq_day)
    print('The most frequent hour is %s' % most_freq_hour)     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_freq_str_station = df['Start Station'].mode()[0]

    # Display most commonly used end station
    most_freq_end_station = df['End Station'].mode()[0]

    # Display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_freq_trip = df['trip'].mode()[0]

    print('\nThe most frequent start station is %s.' % most_freq_str_station)
    print('The most frequent end station is %s.' % most_freq_end_station)
    print('The most frequent trip is %s.' % most_freq_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

  
def convert(seconds): 
    """Converts seconds into days, hours, minutes and seconds."""
    
    minute, sec = divmod(seconds, 60) 
    hour, minute = divmod(minute, 60) 
    day, hour = divmod(hour, 24)
    
    return day, hour, minute, sec


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    tot_travel = df['Trip Duration'].sum()
    tot_days, tot_hours, tot_minutes, tot_seconds = convert(tot_travel)

    # Display mean travel time
    mean_travel = df['Trip Duration'].mean()
    mean_days, mean_hours, mean_minutes, mean_seconds = convert(int(mean_travel))

    print('\nTotal travel time is %s days, %s hours, %s minutes and %s seconds.' % (tot_days, tot_hours, tot_minutes, tot_seconds))
    print('Mean travel time is %s days, %s hours, %s minutes and %s seconds.' % (mean_days, mean_hours, mean_minutes, mean_seconds))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types and their corresponding counts are: \n%s.' % user_types)
    

    # Display counts of gender (Handle exception as gender is only available for Chicago and New York City)
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender types and their corresponding counts are: \n%s.' % gender_types)
    except KeyError:
        print('\nGender data is not available for the selected filters.')
        
        
    # Display earliest, most recent, and most common year of birth (Handle exception as birth year is only available for Chicago and New York City)
    try:
        earliest_birth_yr = df['Birth Year'].min()
        latest_birth_yr = df['Birth Year'].max()
        most_comm_birth_yr = df['Birth Year'].mode()[0]
        
        print('\nThe earliest birth year is %s.' % int(earliest_birth_yr))
        print('The most recent birth year is %s.' % int(latest_birth_yr))
        print('The most common birth year is %s.' % int(most_comm_birth_yr))
    except KeyError:
        print('\nBirth year data is not available for the selected filters.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """Displays raw data from the files."""

    # Get user input for displaying raw data. 
    raw_input = input('Would you like to see raw data? Please enter yes or no.\n')
    line_num = 0
    
    while raw_input.lower() == 'yes':
        print(df.iloc[line_num:line_num + 5])
        line_num += 5
        # Get user input for displaying more raw data. 
        raw_input = input('Would you like to see more raw data? Please enter yes or no.\n')
        
        if raw_input.lower() == 'no':
            return
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
