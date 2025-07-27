rule auto_rule_20250726090929_3846 {
  strings:
    $o0 = "SetMenuItemInfoA" wide ascii nocase
    $o1 = "dwDefaultDataSize" wide ascii nocase
    $o2 = "lpAccelDst" wide ascii nocase
  condition:
    3 of ($o*)
}