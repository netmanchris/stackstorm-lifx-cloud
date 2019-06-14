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


class lightslookup(LifxCloudBaseAction):
    def run(self):
        lights = self.client.list_lights()
        if isinstance(lights, list):
            lights_data = []
            for light in lights:
                out ={
                    'id': light['id'],
                    'uuid': light['uuid'],
                    'label':light['label'],
                    'power':light['power'],
                    'color':light['color'],
                    'brightness': light['brightness']
                      }
                lights_data.append(out)

            return (True, lights_data)
        return (False, lights)
