rule auto_rule_20250726163535_4192 {
  strings:
    $o0 = "dword_411738" wide ascii nocase
    $o1 = "mixerSetControlDetails" wide ascii nocase
    $o2 = "memcpy_0" wide ascii nocase
  condition:
    3 of ($o*)
}