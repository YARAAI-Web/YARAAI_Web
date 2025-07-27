rule auto_rule_20250726062616_7260 {
  strings:
    $o0 = "dwExStyle" wide ascii nocase
    $o1 = "nBitmaps" wide ascii nocase
    $o2 = "wType" wide ascii nocase
    $o3 = "afCmd" wide ascii nocase
    $o4 = "CreateStatusWindowW" wide ascii nocase
  condition:
    4 of ($o*)
}