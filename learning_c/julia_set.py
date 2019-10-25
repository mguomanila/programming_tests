'''
Julia set generator without optional PIL-based image drawing
'''
import time
from functools import wraps


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print('@timefn: %s took %.6fsecs' % (fn.__name__, (t2-t1)) )
        return result
    return measure_time


def calc_pure_python(desired_width, max_iterations):
    ''' Create a list of complex coordinates(zs) and complex
        parameters (cs), build Julia set, and display
    '''
    x_step = (x2-x1) / desired_width
    y_step = (y1-y2) / desired_width
    x, y = [], []
    ycoord = y2
    while ycoord > y1:
        y += [ycoord]
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x += [xcoord]
        xcoord += x_step
    # Build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed;
    # we use it to simulate a real-world scenario with several inputs to
    # our function.
    zs,cs = [], []
    for ycoord in y:
        for xcoord in x:
            zs += [complex(xcoord,ycoord)]
            cs += [complex(c_real,c_imag)]
    print("length of x: %d" % len(x))
    print("Total elements: %d" % len(zs))
    #start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations,zs,cs)
    #end_time = time.time()
    #secs = end_time - start_time
    #print(calculate_z_serial_purepython.__name__ + " took %0.6fsecs" % secs)
    
    # This sum is expected for a 1000^2 grid with 300 iterations.
    # It catches minor errors we might introduce when we're
    # working on a fixed set of inputs.
    #assert sum(output) == 33219980
    assert sum(output) == 8964780
    #print (sum(output))
    

@timefn
def calculate_z_serial_purepython(maxiter,zs,cs):
    ''' Calculate output list using julia update rule'''
    output = [0] * len(zs)
    for i in range(len(zs)):
        n,z,c = 0,zs[i],cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

    
if __name__ == '__main__':
    ''' Calculate the Julia set using a pure python solution with
        reasonable defaults for a laptop'''
    # area of complex space to investigate
    x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
    c_real, c_imag = -0.62772, -.42193
    calc_pure_python(desired_width=10**3,max_iterations=30*2)
    
