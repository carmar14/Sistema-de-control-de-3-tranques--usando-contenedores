/*
 * File: _coder_controlador_api.h
 *
 * MATLAB Coder version            : 4.0
 * C/C++ source code generated on  : 26-Aug-2020 16:37:14
 */

#ifndef _CODER_CONTROLADOR_API_H
#define _CODER_CONTROLADOR_API_H

/* Include Files */
#include "tmwtypes.h"
#include "mex.h"
#include "emlrt.h"
#include <stddef.h>
#include <stdlib.h>
#include "_coder_controlador_api.h"

/* Variable Declarations */
extern emlrtCTX emlrtRootTLSGlobal;
extern emlrtContext emlrtContextGlobal;

/* Function Declarations */
extern void controlador(real_T x[3], real_T q1, real_T q2, real_T ai1_k1, real_T
  ai2_k1, real_T u[2], real_T *ai1, real_T *ai2);
extern void controlador_api(const mxArray * const prhs[5], int32_T nlhs, const
  mxArray *plhs[3]);
extern void controlador_atexit(void);
extern void controlador_initialize(void);
extern void controlador_terminate(void);
extern void controlador_xil_terminate(void);

#endif

/*
 * File trailer for _coder_controlador_api.h
 *
 * [EOF]
 */
