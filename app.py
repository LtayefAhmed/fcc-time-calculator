def add_time(start,duration,start_day=None):
    start_time,period=start.split()
    start_hour,start_minute=map(int,start_time.split(':'))
    duration_hour,duration_minute=map(int,duration.split(':'))
    if period == 'PM' and start_hour !=12:
        start_hour+=12
    if period =='AM' and start_hour ==12:
        start_hour=0
    end_minute=start_minute+duration_minute
    end_hour=start_hour+duration_hour

    if end_minute >=60:
        end_hour+=end_minute//60
        end_minute%=60
    days_later=end_hour//24
    final_hour=end_hour%24
    
    period= 'AM' if final_hour<12 or final_hour==24 else 'PM'
    display_hour=final_hour%12
    if display_hour==0:
        display_hour=12
    days_of_week = [
        "monday", "tuesday", "wednesday", "thursday", 
        "friday", "saturday", "sunday"
    ]
    new_day=''
    if start_day:
         start_day_lower=start_day.lower() 
         start_day_index=days_of_week.index(start_day_lower)
         new_day_index=(start_day_index+days_later)%7
         new_day_name=days_of_week[new_day_index]
         new_day=','+new_day_name.capitalize()

    display_minute=str(end_minute).zfill(2)
    new_time=f"{display_hour}:{display_minute} {period}"
    new_time+=new_day
    if days_later==1:
        new_time+=' (next day)'

    elif days_later>1:
        new_time+=f' ({days_later} days later)'
    return new_time
add_time('3:30 PM', '2:12')