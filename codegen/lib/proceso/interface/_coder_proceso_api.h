/*
 * File: _coder_proceso_api.h
 *
 * MATLAB Coder version            : 4.0
 * C/C++ source code generated on  : 26-Aug-2020 16:50:32
 */

#ifndef _CODER_PROCESO_API_H
#define _CODER_PROCESO_API_H

/* Include Files */
#include "tmwtypes.h"
#include "mex.h"
#include "emlrt.h"
#include <stddef.h>
#include <stdlib.h>
#include "_coder_proceso_api.h"

/* Variable Declarations */
extern emlrtCTX emlrtRootTLSGlobal;
extern emlrtContext emlrtContextGlobal;

/* Function Declarations */
extern void proceso(real_T u[2], real_T x[3], real_T xk1[3]);
extern void proceso_api(const mxArray * const prhs[2], int32_T nlhs, const
  mxArray *plhs[1]);
extern void proceso_atexit(void);
extern void proceso_initialize(void);
extern void proceso_terminate(void);
extern void proceso_xil_terminate(void);

#endif

/*
 * File trailer for _coder_proceso_api.h
 *
 * [EOF]
 */
