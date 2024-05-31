from .verification import radius_valid
from .log_file import loggercalc
from .calculations import volumecalc

def sphereVolume(radius):
    try:
        radius_valid(radius)
        calcVol = volumecalc(radius)
        loggercalc(radius, calcVol, None)
        return calcVol
    except Exception as failure:
        loggercalc(radius, None, err=str(failure))
        raise


if __name__ == "__main__":
    r_var = 10
    print("Radius = ", r_var)
    print("Volume = ", sphereVolume(r_var))