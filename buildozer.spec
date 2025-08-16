[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3==3.10.12,kivy==2.3.1,pyjnius==1.6.1
version = 0.1

# API level target
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
orientation = portrait
