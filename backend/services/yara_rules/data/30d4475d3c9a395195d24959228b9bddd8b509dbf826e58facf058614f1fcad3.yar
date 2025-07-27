rule auto_rule_20250726225255_7944 {
  strings:
    $o0 = "dword_411D74" wide ascii nocase
    $o1 = "dword_412228" wide ascii nocase
    $o2 = "old_esp" wide ascii nocase
    $o3 = "dword_411984" wide ascii nocase
  condition:
    4 of ($o*)
}