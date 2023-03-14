def find_time_of_day(start_time):
    start_time = start_time[:5]
    start_time = start_time.replace(':', '.')
    start_time = float(start_time)
    
    if start_time < 4.00:
        return 'Twilight'
    elif start_time < 8.00:
        return 'Dawn'
    elif start_time < 12.00:
        return 'Morning'
    elif start_time < 16.00:
        return 'Afternoon'
    elif start_time < 20.00:
        return 'Evening'
    else: return 'Night'

print(find_time_of_day('01:35:55'))