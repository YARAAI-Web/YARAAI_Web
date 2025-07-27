rule auto_rule_20250726061115_7573 {
  strings:
    $o0 = "dword_42830F" wide ascii nocase
    $o1 = "x55EFu" wide ascii nocase
    $o2 = "dword_4282AB" wide ascii nocase
    $o3 = "SourceString" wide ascii nocase
    $o4 = "dword_4281A3" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726061118_6216 {
  strings:
    $o0 = "x6EC3" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726061120_4012 {
  condition:
    auto_rule_20250726061115_7573 or auto_rule_20250726061118_6216
}