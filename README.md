# planeKF
Simple example of the Kalman Filter in MATLAB and Python

MATLAB and Python realization of the KF example explained by Michel van Biezen in his lecture series on the Kalman filter. See [here](https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT) for the full lecture series. The example starts at [Lecture 27](https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT).

- There are no prerequisites to run the MATLAB example.
- You must have numpy and matplotlib packages to run the Python example.
- Possibly the Python example can be coded prettier, but I'm no a Python pro (yet;).

**WARNING:** Do not implement the `Pp=diag(diag(Pp))' (similar in Python) line outside this educational example. This is only to make the inversion and thus hand calculation demonstrated easier. A real application of the KF would not discard the off diagonal terms.
