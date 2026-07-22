"""
Booking module for Nova
Handles ticket booking and reservation integration
"""

import logging
import webbrowser
from datetime import datetime

logger = logging.getLogger(__name__)


class BookingHandler:
    """Handle booking and ticket reservations"""
    
    def __init__(self, config):
        """
        Initialize booking handler
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.booking_sites = {
            "flight": "https://www.skyscanner.com",
            "hotel": "https://www.booking.com",
            "train": "https://www.omio.com",
            "bus": "https://www.busbud.com",
            "movie": "https://www.fandango.com",
            "restaurant": "https://www.opentable.com",
            "event": "https://www.ticketmaster.com",
        }
        
        logger.info("BookingHandler initialized")
    
    def book_flight(self, origin=None, destination=None, date=None):
        """
        Open flight booking
        
        Args:
            origin (str): Departure city
            destination (str): Arrival city
            date (str): Travel date
        """
        try:
            url = self.booking_sites["flight"]
            
            if origin and destination:
                # Build search URL
                url = f"{url}?adults=1&children=0&infants=0&cabinclass=economy&rtn=&prefCurrency=USD"
                if origin:
                    url += f"&outboundOriginLocationCode={origin}"
                if destination:
                    url += f"&outboundDestinationLocationCode={destination}"
            
            webbrowser.open(url)
            logger.info(f"Flight booking opened: {origin} -> {destination}")
        
        except Exception as e:
            logger.error(f"Error booking flight: {str(e)}")
    
    def book_hotel(self, city=None, check_in=None, check_out=None):
        """
        Open hotel booking
        
        Args:
            city (str): Hotel location
            check_in (str): Check-in date
            check_out (str): Check-out date
        """
        try:
            url = self.booking_sites["hotel"]
            
            if city:
                url += f"?ss={city}"
            
            webbrowser.open(url)
            logger.info(f"Hotel booking opened: {city}")
        
        except Exception as e:
            logger.error(f"Error booking hotel: {str(e)}")
    
    def book_train(self, origin=None, destination=None, date=None):
        """
        Open train booking
        
        Args:
            origin (str): Departure city
            destination (str): Arrival city
            date (str): Travel date
        """
        try:
            url = self.booking_sites["train"]
            webbrowser.open(url)
            logger.info(f"Train booking opened: {origin} -> {destination}")
        
        except Exception as e:
            logger.error(f"Error booking train: {str(e)}")
    
    def book_movie(self, movie_name=None, location=None, date=None):
        """
        Open movie ticket booking
        
        Args:
            movie_name (str): Movie name
            location (str): Theater location
            date (str): Movie date
        """
        try:
            url = self.booking_sites["movie"]
            webbrowser.open(url)
            logger.info(f"Movie booking opened: {movie_name}")
        
        except Exception as e:
            logger.error(f"Error booking movie: {str(e)}")
    
    def book_restaurant(self, restaurant=None, date=None, time=None, party_size=None):
        """
        Open restaurant reservation
        
        Args:
            restaurant (str): Restaurant name
            date (str): Reservation date
            time (str): Reservation time
            party_size (int): Number of people
        """
        try:
            url = self.booking_sites["restaurant"]
            webbrowser.open(url)
            logger.info(f"Restaurant booking opened: {restaurant}")
        
        except Exception as e:
            logger.error(f"Error booking restaurant: {str(e)}")
    
    def book_event(self, event_name=None, location=None, date=None):
        """
        Open event ticket booking
        
        Args:
            event_name (str): Event name
            location (str): Event location
            date (str): Event date
        """
        try:
            url = self.booking_sites["event"]
            webbrowser.open(url)
            logger.info(f"Event booking opened: {event_name}")
        
        except Exception as e:
            logger.error(f"Error booking event: {str(e)}")
    
    def parse_booking_request(self, request_text):
        """
        Parse booking request from natural language
        
        Args:
            request_text (str): User request
            
        Returns:
            dict: Parsed booking details
        """
        try:
            request_lower = request_text.lower()
            
            booking_type = None
            details = {}
            
            if "flight" in request_lower or "book a flight" in request_lower:
                booking_type = "flight"
            elif "hotel" in request_lower or "book a hotel" in request_lower:
                booking_type = "hotel"
            elif "train" in request_lower or "book a train" in request_lower:
                booking_type = "train"
            elif "movie" in request_lower or "movie ticket" in request_lower:
                booking_type = "movie"
            elif "restaurant" in request_lower or "make a reservation" in request_lower:
                booking_type = "restaurant"
            elif "event" in request_lower or "ticket" in request_lower:
                booking_type = "event"
            
            logger.info(f"Parsed booking type: {booking_type}")
            return {"type": booking_type, "details": details}
        
        except Exception as e:
            logger.error(f"Error parsing booking request: {str(e)}")
            return None
