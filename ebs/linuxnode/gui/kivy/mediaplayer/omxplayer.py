

from ebs.linuxnode.core.config import ElementSpec, ItemSpec
from ebs.linuxnode.gui.kivy.mediaplayer.mixin import MediaPlayerGuiMixin

from ebs.linuxnode.mediaplayer.manager import MAIN
from ebs.linuxnode.mediaplayer.manager import BACKGROUND

from .players.omxplayer import OMXPlayer


class OMXPlayerGuiMixin(MediaPlayerGuiMixin):
    def __init__(self, *args, **kwargs):
        super(OMXPlayerGuiMixin, self).__init__(*args, **kwargs)

    def install(self):
        super(OMXPlayerGuiMixin, self).install()
        if not self.config.platform == 'rpi':
            return
        _elements = {
            'video_dispmanx_layer': ElementSpec('video-rpi', 'dispmanx_video_layer', ItemSpec(int, fallback=-200)),
        }
        for name, spec in _elements.items():
            self.config.register_element(name, spec)
        self.media_player_manager(MAIN).install_player(OMXPlayer(MAIN, self), index=-1)
        self.media_player_manager(BACKGROUND).install_player(OMXPlayer(BACKGROUND, self), index=-1)

    def gui_setup(self):
        gui = super(MediaPlayerGuiMixin, self).gui_setup()
        return gui
