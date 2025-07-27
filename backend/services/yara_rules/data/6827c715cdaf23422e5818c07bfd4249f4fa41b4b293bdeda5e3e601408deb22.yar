rule auto_rule_20250726073916_4941 {
  strings:
    $o0 = "RedrawWindow" wide ascii nocase
    $o1 = "bProcessSecurity" wide ascii nocase
    $o2 = "SetCalendarInfoA" wide ascii nocase
  condition:
    3 of ($o*)
}