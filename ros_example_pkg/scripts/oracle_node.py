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

import sys
import rospy
import argparse
from ros_python_lib_example.oracle import Oracle

def parse_args():
  format_class = argparse.RawDescriptionHelpFormatter
  parser = argparse.ArgumentParser(formatter_class=format_class,
                  description='ROS node making the oracle available via ROS')
  parser.add_argument('--seed', action="store",
              help='Specify the integer seed for the Oracle!')

  args = parser.parse_args(rospy.myargv()[1:])
  return args


class OracleNode(object):
    def __init__(self, seed):
        rospy.init_node('OracleNode')

        self.oracle = Oracle(seed=seed)

        rospy.on_shutdown(self.shutdown_hook)

        rate = rospy.Rate(1.0)
        while not rospy.is_shutdown():
            rospy.loginfo(self.oracle.getPrediction(0, 10))
            rate.sleep()

        print('exiting')

    def shutdown_hook(self):
        rospy.loginfo("Shutting down. The oracle thanks for feeding the seeds: {}".format(self.oracle.seeds))




if __name__ == "__main__":
    args = parse_args()
    print(args)
    o = OracleNode(int(args.seed))