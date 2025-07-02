#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.file import File
from extract_utils.fixups_blob import (
    BlobFixupCtx,
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/meizu/m2481',
    'hardware/qcom-caf/sm8650',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    #(
    #    'vendor/etc/media_codecs_pineapple.xml', 
    #    'vendor/etc/media_codecs_pineapple_vendor.xml'
    #): blob_fixup()
    #    .regex_replace('.*media_codecs_(google_audio|google_c2|google_telephony|google_video|vendor_audio).*\n', ''),
    (
        'vendor/bin/hw/android.hardware.security.keymint-service-spu-qti',
        'vendor/lib64/libspukeymint.so'
    ): blob_fixup()
        .replace_needed('android.hardware.security.sharedsecret-V2-ndk.so', 'android.hardware.security.sharedsecret-V1-ndk.so'),
    'vendor/lib64/libspukeymintprovision.so': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V2-ndk.so', 'android.hardware.security.keymint-V3-ndk.so'),
    'vendor/lib64/android.hardware.gatekeeper-V1-ndk.so': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V3-ndk.so', 'android.hardware.security.keymint-V4-ndk.so'),
    'vendor/bin/hw/android.hardware.health-service.qti': blob_fixup()
        .replace_needed('android.hardware.health-V2-ndk.so', 'android.hardware.health-V4-ndk.so'),    
    (
        'vendor/lib64/android.hardware.graphics.composer3-V2-ndk.so',
        'vendor/lib64/android.hardware.camera.device-V1-ndk.so',
        'vendor/lib64/android.hardware.camera.device-V2-ndk.so'
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V6-ndk.so'),

    (
        'vendor/lib64/vendor.qti.hardware.display.composer3-V1-ndk.so',
        'vendor/bin/hw/vendor.qti.hardware.display.composer-service'
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.composer3-V2-ndk.so', 'android.hardware.graphics.composer3-V3-ndk.so'),

    'vendor/lib64/android.hardware.bluetooth.audio-V3-ndk.so': blob_fixup()
        .replace_needed('android.hardware.audio.common-V1-ndk.so', 'android.hardware.audio.common-V2-ndk.so'),
    
    (
        'vendor/lib64/hw/android.hardware.bluetooth.audio-impl-qti.so',
        'vendor/lib64/libbluetooth_audio_session_aidl.so'
        
    ): blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V3-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so'),

    (
        'vendor/lib64/android.frameworks.sensorservice-V1-ndk.so',
        'vendor/bin/hw/android.hardware.sensors-service.multihal',
        'vendor/lib64/libsensorndkbridge.so'
    ): blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so'),

    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),
    'vendor/bin/aecxsimulator': blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),

    'vendor/lib64/camera.device-external-impl.so': blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so')
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V6-ndk.so'),

    'vendor/lib64/hw/audio.bluetooth.default.so': blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V3-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so')
        .replace_needed('android.hardware.audio.common-V2-ndk.so', 'android.hardware.audio.common-V4-ndk.so'),

    
}  # fmt: skip

module = ExtractUtilsModule(
    'm2481',
    'meizu',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
