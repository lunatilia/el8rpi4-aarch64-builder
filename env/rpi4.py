#
# Copyright (C) 2019 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# --
# Origin: Red Hat, Inc.
# Modified by: Mitsuki Shirase <https://github.com/lunatilia>

import os

from pyanaconda.modules.storage.bootloader.base import BootLoader, Arguments, BootLoaderError
from pyanaconda.core import util
from pyanaconda.core.configuration.anaconda import conf
from pyanaconda.product import productName

from pyanaconda.anaconda_loggers import get_module_logger
log = get_module_logger(__name__)

__all__ = ["RPI4"]


class RPI4(BootLoader):
    name = "RPI4"
    _config_file = "config.txt"
    _config_dir = "/boot"

    stage2_format_types = ["vfat"]
    stage2_device_types = ["partition"]
    stage2_bootable = True

    # Kernel Packages for Raspberry Pi 4
    packages = ["raspberrypi2-firmware", "raspberrypi2-kernel4"]

    @property
    def config_file(self):
        return "%s/%s" % (self._config_dir, self._config_file)

    @property
    def boot_prefix(self):
        """ Prefix, if any, to paths in /boot. """
        if self.stage2_device.format.mountpoint == "/":
            prefix = "/boot"
        else:
            prefix = ""

        return prefix

    def write_config_console(self, config):
        if not self.console:
            return

        console_arg = "console=%s" % self.console
        if self.console_options:
            console_arg += ",%s" % self.console_options
        self.boot_args.add(console_arg)

    def write_config_images(self, config):
        stanza = ("#dtoverlay=pi3-disable-wifi\n"
                  "#dtoverlay=pi3-disable-bt\n")
        config.write(stanza)

    #
    # installation (dummy)
    #

    def install(self, args=None):
        args = ["-f", "/boot/config.txt" ]
        rc = util.execInSysroot("test", args)

        if rc:
            raise BootLoaderError("boot loader install failed")
