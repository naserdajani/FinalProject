import sys

if len(sys.argv) == 1:
# giving the user a usage error message if they do not have any mode seected
    print('Usage: python3 Pro.py "Mode". \n To view all the options use list instead of mode\n')

def main():
# make mode command line argument 
mode = sys.argv[1]

# putting all equations into proper casing
if mode == 'list'
    print('\n 1. acceleration\n 2. velocity\n 3. root2\n 4 rootx\n 5. force\n 6. power\n 7. density\n 8. potential_energy or PE\n 9. kinetic_energy or KE\n 10.')
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