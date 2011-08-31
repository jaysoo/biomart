from models import Settings, Navigation, ThirdPartySoftware
from signals import invalidate_settings_cache, invalidate_navigation_cache, invalidate_thirdpartysoftware_cache
from django.db.models import signals

signals.post_save.connect(invalidate_settings_cache, Settings, True)
signals.post_save.connect(invalidate_navigation_cache, Navigation, True)
signals.post_save.connect(invalidate_thirdpartysoftware_cache, ThirdPartySoftware, True)

