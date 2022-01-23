# OneSignal Recovery codes:
#
# a331b5708e09b676
# 9d75d5b0e949bd46
# bfd551164802c1eb
# b8a8910303553c58
# 26a357d741348429
# 0d8a3ac02b5e776d
# 75a664a087fd1626
# 7f12913b978d5745
# b9e893786254c3c5
# 3ef62fde90cb52e2

from onesignal import *

MY_APP_ID       = "6e7d93f3-9701-40c6-a497-6a8c4e6e995f"
MY_REST_API_KEY = "MWFiZWE5ZGYtZGEyNy00YjEwLTlmNjgtOGM4YTIyMzlkN2Iy"

client = OneSignal(MY_APP_ID, MY_REST_API_KEY)

notification_to_all_users = SegmentNotification(
    contents={
        "en": "Hello from OneSignal-Notifications"
    },
    delayed_option = "timezone",
    included_segments=[SegmentNotification.ALL]
)
client.send(notification_to_all_users)

