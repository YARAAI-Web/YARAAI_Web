rule auto_rule_20250726174829_4819 {
  strings:
    $o0 = "GrayStringA" wide ascii nocase
    $o1 = "x41A41D" wide ascii nocase
    $o2 = "SetClassLongW" wide ascii nocase
    $o3 = "lpszWindow" wide ascii nocase
    $o4 = "pqosNew" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726174832_7353 {
  strings:
    $o0 = "x17000u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726174836_6570 {
  condition:
    auto_rule_20250726174829_4819 or auto_rule_20250726174832_7353
}