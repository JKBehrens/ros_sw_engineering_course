#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2020, Jan Behrens
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function

PKG = 'ros_example_pkg'
NAME = 'oracle_test'

import sys
import unittest

# import rospy
import rostest
# import rosunit
import numpy as np
from ros_python_lib_example.oracle import Oracle


class TestOracle(unittest.TestCase):

    def testOracleGoodInput(self):
        o = Oracle(seed=42)
        prediction = o.getPrediction(arg1=3, arg2=7)
        self.assertGreaterEqual(prediction, 3, "Prediction is out of range.")
        self.assertLessEqual(prediction, 7, "Prediction is out of range.")

    def testOracleMixedInput(self):
        o = Oracle(seed=42)
        prediction = o.getPrediction(arg1=3.05, arg2=7)
        self.assertGreaterEqual(prediction, 3.05, "Prediction is out of range.")
        self.assertLessEqual(prediction, 7, "Prediction is out of range.")

        prediction = o.getPrediction(arg1=10.05, arg2=7)
        self.assertGreaterEqual(prediction, min(10.05, 7), "Prediction is out of range.")
        self.assertLessEqual(prediction, max(10.05, 7), "Prediction is out of range.")

    def testOracleSeeding(self):
        o = Oracle(seed=42)
        o2 = Oracle(seed=42)
        prediction = [o.getPrediction(arg1=3.05, arg2=7) for _ in range(100)]
        prediction2 = [o2.getPrediction(arg1=3.05, arg2=7)  for _ in range(100)]

        self.assertTrue(np.allclose(np.array(prediction), np.array(prediction2)), "Both prediction series should be eual")

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestOracle, sys.argv)
    # rosunit.unitrun(PKG, 'test_oracle', TestOracle)
