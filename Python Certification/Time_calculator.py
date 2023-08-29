def add_time(start, duration,day=''):
    # spliting start for time and day period (AM/PM)
    split_start = start.split()
    time = split_start[0]
    day_period = split_start[1]

    # splitting time for hours and minutes
    split_time = time.split(':')
    hours = int(split_time[0])
    minutes = int(split_time[1])

    # spliting duration for hours and minutes
    split_duration = duration.split(':')
    hours2 = int(split_duration[0])
    minutes2 = int(split_duration[1])

    # sum hours and minutes
    sum_hours = hours + hours2
    sum_minutes = minutes + minutes2

    if sum_minutes >= 60:
        sum_hours += 1
        sum_minutes -= 60

    # days
    n_days = 0
    future_days = ''
    # changing day period
    if sum_hours == 12 and day_period == "AM":
      day_period = "PM"
    elif sum_hours == 12 and day_period == "PM":
      day_period = "AM"
      
    while sum_hours > 12:
        if sum_hours >= 24:
            sum_hours -= 24
            n_days += 1
        if sum_hours >= 12 and day_period == "PM":
            if sum_hours >=13:
              sum_hours -= 12
            day_period = "AM"
            n_days += 1

        elif sum_hours >=12 and day_period == "AM":
            if sum_hours >=13:
              sum_hours -= 12
            day_period = "PM"

    # next day and n days later
    if n_days == 1:
        future_days = ' (next day)'
      
    elif n_days > 1:
        future_days = ' ({} days later)'.format(n_days)
    
    # sum up everything
    if sum_minutes < 10:
          sum_minutes = '0' + str(sum_minutes)
      
    if day == '':
        new_time = str(sum_hours)+ ':' + str(sum_minutes) + ' ' + day_period + future_days
      
    else:
        # Setting day of the week
        week = ["Monday","Tuesday","Wednesday",'Thursday',"Friday","Saturday","Sunday"]
        formated_day = day.capitalize()
        day_index = week.index(formated_day)
      
        # repeating week
        while day_index + n_days >= 6:
            day_index -= 7
        day = week[day_index + n_days]

        new_time = str(sum_hours)+ ':' + str(sum_minutes) + ' ' + day_period + ', ' + day + future_days
        
    return new_time