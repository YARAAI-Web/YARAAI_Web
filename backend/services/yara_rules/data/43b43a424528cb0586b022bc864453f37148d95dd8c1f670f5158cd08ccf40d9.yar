rule auto_rule_20250726081109_3792 {
  strings:
    $o0 = "GetWindowContextHelpId" wide ascii nocase
    $o1 = "ExeNameBuffer" wide ascii nocase
    $o2 = "DrawAnimatedRects" wide ascii nocase
    $o3 = "lpszCurrent" wide ascii nocase
    $o4 = "lpFreeBytesAvailableToCaller" wide ascii nocase
  condition:
    4 of ($o*)
}