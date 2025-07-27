rule auto_rule_20250726140451_2258 {
  strings:
    $o0 = "off_40A1E8" wide ascii nocase
    $o1 = "TrackPopupMenu" wide ascii nocase
  condition:
    all of them
}