rule auto_rule_20250726185254_2193 {
  strings:
    $o0 = "_controlfp" wide ascii nocase
    $o1 = "var_14" wide ascii nocase
    $o2 = "dword_455E0C" wide ascii nocase
  condition:
    3 of ($o*)
}