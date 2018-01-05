#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ITU-R BT.470 Colourspaces
=========================

Defines the *ITU-R BT.470* colourspaces:

-   :attr:`BT470_525_COLOURSPACE`.
-   :attr:`BT470_625_COLOURSPACE`.

See Also
--------
`RGB Colourspaces Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/models/rgb.ipynb>`_

References
----------
.. [1]  International Telecommunication Union. (1998). Recommendation ITU-R
        BT.470-6 - CONVENTIONAL TELEVISION SYSTEMS. Retrieved from
        http://www.itu.int/dms_pubrec/itu-r/rec/bt/\
R-REC-BT.470-6-199811-S!!PDF-E.pdf
"""

from __future__ import division, unicode_literals

import numpy as np
from functools import partial

from colour.colorimetry import ILLUMINANTS
from colour.models.rgb import (RGB_Colourspace, function_gamma,
                               normalised_primary_matrix)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'BT470_525_PRIMARIES', 'BT470_525_WHITEPOINT', 'BT470_525_ILLUMINANT',
    'BT470_525_TO_XYZ_MATRIX', 'XYZ_TO_BT470_525_MATRIX',
    'BT470_525_COLOURSPACE', 'BT470_625_PRIMARIES', 'BT470_625_WHITEPOINT',
    'BT470_625_ILLUMINANT', 'BT470_625_TO_XYZ_MATRIX',
    'XYZ_TO_BT470_625_MATRIX', 'BT470_625_COLOURSPACE'
]

BT470_525_PRIMARIES = np.array(
    [[0.67, 0.33],
     [0.21, 0.71],
     [0.14, 0.08]])  # yapf: disable
"""
*ITU-R BT.470 - 525* colourspace primaries.

BT470_525_PRIMARIES : ndarray, (3, 2)
"""

BT470_525_ILLUMINANT = 'C'
"""
*ITU-R BT.470 - 525* colourspace whitepoint name as illuminant.

BT470_525_ILLUMINANT : unicode
"""

BT470_525_WHITEPOINT = (
    ILLUMINANTS['CIE 1931 2 Degree Standard Observer'][BT470_525_ILLUMINANT])
"""
*ITU-R BT.470 - 525* colourspace whitepoint.

BT470_525_WHITEPOINT : ndarray
"""

BT470_525_TO_XYZ_MATRIX = normalised_primary_matrix(BT470_525_PRIMARIES,
                                                    BT470_525_WHITEPOINT)
"""
*ITU-R BT.470 - 525* colourspace to *CIE XYZ* tristimulus values matrix.

BT470_525_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_BT470_525_MATRIX = np.linalg.inv(BT470_525_TO_XYZ_MATRIX)
"""
*CIE XYZ* tristimulus values to *ITU-R BT.470 - 525* colourspace matrix.

XYZ_TO_BT470_525_MATRIX : array_like, (3, 3)
"""

BT470_525_COLOURSPACE = RGB_Colourspace(
    'ITU-R BT.470 - 525',
    BT470_525_PRIMARIES,
    BT470_525_WHITEPOINT,
    BT470_525_ILLUMINANT,
    BT470_525_TO_XYZ_MATRIX,
    XYZ_TO_BT470_525_MATRIX,
    partial(function_gamma, exponent=1 / 2.8),
    partial(function_gamma, exponent=2.8))  # yapf: disable
"""
*ITU-R BT.470 - 525* colourspace.

BT470_525_COLOURSPACE : RGB_Colourspace
"""

BT470_625_PRIMARIES = np.array(
    [[0.64, 0.33],
     [0.29, 0.60],
     [0.15, 0.06]])  # yapf: disable
"""
*ITU-R BT.470 - 625* colourspace primaries.

BT470_625_PRIMARIES : ndarray, (3, 2)
"""

BT470_625_ILLUMINANT = 'D65'
"""
*ITU-R BT.470 - 625* colourspace whitepoint name as illuminant.

BT470_625_ILLUMINANT : unicode
"""

BT470_625_WHITEPOINT = (
    ILLUMINANTS['CIE 1931 2 Degree Standard Observer'][BT470_625_ILLUMINANT])
"""
*ITU-R BT.470 - 625* colourspace whitepoint.

BT470_625_WHITEPOINT : ndarray
"""

BT470_625_TO_XYZ_MATRIX = normalised_primary_matrix(BT470_625_PRIMARIES,
                                                    BT470_625_WHITEPOINT)
"""
*ITU-R BT.470 - 625* colourspace to *CIE XYZ* tristimulus values matrix.

BT470_625_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_BT470_625_MATRIX = np.linalg.inv(BT470_625_TO_XYZ_MATRIX)
"""
*CIE XYZ* tristimulus values to *ITU-R BT.470 - 625* colourspace matrix.

XYZ_TO_BT470_625_MATRIX : array_like, (3, 3)
"""

BT470_625_COLOURSPACE = RGB_Colourspace(
    'ITU-R BT.470 - 625',
    BT470_625_PRIMARIES,
    BT470_625_WHITEPOINT,
    BT470_625_ILLUMINANT,
    BT470_625_TO_XYZ_MATRIX,
    XYZ_TO_BT470_625_MATRIX,
    partial(function_gamma, exponent=1 / 2.8),
    partial(function_gamma, exponent=2.8))  # yapf: disable
"""
*ITU-R BT.470 - 625* colourspace.

BT470_625_COLOURSPACE : RGB_Colourspace
"""
