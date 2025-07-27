rule auto_rule_20250726233902_6058 {
  strings:
    $o0 = "XAmount" wide ascii nocase
    $o1 = "LoadKeyboardLayoutA" wide ascii nocase
    $o2 = "ImpersonateDdeClientWindow" wide ascii nocase
  condition:
    3 of ($o*)
}