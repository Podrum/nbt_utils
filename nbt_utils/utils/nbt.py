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

from nbt_utils.tag_identifiers import TagIdentifiers

class Nbt:
    @staticmethod
    def new_tag(tag_id: int) -> object:
        from nbt_utils.tag.byte_array_tag import ByteArrayTag
        from nbt_utils.tag.byte_tag import ByteTag
        from nbt_utils.tag.compound_tag import CompoundTag
        from nbt_utils.tag.double_tag import DoubleTag
        from nbt_utils.tag.end_tag import EndTag
        from nbt_utils.tag.float_tag import FloatTag
        from nbt_utils.tag.int_array_tag import IntArrayTag
        from nbt_utils.tag.int_tag import IntTag
        from nbt_utils.tag.list_tag import ListTag
        from nbt_utils.tag.long_array_tag import LongArrayTag
        from nbt_utils.tag.long_tag import LongTag
        from nbt_utils.tag.short_tag import ShortTag
        from nbt_utils.tag.string_tag import StringTag
        if tag_id == TagIdentifiers.END_TAG:
            return EndTag()
        if tag_id == TagIdentifiers.BYTE_TAG:
            return ByteTag()
        if tag_id == TagIdentifiers.SHORT_TAG:
            return ShortTag()
        if tag_id == TagIdentifiers.INT_TAG:
            return IntTag()
        if tag_id == TagIdentifiers.LONG_TAG:
            return LongTag()
        if tag_id == TagIdentifiers.FLOAT_TAG:
            return FloatTag()
        if tag_id == TagIdentifiers.DOUBLE_TAG:
            return DoubleTag()
        if tag_id == TagIdentifiers.BYTE_ARRAY_TAG:
            return ByteArrayTag()
        if tag_id == TagIdentifiers.STRING_TAG:
            return StringTag()
        if tag_id == TagIdentifiers.LIST_TAG:
            return ListTag()
        if tag_id == TagIdentifiers.COMPOUND_TAG:
            return CompoundTag()
        if tag_id == TagIdentifiers.INT_ARRAY_TAG:
            return IntArrayTag()
        if tag_id == TagIdentifiers.LONG_ARRAY_TAG:
            return LongArrayTag()
