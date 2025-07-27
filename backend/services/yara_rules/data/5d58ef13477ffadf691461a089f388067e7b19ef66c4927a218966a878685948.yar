rule auto_rule_20250726152003_0326 {
  strings:
    $o0 = "CharLowerBuffW" wide ascii nocase
    $o1 = "OpenServiceW" wide ascii nocase
    $o2 = "dwNotifyFilter" wide ascii nocase
    $o3 = "dwMaximumSizeLow" wide ascii nocase
  condition:
    4 of ($o*)
}