from .exceptions import RadiusError

def radius_valid(radius):
    # Runs checks for the criteria of the radius
    if not isinstance(radius, (int, float)):
        raise RadiusError("Radius must be a number and/or integer.")
    if radius <= 0:
        raise RadiusError("Radius cannot be negative, enter value greater than 0.")