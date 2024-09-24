# Copyright (c) 2023 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

FAILED_FILEPATHS_WHITELIST = {
    # NOTE: these files are from QSSI builds
    "vendor/qcom/opensource/audio-hal/primary-hal/configs/qssi/qssi.mk",
    "vendor/qcom/proprietary/android-perf/profiles.mk",
    "vendor/qcom/proprietary/chi-cdk/product.mk",
    "vendor/qcom/proprietary/commonsys/qrdplus/sva/products.mk",
    "vendor/qcom/proprietary/commonsys/voiceui/products.mk",
    "vendor/qcom/proprietary/mm-audio-internal/dolby/dax/device/dax2_common_hw.mk",
    "vendor/qcom/proprietary/prebuilt_ASAN/target/product/pineapple/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_ASAN/target/product/qssi_xrl/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_grease/target/common/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_grease/target/product/pineapple/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_grease/target/product/qssi_xr/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_HY11/target/common/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_HY11/target/product/pineapple/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_HY11/target/product/qssi_xrl/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_HY22/target/common/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_HY22/target/product/pineapple/prebuilt.mk",
    "vendor/qcom/proprietary/prebuilt_HY22/target/product/qssi_xrl/prebuilt.mk",
    "vendor/qcom/proprietary/qrdplus/China/ChinaMobile/products.mk",
    "vendor/qcom/proprietary/qrdplus/China/ChinaTelecom/products.mk",
    "vendor/qcom/proprietary/qrdplus/China/ChinaUnicom/products.mk",
    "vendor/qcom/proprietary/qrdplus/China/CTA/products.mk",
    "vendor/qcom/proprietary/qrdplus/Extension/products.mk",
    "vendor/qcom/proprietary/qrdplus/InternalUseOnly/DuerosSDK/products.mk",
    "vendor/qcom/proprietary/resource-overlay/overlay.mk",
}

SHELL_WHITELIST = {
    "device/qcom/sepolicy/SEPolicy.mk",
    "vendor/qcom/defs/product-defs/system/wigig-product.mk",
    "vendor/qcom/proprietary/common/create_files.mk",
    "vendor/qcom/proprietary/commonsys/openclwrapper/Android.mk",
}

TARGET_OUT_HEADERS_WHITELIST = {
    "vendor/qcom/proprietary/commonsys/fastmmi/module/sensor/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/telephone/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/aostlm/daemon/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/aostlm/src/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/aostlm/test/Android.mk",
}

RM_WHITELIST = {
    "vendor/qcom/proprietary/common/scripts/Android.mk",
}

LOCAL_COPY_HEADERS_WHITELIST = {}

KERNEL_OBJ_WHITELIST = {
    "vendor/qcom/proprietary/commonsys/fastmmi/module/sysinfo/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/telephone/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/touch/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/vibrator/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/wifi/Android.mk",
    "vendor/qcom/proprietary/commonsys/ims-ship/vtext/Android.mk",
    "vendor/qcom/proprietary/commonsys/qvr/services/sxr/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-internal/assurancetest/scmtest/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-internal/havenlicense/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-internal/mdtp/test_app/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-internal/mdtp/ut/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-internal/sp_iris_test/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-internal/sse/SecureIndicator/tests/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/LicenseManager/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/QSSP_RTIC/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/aostlm/daemon/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/aostlm/src/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/aostlm/test/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/assurancetest/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/assurancetest/cpzassurancetest/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/bcstsrv/src/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/bcstsrv/test/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/haventoken/common/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/haventoken/havent/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/haventoken/havent_client/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/haventoken/havent_test/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/secota/SecotaNService/common/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/secota/SecotaNService/daemon/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/secota/SecotaNService/intf/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/secota/SecotaNService/src/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/sp_iris_lib/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm-noship/splogger/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm/QHCK/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm/securitytest/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm/soterclient/Android.mk",
    "vendor/qcom/proprietary/commonsys/securemsm/spdaemon/src/Android.mk",
    "vendor/qcom/proprietary/commonsys/vppss/vppsession/Android.mk",
    "vendor/qcom/opensource/commonsys/dataservices/sockev/src/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/LicenseManager/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/QSSP_RTIC/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/aostlm/daemon/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/aostlm/src/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/aostlm/test/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/assurancetest/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/assurancetest/cpzassurancetest/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/bcstsrv/src/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/bcstsrv/test/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/haventoken/common/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/haventoken/havent/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/haventoken/havent_client/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/haventoken/havent_test/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/secota/SecotaNService/common/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/secota/SecotaNService/daemon/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/secota/SecotaNService/intf/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/secota/SecotaNService/src/Android.mk",
    "vendor/qcom/proprietary/commonsys-intf/securemsm/sp_iris_lib/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/audio/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/battery/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/bluetooth/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/camera/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/cpu/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/example/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/flashlight/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/fm/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/gps/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/headset/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/key/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/lcd/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/light/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/memory/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/nfc/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/power/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/sensor/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/sim/Android.mk",
    "vendor/qcom/proprietary/commonsys/fastmmi/module/storage/Android.mk",
}

DATETIME_WHITELIST = {}

TARGET_PRODUCT_WHITELIST = {
    "vendor/qcom/opensource/core-utils/build/AndroidBoardCommon.mk",
    "vendor/qcom/opensource/core-utils/build/build.sh",
    "vendor/qcom/opensource/core-utils/build/build_image_standalone.py",
}

RECURSIVE_WHITELIST = {}

KERNEL_WHITELIST = {}

FOREACH_WHITELIST = {
    "vendor/qcom/opensource/core-utils/build/utils.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-qssi.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-SDM845-pureAOSP.mk",
    "vendor/qcom/proprietary/common-noship/build/generate_extra_images_prop.mk",
}

MACRO_WHITELIST = {
    "device/qcom/sepolicy/SEPolicy.mk",
    "vendor/qcom/opensource/commonsys/display/config/display-product-commonsys.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-qssi.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-SDM845-pureAOSP.mk",
    "vendor/qcom/proprietary/common-noship/etc/device-vendor-noship.mk",
    "vendor/qcom/proprietary/common-noship/etc/device-vendor-noship-SDM845-pureAOSP.mk",
    "vendor/qcom/proprietary/common-noship/etc/device-vendor-qssi-noship.mk",
    "vendor/qcom/proprietary/commonsys/android-perf-noship/config/perf-product-system-proprietary.mk",
    "vendor/qcom/proprietary/commonsys/telephony-build/build/telephony_system_product.mk",
    "vendor/qcom/proprietary/commonsys-intf/data/dpm_system_product_noship.mk",
}

OVERRIDE_WHITELIST = {
    "device/qcom/qssi_xrl/qssi_xrl.mk",
    "device/qcom/qssi_xrl/qssi_xrl_whitelist.mk",
}

SOONG_WHITELIST = {
    "device/qcom/qssi_xrl/base.mk",
    "vendor/qcom/opensource/commonsys/display/config/display-product-commonsys.mk",
    "vendor/qcom/proprietary/commonsys-intf/bluetooth/bt-system-proprietary-product.mk",
    "vendor/qcom/opensource/commonsys-intf/display/config/display-product-system.mk",
}
