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


class IntArrayTag:
    def __init__(self, name: str = "", value: list = []) -> None:
        self.id: int = TagIdentifiers.INT_ARRAY_TAG
        self.name: str = name
        self.value: list = value
        
    def read(self, stream) -> None:
        length: int = stream.read_int_tag()
        self.value = []
        for i in range(0, length):
            self.value.append(stream.read_int_tag())
        
    def write(self, stream) -> None:
        stream.write_int_tag(len(self.value))
        for tag in self.value:
            stream.write_int_tag(tag)
