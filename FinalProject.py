import sys

if len(sys.argv) == 1:
    # giving the user a usage error message if they do not have any mode seected
    print('Usage: python3 Pro.py "MODE". \n To view all the options use list instead of mode\n')

def main():
    # make mode command line argument 
    mode = sys.argv[1]

    # putting all equations into proper casing
    if mode == "list":
        print('\n 1. acceleration\n 2. velocity\n 3. root2\n 4 rootx\n 5. force\n 6. power\n 7. density\n 8. potential_energy or PE\n 9. kinetic_energy or KE\n 10. elastic_energy or EE')
        print('Use mode: equations for a full list of all equations')
        print(' ** Please use same casing\n')

    # equation printing mode
    if mode == 'equations':
        print('Root 2 : N^2\n\n Root x: N^x\n\n Velocity: distance/time\n\n Acceleration: Final velocity - initial velocity / time\n\n Force: Mass * Acceleration\n\n Power: Work / time\n\n Density: Mass / Volume\n\n Potential Energy: Mass * Gravity * Height \n\n Kinetic Energy: 1/2 Mass * Velocity^2 \n\n Elastic Energy: 1/2 spring_constant * extention^2 \n\n')

    # for square root equations
    if mode == 'root2':
        num = float(input('Enter a number = '))
        sqrt = num ** 0.5
        print('The square root of %0.3f is %0.3f' % (num, sqrt))
    
    # x root equation
    if mode == 'rootx':
        num = float(input ('Enter a number = '))
        degree_of_root = float(input('Degree of Root = '))
        xroot = num ** (1/degree_of_root)
        print('Root %.0f of %o.3f is %0.3f' % (degree_of_root, num, xroot))
        return

    # Velocity equation
    if mode == 'velocity':
        displacement = input('Displacement(m) = ')
        time = input('Time(s) = ')
    # used a float because there are strings
        velocity = float (displacement) / float(time)
        print(f'Velocity = {velocity} m/s')
        return

    #acceleration equation
    if mode == 'acceleration':
        int_velocity = input ('Initial Velocity(m/s) = ')
        fin_velocity = input ('Final Velocity(m/s) = ')
        time = input ('Time(s) = ')
    # used a float because there are strIngs
        acceleration = (float(fin_velocity) - float(int_velocity)) / float(time)
    #printing acceleration
        print('Acceleration = %0.3f m/s^2' % (acceleration))
        return

    # force equation
    if mode == 'force':
        mass = input('Mass(g) = ')
        accelerationf = input('Acceleration(m/s^2) = ')
        force = float(mass) * float(accelerationf)
        print('Force(N) = %0.3f N ' % (force))

    # power formula
    if mode == 'power':
        work_done = input('Work Done(J) = ')
        time = input('Time Taken(s) = ')
        power = float(work_done) / float(time)
        print('Power(W) = %0.3f' % power)

    # density formula
    if mode == 'density':
        mass = input('Mass(g) = ')
        volume = input('Volume(cm^3) = ')
        density = float(mass) / float(volume)
        print('Density(p) = %0.3f' % (density))

    # potential energy formula
    if (mode == 'potential_energy' or mode == 'PE'):
        print('Gravity = 9.81 m/s^2')
        gravity = 9.81
        mass = input('Mass(g) = ')
        height = input('Height(m) = ')
        PE = float(mass) * float(gravity) * float(height)
        print('Potential Energy(J) = %.2f' %(PE))



if __name__ == "__main__":
    main()