from datetime import datetime, timedelta

def calculate_effective_hours(total_hours, total_minutes):
    login_time = input("Enter login time (HH:MM AM/PM): ")
    logout_time = input("Enter logout time (HH:MM AM/PM): ")

    # Convert login and logout times to datetime objects
    login_time = datetime.strptime(login_time, "%I:%M %p")
    logout_time = datetime.strptime(logout_time, "%I:%M %p")

    total_break_time = timedelta()  # Initialize total break time as 0

    while True:
        break_in_time = input("Enter break in time (HH:MM AM/PM) or 'stop' to exit: ")
        if break_in_time.lower() == 'stop':
            break
        break_out_time = input("Enter break out time (HH:MM AM/PM): ")

        # Convert break in and out times to datetime objects
        break_in_time = datetime.strptime(break_in_time, "%I:%M %p")
        break_out_time = datetime.strptime(break_out_time, "%I:%M %p")

        # Calculate the duration of the break
        break_duration = break_out_time - break_in_time

        # Add the break duration to the total break time
        total_break_time += break_duration

        # Calculate the elapsed time
        elapsed_time = break_out_time - login_time - total_break_time

        # Calculate the remaining time to stay
        remaining_time = timedelta(hours=total_hours, minutes=total_minutes) - elapsed_time
        remaining_hours = remaining_time.seconds // 3600
        remaining_minutes = (remaining_time.seconds % 3600) // 60

        print("Remaining time to stay: {} hours {} minutes".format(remaining_hours, remaining_minutes))

        # Calculate the time up to which we need to cover 7 hours 30 minutes
        Time_to_Leave = break_out_time + remaining_time
        Time_to_Leave_formatted = Time_to_Leave.strftime("%I:%M %p")
        print("Time To Leave: {}".format(Time_to_Leave_formatted))

    # Calculate the total duration
    total_duration = logout_time - login_time - total_break_time

    # Calculate the total hours and minutes
    hours = total_duration.seconds // 3600
    minutes = (total_duration.seconds % 3600) // 60

    return hours, minutes

# Example usage
total_hours = 7
total_minutes = 30
hours, minutes = calculate_effective_hours(total_hours, total_minutes)
print("Effective hours present: {} hours {} minutes".format(hours, minutes))