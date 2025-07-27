rule auto_rule_20250726062107_7749 {
  strings:
    $o0 = "dwOpenMode" wide ascii nocase
    $o1 = "dword_446FA8" wide ascii nocase
    $o2 = "dyHotspot" wide ascii nocase
    $o3 = "rgbBk" wide ascii nocase
    $o4 = "FlatSB_GetScrollPos" wide ascii nocase
  condition:
    5 of ($o*)
}