[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3==3.11.13,kivy==2.3.1

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support.
android.ndk_api = 21

# (str) Android build-tools version
android.build_tools_version = 33.0.2

# (bool) Android logcat filters to include in log output
android.logcat_filters = *:S python:D

# (list) Permissions
android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Presplash background color (for android toolchain)
#android.presplash_color = #FFFFFF

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

#
# OSX Specific
#
osx.python_version = 3
osx.kivy_version = 1.9.1

#
# Buildozer logging and debug
#
log_level = 2
warn_on_root = 1
