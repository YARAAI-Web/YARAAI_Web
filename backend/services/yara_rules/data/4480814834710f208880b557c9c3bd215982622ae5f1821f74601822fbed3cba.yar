rule auto_rule_20250726133916_3519 {
  strings:
    $o0 = "EnumWindowStationsW" wide ascii nocase
    $o1 = "GetWindowTextA" wide ascii nocase
    $o2 = "lpNewItem" wide ascii nocase
  condition:
    3 of ($o*)
}