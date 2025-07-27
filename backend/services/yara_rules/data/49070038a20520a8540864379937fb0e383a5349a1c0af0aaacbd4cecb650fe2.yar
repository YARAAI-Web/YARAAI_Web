rule auto_rule_20250726104740_3279 {
  strings:
    $o0 = "GetItemData" wide ascii nocase
    $o1 = "wxDataViewColumn" wide ascii nocase
    $o2 = "CloseSubpath" wide ascii nocase
    $o3 = "SetThumbnailClip" wide ascii nocase
    $o4 = "Tile" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726104743_2009 {
  strings:
    $o0 = "wxView" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726104746_5930 {
  condition:
    auto_rule_20250726104740_3279 or auto_rule_20250726104743_2009
}