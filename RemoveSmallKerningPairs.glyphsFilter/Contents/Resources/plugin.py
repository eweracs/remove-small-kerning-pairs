# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *


class RemoveSmallKerningPairs(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			"en": "Remove Small Kerning Pairs",
			"de": "Kleine Kerningpaare entfernen",
			"es": "Eliminar pares de kerning pequeños",
			"fr": "Supprimer les petites paires de kerning",
			"ja": "小さなカーニングペアを削除",
			"ko": "작은 캐닝 페어 제거",
			"zh": "删除小的字距对",
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		if len(customParameters) == 0:
			threshold = 5
		else:
			threshold = customParameters[0]
		font = layer.font()
		if layer.parent != font.glyphs[0]:
			return
		for master in font.masters:
			pairs_to_round = []
			master_kerning = font.kerning[master.id]
			for left in master_kerning.keys():
				left_kerning = master_kerning[left]
				for right in left_kerning.keys():
					value = left_kerning[right]
					if abs(value) < threshold:
						pairs_to_round.append((left, right))

			for pair in pairs_to_round:
				left_kerning = master_kerning[pair[0]]
				left_kerning[pair[1]] = 0

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
