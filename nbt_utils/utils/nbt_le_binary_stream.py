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

from binary_utils.binary_stream import binary_stream
from nbt_utils.tag.end_tag import end_tag
from nbt_utils.utils.nbt import nbt

class nbt_le_binary_stream(binary_stream):
    def read_byte_tag(self) -> int:
        return self.read_byte()
      
    def write_byte_tag(self, value: int) -> None:
        self.write_byte(value)
        
    def read_short_tag(self) -> int:
        return self.read_short_le()
      
    def write_short_tag(self, value: int) -> None:
        self.write_short_le(value)
        
    def read_int_tag(self) -> int:
        return self.read_int_le()
      
    def write_int_tag(self, value: int) -> None:
        self.write_int_le(value)
        
    def read_long_tag(self) -> int:
        return self.read_long_le()
      
    def write_long_tag(self, value: int) -> None:
        self.write_long_le(value)
        
    def read_float_tag(self) -> float:
        return self.read_float_le()
      
    def write_float_tag(self, value: float) -> None:
        self.write_float_le(value)
        
    def read_double_tag(self) -> float:
        return self.read_double_le()
      
    def write_double_tag(self, value: float) -> None:
        self.write_double_le(value)
            
    def read_string_tag(self) -> str:
        return self.read(self.read_unsigned_short_le()).decode()
      
    def write_string_tag(self, value: str) -> None:
        self.write_unsigned_short_le(len(value))
        self.write(value.encode())

    def read_root_tag(self) -> object:
        if not self.feos():
            new_tag: object = nbt.new_tag(self.read_byte_tag())
            if not isinstance(new_tag, end_tag):
                new_tag.name: str = self.read_string_tag()
                new_tag.read(self)
            return new_tag

    def write_root_tag(self, value: object) -> None:
        self.write_byte_tag(value.id)
        if not isinstance(value, end_tag):
            self.write_string_tag(value.name)
            value.write(self)
