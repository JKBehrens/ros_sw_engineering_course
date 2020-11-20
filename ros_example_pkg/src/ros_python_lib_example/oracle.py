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

import random
from collections import deque

class Oracle(object):
    """
    An example python library within a ROS package.

    The oracle class is a small wrapper for a random number generator.
    """

    def __init__(self, seed=42):
        self.initial_seed = seed
        self.seeds = {seed}
        self.rand = random.Random()
        self.rand.seed(seed)

        self.last_predictions = deque(maxlen=30)

        self.predictor = self.getSampleEven

    def feed(self, seed):
        """
        Provide new inspiration for the oracle.
        :param seed: integer number used to seed the random number generator
        :return:
        """
        if not isinstance(seed, int):
            raise TypeError("The oracle eats only integers.")
        if seed in self.seeds:
            raise ValueError("The oracle doesn't accept old seeds.")
        self.rand.seed(seed)
        self.seeds.add(seed)
        return

    def setPredictor(self, model='even'):
        """
        Setting the model the oracle uses.
        :param model: string specifying the model. Can be 'even' or 'gauss'
        :return:
        """
        if model == 'even':
            self.predictor = self.getSampleEven
        if model == 'gauss':
            self.predictor = self.getSampleGauss

    def getPrediction(self, arg1, arg2):
        self.last_predictions.append(self.predictor(arg1, arg2))
        return self.last_predictions[-1]

    def getSampleGauss(self, mu, sigma):
        return self.rand.gauss(mu, sigma)

    def getSampleEven(self, min, max):
        """
        Returns a random value between min and max. If min > max, the values will be swapped.
        :param min: lower border of selection interval
        :param max: upper border of selection interval
        :return: float sampled from an even distribution between min and max.
        """
        if not max > min:
            min, max = max, min
        delta = max - min
        return self.rand.random() * delta + min

    def reset(self):
        """Resets the Oracle to the state of the creation."""
        self.seeds = {self.initial_seed}
        self.rand.seed(self.initial_seed)
