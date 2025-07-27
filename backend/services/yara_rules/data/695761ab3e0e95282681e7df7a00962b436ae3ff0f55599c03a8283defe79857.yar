rule auto_rule_20250726120257_0911 {
  strings:
    $o0 = "x244ECBD0u" wide ascii nocase
    $o1 = "dword_42E4B1" wide ascii nocase
    $o2 = "x7FF8u" wide ascii nocase
    $o3 = "dword_42B018" wide ascii nocase
  condition:
    4 of ($o*)
}