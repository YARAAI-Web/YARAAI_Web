rule auto_rule_20250726093046_2067 {
  strings:
    $o0 = "GetLocaleInfoA" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
    $o3 = "off_476D20" wide ascii nocase
    $o4 = "terminated" wide ascii nocase
  condition:
    5 of ($o*)
}