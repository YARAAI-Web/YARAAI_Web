rule auto_rule_20250726224009_1689 {
  strings:
    $o0 = "_byte_0" wide ascii nocase
    $o1 = "dword_411990" wide ascii nocase
    $o2 = "byte_40F994" wide ascii nocase
    $o3 = "dword_411D7C" wide ascii nocase
  condition:
    4 of ($o*)
}