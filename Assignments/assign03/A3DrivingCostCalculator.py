# CS1400 Assignment 3: Driving Cost Calculator by Jana

# This program prompts the user for the price of gasoline and
# electricity per kilowatt-hour. It then uses these prices with
# typical fuel efficiency for a car, a truck and an electric
# vehicle to calculate and display cost of driving trips
# of various lengths.

#Calculate the cost of a trip for a gasoline-powered vehicle.
    # miles : float The length of the trip in miles.
    # mpg : float The vehicle's fuel efficiency in miles per gallon.
    # gas_cost : float The cost of one gallon of gasoline in dollars.
    # Returns the total cost of the trip in dollars.
def calculate_gas_vehicle_trip_cost(miles: float, mpg: float, gas_cost: float) -> float:
    # Calculate gallons needed and total cost
    gallons_needed = miles / mpg
    total_cost = gallons_needed * gas_cost
    return total_cost

# Calculate the cost of a trip for an electric vehicle.
# Returns: float The total cost of the trip in dollars.
def calculate_electric_vehicle_trip_cost(miles: float, whpm: float, kwh_cost: float) -> float:
    # Convert watt‑hours per mile to kilowatt‑hours per mile
    kwh_per_mile = whpm / 1000
    # Total kWh consumed on the trip
    total_kwh = kwh_per_mile * miles
    # Calculate total cost
    total_cost = total_kwh * kwh_cost
    return total_cost

# Gather input from the user and display trip cost estimates.
def main() -> None:

    # Ask user for cost inputs
    gas_price_input = input("Enter the price of gasoline in dollars per gallon: ")
    electricity_price_input = input("Enter the price of electricity in dollars per kilowatt-hour: ")

    gas_price = float(gas_price_input)
    electricity_price = float(electricity_price_input)

    # MPG for gas vehicles, WHPM for electric vehicle
    car_mpg = 24.4
    truck_mpg = 14.2
    ev_whpm = 229.0

    # Loop over trip distances and compute costs
    for distance in range(50, 501, 50):
        # Calculate costs for each vehicle type
        truck_cost = calculate_gas_vehicle_trip_cost(distance, truck_mpg, gas_price)
        car_cost = calculate_gas_vehicle_trip_cost(distance, car_mpg, gas_price)
        ev_cost = calculate_electric_vehicle_trip_cost(distance, ev_whpm, electricity_price)

        # Round costs to nearest whole number for display
        truck_cost_rounded = round(truck_cost)
        car_cost_rounded = round(car_cost)
        ev_cost_rounded = round(ev_cost)

        # Display the results
        print(
            "For a trip of " + str(distance) + " miles, the costs are: "
            " truck: " + str(truck_cost_rounded)," car: " + str(car_cost_rounded) +
            " electric: " + str(ev_cost_rounded))


if __name__ == "__main__":
    main()