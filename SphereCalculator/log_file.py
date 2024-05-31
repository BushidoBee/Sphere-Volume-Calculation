import logging

logging.basicConfig(filename='SphereVolumeLog.log', level=logging.INFO) # Create/Add the current calculation to the log file 
def loggercalc(rad, vol, err):
    if err:
        logging.error(f"ERROR: Computation Failure for Radius = {rad} | {err}")
    else:
        logging.info(f"COMPLETE >>> Radius = {rad} | Volume = {vol}")