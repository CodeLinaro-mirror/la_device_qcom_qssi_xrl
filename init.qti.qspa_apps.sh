#! /system/bin/sh
#
# Copyright (c) 2022,2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear
#

soc_id=`cat /sys/devices/soc0/soc_id` 2> /dev/null

if [ "$soc_id" -eq 554 ]; then
    setprop ro.vendor.config.qspa.apps true
elif [ "$soc_id" -eq 579 ]; then
    setprop ro.vendor.config.qspa.apps false
fi
