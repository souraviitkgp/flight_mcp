import unittest
from lib.flight_search import search_flights, make_booking, get_booking_details
from schemas.flight import FlightSearchRequest, FlightSearchResponse

class TestFlightSearch(unittest.TestCase):

    def test_search_flights(self):
        request = FlightSearchRequest(origin="JFK", destination="LHR")
        response = search_flights(request)

        self.assertIsInstance(response, FlightSearchResponse)
        self.assertEqual(len(response.flights), 1)
        self.assertEqual(response.flights[0]["flight_number"], "AI101")

    def test_make_booking(self):
        booking_details = {
            "flight": "Flight 123",
            "passenger_name": "John Doe",
            "price": "$300",
            "date": "2025-09-28",
            "origin": "New York",
            "destination": "Los Angeles"
        }
        response = make_booking(booking_details)

        self.assertIsInstance(response, dict)
        self.assertEqual(response["status"], "Confirmed")
        self.assertEqual(response["flight"], "Flight 123")

    def test_get_booking_details(self):
        booking_id = "BK1234"
        response = get_booking_details(booking_id)

        self.assertIsInstance(response, dict)
        self.assertEqual(response["booking_id"], booking_id)
        self.assertEqual(response["status"], "Confirmed")

if __name__ == "__main__":
    unittest.main()