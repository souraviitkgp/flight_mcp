import sys
import os
tpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(f"Appending path: {tpath}")
sys.path.append(tpath)


from fastmcp import FastMCP
from lib.flight_search import search_flights, make_booking, get_booking_details

mcp = FastMCP("Flight MCP Server")

@mcp.tool
def flight_search_tool(query: dict) -> list:
    """
    Searches for flights based on the query.

    Args:
        query (dict): A dictionary containing search parameters such as:
            - origin (str): The origin city or airport.
            - destination (str): The destination city or airport.
            - date (str): The date of travel in 'YYYY-MM-DD' format.
            - passengers (int): The number of passengers.

    Returns:
        list: A list of dictionaries, each representing a flight with the following keys:
            - flight (str): Flight identifier.
            - origin (str): Origin city or airport.
            - destination (str): Destination city or airport.
            - departure (str): Departure time.
            - arrival (str): Arrival time.
            - price (str): Price of the flight.
            - date (str): Date of travel.
            - passengers (int): Number of passengers.

    Example:
        >>> search_flights({"origin": "New York", "destination": "Los Angeles", "date": "2025-09-28", "passengers": 1})
        [
            {
                "flight": "Flight 123",
                "origin": "New York",
                "destination": "Los Angeles",
                "departure": "10:00 AM",
                "arrival": "1:00 PM",
                "price": "$300",
                "date": "2025-09-28",
                "passengers": 1
            },
            ...
        ]
    """
    return search_flights(query)

@mcp.tool
def make_booking_tool(booking_details: dict) -> dict:
    """
    Creates a flight booking based on the provided details.

    This function simulates booking a flight and returns a confirmation.

    Args:
        booking_details (dict): A dictionary containing flight and passenger details such as:
            - flight (str): Flight identifier.
            - passenger_name (str): Name of the passenger.
            - price (str): Price of the flight.
            - date (str): Date of travel in 'YYYY-MM-DD' format.
            - origin (str): Origin city or airport.
            - destination (str): Destination city or airport.

    Returns:
        dict: A dictionary representing the booking confirmation with the following keys:
            - booking_id (str): Unique identifier for the booking.
            - status (str): Status of the booking (e.g., 'Confirmed').
            - flight (str): Flight identifier.
            - passenger_name (str): Name of the passenger.
            - price (str): Price of the flight.
            - date (str): Date of travel.
            - origin (str): Origin city or airport.
            - destination (str): Destination city or airport.

    Example:
        >>> make_booking({"flight": "Flight 123", "passenger_name": "John Doe", "price": "$300", "date": "2025-09-28", "origin": "New York", "destination": "Los Angeles"})
        {
            "booking_id": "BK1234",
            "status": "Confirmed",
            "flight": "Flight 123",
            "passenger_name": "John Doe",
            "price": "$300",
            "date": "2025-09-28",
            "origin": "New York",
            "destination": "Los Angeles"
        }
    """
    return make_booking(booking_details)

@mcp.tool
def get_booking_details_tool(booking_id: str) -> dict:
    """Retrieves booking details for the given booking ID.

    Args:
        booking_id (str): The ID of the booking to retrieve details for.

    Returns:
        dict: A dictionary representing the booking details.
    """
    return get_booking_details(booking_id)

if __name__ == "__main__":
    mcp.run(transport="http", port=8000, log_level="DEBUG")