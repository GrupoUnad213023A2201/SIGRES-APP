# --- Custom Exceptions ---
class ReservationError(Exception):
    """Base class for reservation-related exceptions."""
    pass

class ReservationStatusError(ReservationError):
    """Raised when a status transition is invalid."""
    pass


# --- Reservation Class ---
class Reservation:
    def __init__(self, reservation_id, customer, date, details):
        self.reservation_id = reservation_id
        self.customer = customer  # Expected to be a Customer object
        self.date = date
        self.details = details
        self.status = "Pending"  # Possible statuses: Pending, Confirmed, Canceled

    def confirm(self):
        """Confirms the reservation if it's currently Pending."""
        if self.status == "Confirmed":
            raise ReservationStatusError(f"Reservation {self.reservation_id} is already confirmed.")
        elif self.status == "Canceled":
            raise ReservationStatusError(f"Cannot confirm reservation {self.reservation_id} because it was canceled.")
        
        self.status = "Confirmed"
        print(f"Success: Reservation {self.reservation_id} confirmed for {self.customer.name}.")

    def cancel(self):
        """Cancels the reservation if it's not already canceled."""
        if self.status == "Canceled":
            raise ReservationStatusError(f"Reservation {self.reservation_id} is already canceled.")
        
        self.status = "Canceled"
        print(f"Success: Reservation {self.reservation_id} has been canceled.")

    def __str__(self):
        return f"Reservation #{self.reservation_id} | Status: {self.status} | Date: {self.date} | Customer: {self.customer.name}"