[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3==3.11.13,kivy==2.3.1

# API level target
android.api = 33

# الحد الأدنى من API
android.minapi = 21

# إصدار NDK
android.ndk = 25b

# قبول تراخيص SDK تلقائيًا
android.accept_sdk_license = True

orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
