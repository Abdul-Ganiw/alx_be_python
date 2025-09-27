def display_current_datetime():
    from datetime import datetime
    current_date = datetime.now()
    print("Current date and time:", current_date)


number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(number_of_days):
    from datetime import datetime, timedelta
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date}")

