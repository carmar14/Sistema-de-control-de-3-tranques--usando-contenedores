//
// File: proceso.cpp
//
// MATLAB Coder version            : 4.0
// C/C++ source code generated on  : 26-Aug-2020 16:50:32
//

// Include Files
#include "rt_nonfinite.h"
#include "proceso.h"

// Function Definitions

//
// Matrices A y B del sistema discreto
// Arguments    : const double u[2]
//                const double x[3]
//                double xk1[3]
// Return Type  : void
//
void proceso(const double u[2], const double x[3], double xk1[3])
{
  double d0;
  int i0;
  double d1;
  static const double a[3] = { 0.9888, 0.0001, 0.0112 };

  double d2;
  static const double b_a[2] = { 64.5687, 0.0014 };

  double d3;
  static const double c_a[3] = { 0.0001, 0.9781, 0.0111 };

  double d4;
  double d5;
  static const double d_a[3] = { 0.0112, 0.0111, 0.9776 };

  double dv0[3];

  // calculo los estados
  // A11*x1(i)+A12*x2(i)+A13*x3(i)+B11*u1+B12*u2;
  // A21*x1(i)+A22*x2(i)+A23*x3(i)+B21*u1+B22*u2;
  // A31*x1(i)+A32*x2(i)+A33*x3(i)+B31*u1+B32*u2;
  d0 = 0.0;
  for (i0 = 0; i0 < 3; i0++) {
    d0 += a[i0] * x[i0];
  }

  d1 = 0.0;
  for (i0 = 0; i0 < 2; i0++) {
    d1 += b_a[i0] * u[i0];
  }

  d2 = 0.0;
  for (i0 = 0; i0 < 3; i0++) {
    d2 += c_a[i0] * x[i0];
  }

  d3 = 0.0;
  for (i0 = 0; i0 < 2; i0++) {
    d3 += (0.0014 + 64.2188 * (double)i0) * u[i0];
  }

  d4 = 0.0;
  for (i0 = 0; i0 < 3; i0++) {
    d4 += d_a[i0] * x[i0];
  }

  d5 = 0.0;
  for (i0 = 0; i0 < 2; i0++) {
    d5 += (0.365 + -0.0012999999999999678 * (double)i0) * u[i0];
  }

  dv0[0] = d0 + d1;
  dv0[1] = d2 + d3;
  dv0[2] = d4 + d5;
  for (i0 = 0; i0 < 3; i0++) {
    xk1[i0] = dv0[i0];
  }
}

//
// File trailer for proceso.cpp
//
// [EOF]
//
