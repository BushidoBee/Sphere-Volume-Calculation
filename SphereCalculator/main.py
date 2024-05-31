from .verification import radius_valid
from .log_file import loggercalc
from .calculations import volumecalc

def sphereVolume(radius):
    try:
        radius_valid(radius) # Verify a valid Radius entry
        calcVol = volumecalc(radius) # Use "radius" to calculate the volume of the Sphere
        loggercalc(radius, calcVol, None) # Create a new line the successful calculation
        return calcVol
    except Exception as failure:
        loggercalc(radius, None, err=str(failure)) # Create a new line for the error that occured
        raise


if __name__ == "__main__":
    r_var = 10
    print("Radius = ", r_var)
    print("Volume = ", sphereVolume(r_var))