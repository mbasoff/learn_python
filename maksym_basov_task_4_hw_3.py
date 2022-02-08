import nums_from_string  # This library needs to get numbers from string

quantity_of_earth_days_and_hours: str = input("""количество_земных_дней, количество_часов """)
quantity_of_earth_days_and_hours: list = nums_from_string.get_nums(quantity_of_earth_days_and_hours)
quantity_of_earth_days: int = quantity_of_earth_days_and_hours[0]
quantity_of_earth_hours: int = quantity_of_earth_days_and_hours[1]

quantity_of_sols: float = quantity_of_earth_days * 1.02595675  # Quantity of marsian sols calculation
quantity_of_mars_hours: float = quantity_of_earth_hours * 1.02595675

print(round(quantity_of_sols, 2), 'солов', round(quantity_of_mars_hours, 2), 'марсианских часов')
