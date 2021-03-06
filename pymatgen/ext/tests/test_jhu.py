# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

from __future__ import division, unicode_literals
import unittest
import os

from pymatgen.util.testing import PymatgenTest
from pymatgen.ext.jhu import get_kpoints
from pymatgen.io.vasp.inputs import Incar

__author__ = "Joseph Montoya"
__copyright__ = "Copyright 2017, The Materials Project"
__maintainer__ = "Joseph Montoya"
__email__ = "montoyjh@lbl.gov"
__date__ = "June 22, 2017"

test_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                        'test_files')


class JhuTest(PymatgenTest):
    def test_get_kpoints(self):
        si = PymatgenTest.get_structure("Si")
        file_name = os.path.join(test_dir, 'INCAR')
        incar = Incar.from_file(file_name)
        kpoints = get_kpoints(si, incar=incar)

if __name__ == '__main__':
    unittest.main()
