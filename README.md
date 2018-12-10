Overview
========

astr8300_rappture_rotation_curve is one of the packages for Astr8300 rappture projects

Installation
------------

You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.  Type the following:

* git clone https://github.com/xiuruiz/astr8300_rappture_rotation_curves.git
* cd astr8300_rappture_rotation_curves
* there are two folder: 1. 1D model 2. 3D model
* e.g., cd final_project_3D
* rappture


Authors
-------

- Xiurui Zhao <xiuruiz@g.clemson.edu> and Bradley S. Meyer <mbradle@clemson.edu>


# Rotation Curve
In this project, you could find 1D model and 3D model for building rotation curve. 

In 1D model, you can input the inner radius rmin (defult = 0.1), the outer radius rmax (defult = 10), initial mass M0 (defult = 0), and the number of points you would like to draw in the figure, npt (defult = 100). You will also need to give a density distribution &#x3C1; (r) (defult = r**-2.5). Successfully inputting the above parameters and functions, you could obtain the density &#x3C1; at different radius, inner mass (M) at different radius velocity in different radius and the velocity (r) at different radius.

In 3D model, you will have the same input parameters (rmin, rmax, M0 and npts). However, in 3D model you can input the polar angle (theta), such that the density distribution will be &#x3C1; (r,theta) (defult = r**-2.5 * sin(theta); here we assume a &#x3C6; symmetrical distribution). Successfully inputting the above parameters and functions, you could obtain the density &#x3C1; at different radius and different polar angle, inner mass (M) at different radius velocity in different radius and the velocity (v) at different radius.

# Math

![equations](https://github.com/xiuruiz/astr8300_rappture_rotation_curves/blob/master/equations.png)

# Outlook
The 3D model is a spherical model, while we could add a cylinderical model with variables of radius (r) and height (z).
