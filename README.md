# remove-small-kerning-pairs

Small Glyphs PreFilter to remove small kerning pairs.

Usage: Add "RemoveSmallKerningPairs" as a PreFilter in Glyphs, with an optional argument for the threshold below with kerning pairs should be removed.

Example: `RemoveSmallKerningPairs;8` will remove all kerning pairs with an absolute value of less than 8. If no threshold is given, the default value of 5 will be used.
