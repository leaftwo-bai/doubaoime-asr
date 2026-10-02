# 设备注册 API URL
REGISTER_URL = "https://log-klink.zijieapi.com/service/2/device_register/"

# Settings API URL (获取 Token)
SETTINGS_URL = "https://is.snssdk.com/service/settings/v3/"

# ASR WebSocket URL
WEBSOCKET_URL = "wss://frontier-audio-ime-ws.doubao.com/ocean/api/v1/ws"

# 豆包输入法的 APP ID
AID = 401734

import os

# 官方豆包输入法内置 ASR app key；settings 返回的 app_key 已无法路由 ASR。
# 通过环境变量 ASR_APP_KEY 注入（由 .envrc.local / direnv 提供），不在源码中硬编码。
ASR_APP_KEY = os.environ.get("ASR_APP_KEY", "")

# 应用配置 (豆包输入法)
APP_CONFIG = {
    "aid": AID,
    "app_name": "oime",
    "version_code": 100307013,
    "version_name": "1.3.7",
    "manifest_version_code": 100307013,
    "update_version_code": 100307013,
    "channel": "official",
    "package": "com.bytedance.android.doubaoime",
}

# 默认设备配置 (模拟 Pixel 7 Pro)
DEFAULT_DEVICE_CONFIG = {
    "device_platform": "android",
    "os": "android",
    "os_api": "34",
    "os_version": "16",
    "device_type": "Pixel 7 Pro",
    "device_brand": "google",
    "device_model": "Pixel 7 Pro",
    "resolution": "1080*2400",
    "dpi": "420",
    "language": "zh",
    "timezone": 8,
    "access": "wifi",
    "rom": "UP1A.231005.007",
    "rom_version": "UP1A.231005.007",
}

USER_AGENT = "com.bytedance.android.doubaoime/100307013 (Linux; U; Android 16; en_US; Pixel 7 Pro; Build/BP2A.250605.031.A2; Cronet/TTNetVersion:94cf429a 2025-11-17 QuicVersion:1f89f732 2025-05-08)"