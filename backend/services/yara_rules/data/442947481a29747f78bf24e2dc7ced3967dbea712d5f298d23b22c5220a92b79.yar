rule auto_rule_20250727015059_2631 {
  strings:
    $o0 = "x7510851u" wide ascii nocase
    $o1 = "dword_414B82" wide ascii nocase
    $o2 = "x69CA0B32" wide ascii nocase
    $o3 = "dword_414BD6" wide ascii nocase
    $o4 = "x7510851" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727015102_4201 {
  strings:
    $o0 = "x46B5u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727015106_6311 {
  condition:
    auto_rule_20250727015059_2631 or auto_rule_20250727015102_4201
}