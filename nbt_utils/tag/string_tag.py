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


class StringTag:
    def __init__(self, name: str = "", value: str = "") -> None:
        self.id: int = TagIdentifiers.STRING_TAG
        self.name: str = name
        self.value: str = value
        
    def read(self, stream) -> None:
        self.value = stream.read_string_tag()
        
    def write(self, stream) -> None:
        stream.write_string_tag(self.value)
