//
// File: controlador.cpp
//
// MATLAB Coder version            : 4.0
// C/C++ source code generated on  : 26-Aug-2020 16:37:14
//

// Include Files
#include "rt_nonfinite.h"
#include "controlador.h"

// Function Definitions

//
// Arguments    : const double x[3]
//                double q1
//                double q2
//                double ai1_k1
//                double ai2_k1
//                double u[2]
//                double *ai1
//                double *ai2
// Return Type  : void
//
void controlador(const double x[3], double q1, double q2, double ai1_k1, double
                 ai2_k1, double u[2], double *ai1, double *ai2)
{
  double u2;
  int i0;
  double u1;
  static const double a[3] = { 0.0216, 0.003, -0.005 };

  static const double b_a[3] = { 0.0029, 0.019, -0.004 };

  // calculo el error
  // calculo la accion de control u1 y u2
  *ai1 = (q1 - x[0]) + ai1_k1;
  *ai2 = (q2 - x[1]) + ai2_k1;

  // accion integral
  // accion integral
  // K1(1,1)*x1(i)+K1(1,2)*x2(i)+K1(1,3)*x3(i);
  // K1(2,1)*x1(i)+K1(2,2)*x2(i)+K1(2,3)*x3(i);
  // accion propocional
  // accion propocional
  u2 = 0.0;
  for (i0 = 0; i0 < 3; i0++) {
    u2 += a[i0] * x[i0];
  }

  u1 = -(-0.00095 * *ai1 + -0.00032 * *ai2) + -u2;

  // accion de control
  u2 = 0.0;
  for (i0 = 0; i0 < 3; i0++) {
    u2 += b_a[i0] * x[i0];
  }

  u2 = -(-0.0003 * *ai1 + -0.00091 * *ai2) + -u2;

  // accion de control
  // Saturacion para evitar daños en los acutadores
  if (u1 > 0.0015) {
    u1 = 0.0015;
  }

  if (u2 > 0.0015) {
    u2 = 0.0015;
  }

  if (u1 < 0.0) {
    u1 = 0.0;
  }

  if (u2 < 0.0) {
    u2 = 0.0;
  }

  u[0] = u1;
  u[1] = u2;
}

//
// File trailer for controlador.cpp
//
// [EOF]
//
