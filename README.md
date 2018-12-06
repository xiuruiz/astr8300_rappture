Overview
========

astr8300_rappture is a sample package for Astr8300 rappture projects

Installation
------------

You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.  Type the following:

* git clone http://github.com/mbradle/astr8300_rappture.git
* cd astr8300_rappture
* rappture

Math
----

Here are some symbols:  &alpha;, &beta;, &gamma;, and &delta;.  And here is a reaction:  <sup>12</sup>C + <sup>4</sup>He &rarr; <sup>16</sup>O + &gamma;.  And here is an equation:  <b>F</b> = m<b>a</b>.

Authors
-------

- Bradley S. Meyer <mbradle@clemson.edu>



# Rotation Curve
In this project, you could input the initial rmin (defult = 0), the outer radius rmax (defult = 10) and initial mass M0 (defult = 0), and the number of points you would like to calculate npt (defult = 100). You will also need to give a density &#xx3C1; (defult = 1) in 0.063 g/cm<sup>-3</sup>. You could also obtain the velocity in different radius. The radius is in solar radius (r = 6.96x10<sup>10</sup>cm) and the mass is in solar mass (m = 1.99x10<sup>33</sup>g), the velocity is in 437 km/s. 

# Torus of AGNs (This part is contributed by Xiurui Zhao)

The line-of-sight column density may differ from the global average column density of the torus, so in some models (e.g., <b>MYTorus</b>), the line-of-sight column density, N<sub>H,l.o.s.</sub>=N<sub>H</sub>[1-(c/a)<sup>2</sup>cos<sup>2</sup>&theta;<sub>obs</sub>]<sup>1/2</sup>, where N<sub>H</sub> is the equatorial column density of the torus, when &theta;<sub>obs</sub>=90&deg; and cos<sup>2</sup>&theta;<sub>obs</sub>=0; &theta;<sub>obs</sub> is the observing angle; <i>a</i> is the redius of the torus and <i>c</i> is the distance between the black hole and the center point of the torus. 
