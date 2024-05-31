import logging

logging.basicConfig(filename='SphereVolumeLog.log', level=logging.INFO)
def loggercalc(rad, vol, err):
    if err:
        logging.error(f"ERROR: Computation Failure for Radius = {rad} | {err}")
    else:
        logging.info(f"COMPLETE >>> Radius = {rad} | Volume = {vol}")