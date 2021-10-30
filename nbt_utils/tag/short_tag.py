r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
 
 Copyright 2021 Podrum Team.
 
 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

from nbt_utils.tag_identifiers import TagIdentifiers


class ShortTag:
    def __init__(self, name: str = "", value: int = 0) -> None:
        self.id: int = TagIdentifiers.SHORT_TAG
        self.name: str = name
        self.value: int = value
        
    def read(self, stream) -> None:
        self.value = stream.read_short_tag()
        
    def write(self, stream) -> None:
        stream.write_short_tag(self.value)
