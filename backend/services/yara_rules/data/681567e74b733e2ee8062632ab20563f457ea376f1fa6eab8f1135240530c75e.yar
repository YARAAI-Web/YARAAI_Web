rule auto_rule_20250726095831_1531 {
  strings:
    $o0 = "lopen" wide ascii nocase
    $o1 = "lpExitTime" wide ascii nocase
    $o2 = "lpBytesLeftThisMessage" wide ascii nocase
  condition:
    3 of ($o*)
}