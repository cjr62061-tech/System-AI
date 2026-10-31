[app]
title = Bhai Ka AI
package.name = bhaikaai
package.domain = com.bhai.ai

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,Flask,requests,openai
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# --- Android ke liye ---
[app:android]
# Tera APK banega yaha se
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

# --- Build ---
[build]