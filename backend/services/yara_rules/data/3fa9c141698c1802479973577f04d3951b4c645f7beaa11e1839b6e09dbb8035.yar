rule auto_rule_20250726152448_2693 {
  strings:
    $o0 = "xB91ABEDE" wide ascii nocase
    $o1 = "xB91BABF3" wide ascii nocase
    $o2 = "a6Ek" wide ascii nocase
    $o3 = "dword_42C70D" wide ascii nocase
  condition:
    4 of ($o*)
}