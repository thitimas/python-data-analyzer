#implement functions for median and standard deviationst 
#input parameters: list of times and temperatures from the external API

import statistics
def calculate_median(temperatures):
    if not temperatures:
        return None
    return statistics.median(temperatures)  

def calculate_standard_deviation(temperatures):
    if not temperatures:
        return None
    return statistics.stdev(temperatures)   

def analyze_time_series(times, temperatures):
    median_temp = calculate_median(temperatures)
    stddev_temp = calculate_standard_deviation(temperatures)
    #return minx, max, average, median, stddev
    #return the time for the min and max temperatures as well
    min_temp_time = times[temperatures.index(min(temperatures))] if temperatures else None
    max_temp_time = times[temperatures.index(max(temperatures))] if temperatures else None

    return {
        "median": median_temp,
        "stddev": stddev_temp, 
        "min": min(temperatures),
        "min_time": min_temp_time,
        "max": max(temperatures),
        "max_time": max_temp_time,
        "average": sum(temperatures) / len(temperatures) if temperatures else None
    }
  

