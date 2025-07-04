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
    (
        'vendor.qti.diaghal@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.imsrtpservice@3.1',
        'vendor.qti.ImsRtpService-V1-ndk'
    ): lib_fixup_vendor_suffix,
    (
        'android.hardware.graphics.composer3-V2-ndk',
        'audio.primary.pineapple',
        'libar-acdb',
        'libar-gsl',
        'libagmclient',
        'liblx-osal',
        'libagmmixer',
        'libats',
        'libpalclient',
        'libwpa_client',
        'vendor.qti.hardware.AGMIPC@1.0-impl',
        'libar-pal',
        'libagm',
        'vendor.qti.hardware.pal@1.0-impl',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    (
        'product/etc/permissions/vendor.qti.hardware.data.connection-V1.0-java.xml',
        'product/etc/permissions/vendor.qti.hardware.data.connection-V1.1-java.xml',
        'product/etc/permissions/vendor.qti.hardware.data.connectionaidl-V1-java.xml'
    ): blob_fixup()
        .regex_replace('version="2.0"', 'version="1.0"'),
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
    'vendor/lib64/vendor.qti.hardware.display.composer3-V1-ndk.so': blob_fixup()
        .replace_needed('android.hardware.graphics.composer3-V2-ndk.so', 'android.hardware.graphics.composer3-V3-ndk.so'),
    'vendor/bin/hw/vendor.qti.hardware.display.composer-service': blob_fixup()
        .replace_needed('android.hardware.graphics.composer3-V2-ndk.so', 'android.hardware.graphics.composer3-V3-ndk.so')
        .replace_needed('vendor.qti.hardware.display.config-V8-ndk.so', 'vendor.qti.hardware.display.config-V11-ndk.so'),
    #(
    #    'vendor/bin/hw/vendor.qti.hardware.display.composer-service'
    #): blob_fixup()
    #    .replace_needed('vendor.qti.hardware.display.config-V11-ndk.so', 'vendor.qti.hardware.display.config-V8-ndk.so'),
    'vendor/lib64/android.hardware.bluetooth.audio-V3-ndk.so': blob_fixup()
        .replace_needed('android.hardware.audio.common-V1-ndk.so', 'android.hardware.audio.common-V2-ndk.so'),    
    (
        'vendor/lib64/libbluetooth_audio_session_aidl.so',
        'vendor/lib64/libbluetooth_audio_session_aidl_qti.so',
        'vendor/lib64/hw/audio.bluetooth_qti.default.so'
    )
    : blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V3-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so'),
    (
        'vendor/lib64/hw/android.hardware.bluetooth.audio-impl-qti.so',
        'vendor/lib64/btaudio_offload_if.so'
    )
    : blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V3-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so')
        .replace_needed('android.media.audio.common.types-V2-ndk.so', 'android.media.audio.common.types-V4-ndk.so'),
    'vendor/lib64/hw/audio.bluetooth.default.so': blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V3-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so')
        .replace_needed('android.hardware.audio.common-V2-ndk.so', 'android.hardware.audio.common-V4-ndk.so'),
    (
        'vendor/lib64/android.frameworks.sensorservice-V1-ndk.so',
        'vendor/bin/hw/android.hardware.sensors-service.multihal',
        'vendor/lib64/libsensorndkbridge.so'
    ): blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .remove_needed('android.hardware.graphics.allocator-V1-ndk.so'),
    (
        'vendor/bin/aecxsimulator',
        'vendor/lib64/camera/components/com.qti.node.itofpreprocess.so',
        'vendor/lib64/camera/components/com.qti.node.hdr10phist.so',
        'vendor/lib64/hw/camera.qcom.so',
        'vendor/lib64/camera/components/com.qti.node.evadepth.so',
        'vendor/lib64/camera/components/com.qti.node.aon.so',
        'vendor/lib64/camera/components/com.qti.node.depthprovider.so',
        'vendor/lib64/camera/components/com.qti.node.gme.so',
        'vendor/lib64/camera/components/com.qti.node.hdr10pgen.so',
        'vendor/lib64/camera/components/com.qti.node.eisv2.so',
        'vendor/lib64/camera/components/com.qti.node.mlinference.so',
        'vendor/lib64/camera/components/com.qti.node.swvrt.so',
        'vendor/lib64/camera/components/com.qti.node.depthselector.so',
        'vendor/lib64/camera/components/com.qti.node.swregistration.so',
        'vendor/lib64/camera/components/com.qti.node.depth.so',
        'vendor/lib64/camera/components/com.qti.node.swec.so',
        'vendor/lib64/camera/components/com.qti.node.ml.so',
        'vendor/lib64/camera/components/com.qti.node.itof.so',
        'vendor/lib64/camera/components/com.qti.node.gyrornn.so',
        'vendor/lib64/camera/components/com.qti.node.dewarp.so',
        'vendor/lib64/camera/components/com.qti.node.eisv3.so',
        'vendor/lib64/camera/components/com.qti.node.seg.so',
        'vendor/lib64/com.qti.qseeutils.so',
        'vendor/lib64/com.qti.camx.chiiqutils.so',
        'vendor/lib64/libcamxncsdatafactory.so',
        'vendor/lib64/hw/camera.qcom.sm8650.so',
        'vendor/lib64/vendor.qti.hardware.camera.aon-service-impl.so',
        'vendor/lib64/libcamxhwnodecontext.so',
        'vendor/lib64/libisphwsetting.so',
        'vendor/lib64/libchifeature2.so',
        'vendor/lib64/hw/com.qti.chi.override.so',
        'vendor/lib64/camera/components/libcamxevainterface.so',
        'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so',
        'vendor/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so',
        'vendor/lib64/vendor.qti.hardware.camera.postproc-service-impl.so',
        'vendor/lib64/com.qti.feature2.generic.so',
        'vendor/lib64/com.qti.feature2.ml.so',
        'vendor/lib64/com.qti.feature2.qcfa.so',
        'vendor/lib64/com.qti.feature2.rawhdr.so',
        'vendor/lib64/com.qti.feature2.stub.so',
        'vendor/lib64/com.qti.chiusecaseselector.so',
        'vendor/lib64/com.qti.feature2.statsregeneration.so',
        'vendor/lib64/com.qti.feature2.metadataserializer.so',
        'vendor/lib64/com.qti.feature2.demux.so',
        'vendor/lib64/com.qti.feature2.e2edl.so',
        'vendor/lib64/com.qualcomm.mcx.distortionmapper.so',
        'vendor/lib64/com.qti.feature2.yuvmf.so',
        'vendor/lib64/com.qti.feature2.anchorsync.so',
        'vendor/lib64/com.qti.feature2.afbrckt.so',
        'vendor/lib64/com.qti.feature2.rtmcx.so',
        'vendor/lib64/com.qualcomm.mcx.policy.mfl.so',
        'vendor/lib64/com.qti.feature2.fusion.so',
        'vendor/lib64/com.qualcomm.mcx.linearmapper.so',
        'vendor/lib64/com.qti.feature2.swmf.so',
        'vendor/lib64/com.qualcomm.mcx.nonlinearmapper.so',
        'vendor/lib64/com.qti.feature2.mfsr.so',
        'vendor/lib64/com.qualcomm.qti.mcx.usecase.extension.so',
        'vendor/lib64/com.qti.feature2.yuvsr.so',
        'vendor/lib64/com.qti.feature2.realtimeserializer.so',
        'vendor/lib64/com.qti.feature2.mux.so',
        'vendor/lib64/com.qti.feature2.memcpy.so',
        'vendor/lib64/com.qti.feature2.mcreprocrt.so',
        'vendor/lib64/com.qti.feature2.hdr.so',
        'vendor/lib64/com.qti.feature2.serializer.so',
        'vendor/lib64/com.qti.feature2.rt.so',
        'vendor/lib64/hw/com.qti.chi.offline.so',
        'vendor/lib64/libcamerapostproc.so',
        'vendor/lib64/com.qti.feature2.derivedoffline.so',
        'vendor/lib64/com.qti.feature2.arcrawpro.so',
        'vendor/lib64/com.qti.feature2.arctf.so',
        'vendor/lib64/com.qti.feature2.gs.sm8650.so'        
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),

    'vendor/lib64/libcamera2ndk_vendor.so': blob_fixup()
        .replace_needed('android.frameworks.cameraservice.device-V1-ndk.so', 'android.frameworks.cameraservice.device-V3-ndk.so')
        .replace_needed('android.frameworks.cameraservice.service-V1-ndk.so', 'android.frameworks.cameraservice.service-V3-ndk.so'),

    'vendor/lib64/camera.device-external-impl.so': blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so')
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V6-ndk.so'),    
    'vendor/lib64/libproj_sot.so': blob_fixup()
        .remove_needed('ld-android.so'),
    'vendor/lib64/libcommonchiutils.so': blob_fixup()
        .remove_needed('android.hardware.graphics.allocator-V1-ndk.so'),
    (
        'vendor/lib64/libSNPE.so'
    ): blob_fixup()
        .add_needed('libemutls_get_address.so'),
    'vendor/lib64/libqcodec2_core.so': blob_fixup()
        .add_needed('libcodec2_shim.so'),
    'vendor/lib64/vendor.libdpmframework.so': blob_fixup()
        .add_needed('libhidlbase_shim.so'),
    'vendor/lib64/libarcsoft_high_dynamic_range_v5.so': blob_fixup()
        .clear_symbol_version('remote_register_buf'),
    (
        'vendor/lib64/libTrueSight.so'
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
}  # fmt: skip

module = ExtractUtilsModule(
    'm2481',
    'meizu',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
