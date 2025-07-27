rule auto_rule_20250726164925_3183 {
  strings:
    $o0 = "dword_47265C" wide ascii nocase
    $o1 = "byte_472680" wide ascii nocase
    $o2 = "dword_47266C" wide ascii nocase
    $o3 = "byte_47225C" wide ascii nocase
    $o4 = "dword_4724F8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726164928_1877 {
  strings:
    $o0 = "dword_471A34" wide ascii nocase
    $o1 = "dword_4729C8" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726164932_2296 {
  condition:
    auto_rule_20250726164925_3183 or auto_rule_20250726164928_1877
}