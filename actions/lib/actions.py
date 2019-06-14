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

from pifx import PIFX
from st2common.runners.base_action import Action

class LifxCloudBaseAction(Action):
    def __init__(self,config):
        super(LifxCloudBaseAction, self).__init__(config)
        self.client = self._get_client()

    def _get_client(self):
        token = self.config['apitoken']
        client = PIFX(api_key=token)
        return client
