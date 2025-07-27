rule auto_rule_20250727005328_6900 {
  strings:
    $o0 = "DrawTextW" wide ascii nocase
    $o1 = "iCodePage" wide ascii nocase
    $o2 = "uFormat" wide ascii nocase
    $o3 = "dwExtraInfo" wide ascii nocase
    $o4 = "hcur" wide ascii nocase
  condition:
    5 of ($o*)
}