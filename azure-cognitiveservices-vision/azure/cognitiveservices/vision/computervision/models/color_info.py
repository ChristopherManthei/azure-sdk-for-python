# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ColorInfo(Model):
    """An object providing additional metadata describing color attributes.

    :param dominant_color_foreground: Possible dominant foreground color.
    :type dominant_color_foreground: str
    :param dominant_color_background: Possible dominant background color.
    :type dominant_color_background: str
    :param dominant_colors: An array of possible dominant colors.
    :type dominant_colors: list[str]
    :param accent_color: Possible accent color.
    :type accent_color: str
    :param is_bw_img: A value indicating if the image is black and white.
    :type is_bw_img: bool
    """

    _attribute_map = {
        'dominant_color_foreground': {'key': 'dominantColorForeground', 'type': 'str'},
        'dominant_color_background': {'key': 'dominantColorBackground', 'type': 'str'},
        'dominant_colors': {'key': 'dominantColors', 'type': '[str]'},
        'accent_color': {'key': 'accentColor', 'type': 'str'},
        'is_bw_img': {'key': 'isBWImg', 'type': 'bool'},
    }

    def __init__(self, dominant_color_foreground=None, dominant_color_background=None, dominant_colors=None, accent_color=None, is_bw_img=None):
        self.dominant_color_foreground = dominant_color_foreground
        self.dominant_color_background = dominant_color_background
        self.dominant_colors = dominant_colors
        self.accent_color = accent_color
        self.is_bw_img = is_bw_img
