//
// File: controlador.h
//
// MATLAB Coder version            : 4.0
// C/C++ source code generated on  : 26-Aug-2020 16:37:14
//
#ifndef CONTROLADOR_H
#define CONTROLADOR_H

// Include Files
#include <stddef.h>
#include <stdlib.h>
#include "rtwtypes.h"
#include "controlador_types.h"

// Function Declarations
extern void controlador(const double x[3], double q1, double q2, double ai1_k1,
  double ai2_k1, double u[2], double *ai1, double *ai2);

#endif

//
// File trailer for controlador.h
//
// [EOF]
//
