# ----------------------------------------------------------------------------
# GS Widget Kit Copyright 2021 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import wx


class Label(wx.StaticText):
    def __init__(self, parent, id=wx.ID_ANY, label="", color="#fff",
                 bg_color=None, font_bold=False, style=0):
        wx.StaticText.__init__(self, parent, id=id, label=label, style=style)

        if bg_color is None:
            self.SetBackgroundColour(parent.GetBackgroundColour())
        else:
            self.SetBackgroundColour(bg_color)
        if font_bold is True:
            self.SetFont(self.GetFont().Bold())
        self.SetForegroundColour(color)
