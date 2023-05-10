This folder contains experimental data and Python codes to evaluate damping models for nonlinear pendulums.

Please refer to the paper: Experimental evaluation of damping models for a nonlinear pendulum system (DOI: ---) for complete understanding of the codes.

All files must be placed in the same folder. The function of each file is as follows.
-------
File exp_data.dat contains experimental data. The data were listed in Table 2 of the paper.
    Line 1: contains 16 peak angles that were measured in Trial 1.
    Line 2: contains 16 peak angles that were measured in Trial 2.
    Line 3: contains 16 peak angles that were measured in Trial 3.
-------
File Main_numerical_analysis_for_linear_damping.py solves Equation (18) in the paper.
-------
File Main_numerical_analysis_for_square_damping.py solves Equation (22) in the paper.
-------
File Main_numerical_analysis_for_quad_damping.py solves Equation (23) in the paper.
-------
File Main_fitting.py is for finding the damping coefficients those best fit the experimental data. This file was used throughout Section 5 of the paper.
-------
File FreeVibrationModule.py contains functions for the other files. It cannot be executed alone.