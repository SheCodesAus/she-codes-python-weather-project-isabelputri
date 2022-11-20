import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"



def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    convert_date = datetime.fromisoformat(iso_string)
    date = convert_date.strftime("%A %d %B %Y")
    return date
    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = (float(temp_in_farenheit) - 32)*(5/9)
    return round(temp_in_celcius, 1)
    pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
# ---- Method 1 --------------------------------------------------------

    weather_data_float = [float(x) for x in weather_data]
    total = sum(weather_data_float)
    calculate_mean = total / len(weather_data_float)
    return calculate_mean

# ---- Method 2 --------------------------------------------------------

    #count = 0
    #for numbers in weather_data:
        #count += float(numbers)
    
    #mean = float(count/ len(weather_data))
    
    #return mean

    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather = [] #Creating an empty list

    with open(csv_file) as csv_file: #Opening the CSV file
        reader = csv.reader(csv_file) #Reading the CSV file
        next(reader) #Skipping the header/first line
        for line in reader: #For each row in the CSV
            if len(line) > 0: #If the row is not blank/empty
                weather.append([line[0], int(line[1]), int(line[2])])
                #Appending information from the row into the empty list by turning it into a sublist
                #Returning the right type of information --> min_temp and max_temp to an integer 
    # print (weather) #Checking if the list appears correctly according to the test
    return weather #Giving back the list for python to run       
    pass 

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """  
    if len(weather_data) != 0:
        min_index = 0
        min_val = weather_data[0]
        for i in range(len(weather_data)):
            if weather_data [i] <= min_val:
                min_val = (weather_data[i])
                min_index = i
        return (float(min_val), min_index)
    else:
        return ()

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

    if len(weather_data) != 0:
        max_index = 0
        max_val = weather_data[0]
        for i in range(len(weather_data)):
            if weather_data [i] >= max_val:
                max_val = (weather_data[i])
                max_index = i
        return (float(max_val), max_index)
    else:
        return ()
    pass

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.

    """
    min_temp = []
    max_temp = []

    for item in weather_data:
        min_temp.append(item[1])
        max_temp.append(item[2])
    
    total_days = len(weather_data)
    min_temp_c = output_temperature(find_min(min_temp)[0]) #1. Finding the (min value, min_index) --> getting the value only [0]
    max_temp_c = format_temperature(convert_f_to_c(find_max(max_temp)[0]))
    min_temp_date = convert_date(weather_data[(find_min(min_temp)[1])][0])
    max_temp_date = convert_date(weather_data[(find_max(max_temp)[1])][0])
    min_temp_mean = format_temperature(convert_f_to_c(calculate_mean(min_temp)))
    max_temp_mean = format_temperature(convert_f_to_c(calculate_mean(max_temp)))
    generate_summary = f"{total_days} Day Overview\n  The lowest temperature will be {min_temp_c}, and will occur on {min_temp_date}.\n  The highest temperature will be {max_temp_c}, and will occur on {max_temp_date}.\n  The average low this week is {min_temp_mean}.\n  The average high this week is {max_temp_mean}.\n"
    return (generate_summary)

def output_temperature(temperature):
    return format_temperature(convert_f_to_c(temperature))

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = []
    final_summary = ""
    for item in weather_data:
        formatted_date = convert_date(item[0])
        min_temp_c = convert_f_to_c(item[1])
        formatted_min_temp = format_temperature(min_temp_c)
        max_temp_c = convert_f_to_c(item[2])
        formatted_max_temp = format_temperature(max_temp_c)
        daily_summary.append([formatted_date, formatted_min_temp, formatted_max_temp])
    for individual_day in daily_summary:
        date = individual_day[0]
        individual_min = individual_day[1]
        individual_max = individual_day[2]
        daily_summary = f"---- {date} ----\n  Minimum Temperature: {individual_min}\n  Maximum Temperature: {individual_max}\n\n"
        final_summary += daily_summary
    return final_summary

    pass
