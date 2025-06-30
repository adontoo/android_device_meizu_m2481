#
# Copyright (C) 2023 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from m2481 device.
$(call inherit-product, device/meizu/m2481/device.mk)

# Inherit Gapps if exists
#$(call inherit-product, vendor/gapps/arm64/arm64-vendor.mk)

## Device identifier
PRODUCT_BRAND := Meizu
PRODUCT_DEVICE := m2481
PRODUCT_MANUFACTURER := Meizu
PRODUCT_NAME := lineage_m2481
PRODUCT_MODEL := m2481

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc=$(call normalize-path-list, "qssi_64-user 15 AQ3A.250129.001 1740478319 release-keys")

BUILD_FINGERPRINT := meizu/meizu_21Pro_CN/meizu21Pro:15/AQ3A.241229.001/1740478319:user/release-keys

# GMS
PRODUCT_GMS_CLIENTID_BASE := android-meizu
