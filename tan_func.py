'''math module includes all the mathematical functions'''
import math


def tan_fun(inp1):
    '''check for the tangent value of a number'''
    tan_f = math.tan(int(inp1))
    r_tan_f = round(tan_f, 9)
    print r_tan_f
    return r_tan_f



# sample = raw_input()
#  tan_fun(sample)
