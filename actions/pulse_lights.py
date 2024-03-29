# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netmanchris"
# __license__ = "Apache2.0"

from lib.actions import LifxCloudBaseAction


class PulseLights(LifxCloudBaseAction):
    def run(self, label=None, color=None, from_color=None, cycles=None,power_on=True):
        #send toggle command to LIFX cloud for specific light bulb

        if label:
            label = 'label:{}'.format(label)
        else:
            label = 'all'
        print (label)
        result = self.client.pulse_lights(selector=label, power_on=power_on,
                                          color=color,
                                       cycles=cycles, from_color=from_color)
        if result[0]['status'] == 'ok':
            return (True, result)
        return (False, lights)
