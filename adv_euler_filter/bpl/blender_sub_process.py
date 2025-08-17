# SPDX-FileCopyrightText: 2024-2025 Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  Adv Euler Filter
#  https://github.com/xavier150/Adv_Euler_Filter
# ----------------------------------------------

# ----------------------------------------------
#  BBAM -> BleuRaven Blender Addon Manager
#  https://github.com/xavier150/BBAM
#  BleuRaven.fr
#  XavierLoux.com
# ----------------------------------------------

import importlib

from . import bbam_addon_config_type
from . import bbam_addon_config_utils

# Reloading modules if they're already loaded
if "bbam_addon_config_type" in locals():
    importlib.reload(bbam_addon_config_type)
if "bbam_addon_config_utils" in locals():
    importlib.reload(bbam_addon_config_utils)

