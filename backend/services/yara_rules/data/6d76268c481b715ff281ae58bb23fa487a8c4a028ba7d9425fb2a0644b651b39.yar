rule auto_rule_20250726193146_2262 {
  strings:
    $o0 = "CopyAcceleratorTableW" wide ascii nocase
    $o1 = "SetDeskWallpaper" wide ascii nocase
    $o2 = "UrlUnescapeA" wide ascii nocase
  condition:
    3 of ($o*)
}