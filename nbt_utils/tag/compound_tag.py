################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

from nbt_utils.tag.end_tag import end_tag
from nbt_utils.tag_ids import tag_ids
from nbt_utils.utils.nbt import nbt

class compound_tag:
    def __init__(self, name: str = "", value: list = []):
        self.id: int = tag_ids.compound_tag
        self.name: str = name
        self.value: list = value
        
    def read(self, stream: object) -> None:
        result = []
        while not stream.feos():
            new_tag: int = nbt.new_tag(stream.read_byte_tag())
            if isinstance(new_tag, end_tag):
                break
            new_tag.name: str = stream.read_string_tag()
            new_tag.read(stream)
            result.append(new_tag)
        self.value: list = result
        
    def write(self, stream: object) -> None:
        for tag in self.value:
            if not isinstance(tag, end_tag):
                stream.write_byte_tag(tag.id)
                stream.write_string_tag(tag.name)
                tag.write(stream)
        stream.write_byte_tag(0)
        
    def get_tag(self, name: str) -> object:
        for tag in self.value:
            if name == tag.name:
                return tag
            
    def has_tag(self, name: str) -> bool:
        for tag in self.value:
            if name == tag.name:
                return True
        return False
         
    def set_tag(self, tag: object) -> None:
        if not self.has_tag(tag.name):
            self.value.append(tag)
        else:
            for i, v in enumerate(self.value):
                if tag.name == v.name:
                    self.value[i] = tag
