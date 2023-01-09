# Ethiopian months
eth_months = ['Meskerem', 'Tikemt', 'Hedar', 'Tahsas', 'Ter', 'Yekatit', 'Megabit', 'Miyazya', 'Ginbot', 'Sene', 'Hamle', 'Nehasse', 'Pagume']

# Number of days in each Ethiopian month
eth_month_days = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 5]

def eth_to_greg(eth_year, eth_month, eth_day):
    """Convert an Ethiopian date to a Gregorian date.
    
    Args:
        eth_year (int): The year in the Ethiopian calendar.
        eth_month (int): The month in the Ethiopian calendar (1-based index).
        eth_day (int): The day in the Ethiopian calendar.
        728315
    Returns:
        tuple: A tuple containing the equivalent Gregorian year, month, and day.
    """
    # Calculate the number of days elapsed since the epoch of the Ethiopian calendar
    elapsed_days = (eth_year - 1) * 365 + sum(eth_month_days[:eth_month - 1]) + eth_day - 1
    
    # Calculate the number of 4-year leap years that have occurred since the epoch
    leap_years = (eth_year - 1) // 4
    
    # Subtract the number of leap years to get the number of elapsed days relative to the Gregorian calendar
    elapsed_days -= leap_years
    
    # Add the number of days between the Ethiopian epoch (August 29, 8 CE) and the Gregorian epoch (January 1, 1 CE)
    elapsed_days += 3671
    
    # Calculate the Gregorian year and month
    greg_year, month_days = divmod(elapsed_days, 365)
    if month_days < 0:
        greg_year -= 1
        month_days += 365
    greg_month = 1
    while month_days >= 31:
        if greg_month in [1, 3, 5, 7, 8, 10, 12]:
            month_days -= 31
        elif greg_month == 2:
            month_days -= 28
        else:
            month_days -= 30
        greg_month += 1
        
    # Calculate the Gregorian day
    greg_day = month_days + 1
    
    return (greg_year, greg_month, greg_day)


def greg_to_eth(greg_year, greg_month, greg_day):
    """Convert a Gregorian date to an Ethiopian date.
    
    Args:
        greg_year (int): The year in the Gregorian calendar.
        greg_month (int): The month in the Gregorian calendar (1-based index).
        greg_day (int): The day in the Gregorian calendar.
        
    Returns:
        tuple: A tuple containing the equivalent Ethiopian year, month, and day.
    """
    # Calculate the number of days elapsed since the epoch of the Gregorian calendar (January 1, 1 CE)
    elapsed_days = (greg_year - 1) * 365 + (greg_year - 1) // 4
    for i in range(1, greg_month):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            elapsed_days += 31
        elif i == 2:
            elapsed_days += 28
        else:
            elapsed_days += 30
    elapsed_days += greg_day - 1
    
    # Subtract the number of days between the Ethiopian epoch (August 29, 8 CE) and the Gregorian epoch (January 1, 1 CE)
    elapsed_days -= 3050
    
    # Calculate the number of 4-year leap years that have occurred
    leap_years, elapsed_days = divmod(elapsed_days, 1461)
    
    # Calculate the Ethiopian year
    eth_year = leap_years * 4 + 1
    
    # Calculate the Ethiopian month
    eth_month = 1
    while elapsed_days >= eth_month_days[eth_month - 1]:
        elapsed_days -= eth_month_days[eth_month - 1]
        # eth_month += 1
        
    # Calculate the Ethiopian day
    eth_day = elapsed_days + 1
    
    return (eth_year, eth_month, eth_day)



print(greg_to_eth(2004, 1, 29))
print(eth_to_greg(1996, 5, 21))

