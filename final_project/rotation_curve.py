# ----------------------------------------------------------------------
#  GRAPH
#
#  This simple example shows how you can use the Rappture toolkit
#  to handle I/O for a simple simulator--in this case, one that
#  evaluates an x/y graph
#
# ======================================================================
#  AUTHOR:  Michael McLennan, Purdue University
#  Copyright (c) 2004-2012  HUBzero Foundation, LLC
#
#  See the file "license.terms" for information on usage and
#  redistribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
# ======================================================================

import Rappture
import sys
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize

def f(r, formula):
    return eval(formula)

def calc(M, r, formula):
    return eval(formula) * r**2

def main():
    io = Rappture.library(sys.argv[1])

    rmin = float(io.get('input.number(min).current'))
    rmax = float(io.get('input.number(max).current'))
    M0 = float(io.get('input.number(M0).current'))
    npts = int(io.get('input.number(Npts).current'))
    formula = io.get('input.string(formula).current')
    #formula1 = '(' + io.get('input.string(formula).current')+')*r**2.'

    r = np.linspace(rmin, rmax, npts)
    sol = odeint(calc, M0, r, args=(formula,))
    v = np.linspace(0,npts,npts)
    io.put('output.curve(result2).about.label','Mass vs r',append=0)
    io.put('output.curve(result2).yaxis.label','Mass')
    io.put('output.curve(result2).xaxis.label','r')

    io.put('output.curve(result1).about.label','Density vs r',append=0)
    io.put('output.curve(result1).yaxis.label','Density')
    io.put('output.curve(result1).xaxis.label','r')

    for i in range(npts):
        io.put(
               'output.curve(result2).component.xy',
               '%g %g\n' % (r[i],sol[i][0]), append=1
              )
        v[i] = (sol[i][0]/r[i])**0.5
        io.put(
               'output.curve(result3).component.xy',
               '%g %g\n' % (r[i],v[i]), append=1
              )
        io.put(
               'output.curve(result1).component.xy',
               '%g %g\n' % (r[i],f(r[i], formula)), append=1)
    io.put('output.curve(result3).about.label','Velocity vs r',append=0)
    io.put('output.curve(result3).yaxis.label','velocity')
    io.put('output.curve(result3).xaxis.label','r')

    Rappture.result(io)

if __name__ == "__main__":
    main()


