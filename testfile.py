from SphereCalculator import main, exceptions

try:
    r_var = int(input("Insert a number: "))
    sphere_volume = main.sphereVolume(r_var) #Calculates the Volume using variable "r_var"
    print("Radius = ", r_var)
    print("Volume = ", sphere_volume)
    
except exceptions.RadiusError() as sys_error:
    print("An Error has occured: ", sys_error)