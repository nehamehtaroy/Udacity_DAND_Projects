import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'C:/Neha/Udacity/BikeShare/new_york_city.csv',
              'washington': 'C:/Neha/Udacity/BikeShare/washington.csv'}

def select_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze

    """
    city = input('Enter the city name for which you want to explore BikeShare data.'
                  'Would you like to see data for Chicago, New York, or Washington?\n').title()
    if city.lower() == 'chicago' or city.lower() == 'c':

        return "chicago"

    elif city.lower() == 'new york' or city.lower() == 'n':

        return "new york"

    elif city.lower() == 'washington' or city.lower() == 'w':

        return "washington"

    else:

        print("\nI'm sorry, I'm not sure which city you're referring to. Let's try again.")

        return select_city()

def select_month():
    """
        Asks user to specify the month for which the data is required.

        Returns:
            (str) String representation of month number, e.g. for January, it returns '01'
    """

    month = input('\nEnter the month for which you want to see the BikeShare data.'
        'January, February, March, April, May, or June?\n').title()
    if month == 'January':

        return 'January'

    elif month == 'February':

        return 'February'

    elif month == 'March':

        return 'March'

    elif month == 'April':

        return 'April'

    elif month == 'May':

        return 'May'

    elif month == 'June':

        return 'June'

    else:

        print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again.")

        return select_month()

def select_day():
    """
         Asks user to specify the day of the week for which the data is required.

        Returns:
           (int) Integer representation of the day of the week, e.g. for Monday it returns 0
        """
    day_of_week = input(
        '\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()

    if day_of_week == 'Monday':

        return "Monday"

    elif day_of_week == 'Tuesday':

        return "Tuesday"

    elif day_of_week == 'Wednesday':

        return "Wednesday"

    elif day_of_week == 'Thursday':

        return "Thursday"

    elif day_of_week == 'Friday':

        return "Friday"

    elif day_of_week == 'Saturday':

        return "Saturday"

    elif day_of_week == 'Sunday':

        return "Sunday"

    else:

        print("\nI'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again.")

        return select_day()

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
    if city.lower() == "chicago" or city.lower() == "c":
        filename = 'C:\\Neha\\Udacity\\BikeShare\\chicago.csv'
    elif city.lower() == "New York" or city.lower() == "new york":
        filename = 'C:\\Neha\\Udacity\\BikeShare\\new_york_city.csv'
    elif city.lower() == "Washington" or city.lower() == "washington":
        filename = 'C:\\Neha\\Udacity\\BikeShare\\washington.csv'
    # load data file into a dataframe
    #df = pd.read_csv(CITY_DATA["city"])
    df = pd.read_csv(filename)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    # display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day

    # find the most popular month
    popular_day = df['day'].mode()[0]

    print('Most Popular Day:', popular_day)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    most_popular_start_station = "\nMost popular start station: " + sorted_start_stations.index[0]

    # display most commonly used end station
    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    most_popular_end_station = "Most popular end station: " + sorted_end_stations.index[0]

    # display most frequent combination of start station and end station trip
    trip_counts = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    sorted_trip_stations = trip_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    print("Most popular trip: " + "\n  Start station: " + str(sorted_trip_stations.index[0][0]) + "\n  End station: " + str(
        sorted_trip_stations.index[0][1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # display mean travel time
    total_trip_duration = df['Trip Duration'].sum()

    avg_trip_duration = df['Trip Duration'].mean()

    m, s = divmod(total_trip_duration, 60)

    h, m = divmod(m, 60)

    d, h = divmod(h, 24)

    y, d = divmod(d, 365)

    total_trip_duration = print("\nTotal trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s))

    m, s = divmod(avg_trip_duration, 60)

    h, m = divmod(m, 60)

    avg_trip_duration = print("Average trip duration: %d hrs %02d min %02d sec" % (h, m, s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # Display counts of gender
    if city != "washington":
        gender_count = df['Gender'].value_counts()

        print(gender_count)

        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("Earliest year of birth: ", earliest_year)

        recent_year = df['Birth Year'].max()
        print("Most recent year of birth: ", recent_year)

        common_year = df['Birth Year'].mode()
        print("Most common year of birth: ", common_year)


def bikeShare():
    while True:
        print("\n Welcome to BikeShare project!\n")
        city = select_city()
        ctrl=filterdata()
        if ctrl == 1:
            month = select_month()
            day = "all"
        elif ctrl == 2:
            day = select_day()
            month = "all"
        elif ctrl == 3:
            day = "all"
            month = "all"
        df = load_data(city, month, day)
        print("Here are the BikeShare details for: ", city)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        #if city != "washington":
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


def filterdata():
    filterdatas = input("Would you like to filter the data by Month, Day, or not at all? Type 'none' for no time filters\n")

    if filterdatas.lower() == "month":
        return 1
    elif filterdatas.lower() == "day":
        return 2
    elif filterdatas.lower() == "none":
        return 3
    else:
        print("I am sorry! Invalid input. Please try again.")
        filterdata()

if __name__ == "__main__":
    bikeShare()
