rule auto_rule_20250726173607_2636 {
  strings:
    $o0 = "dword_42E8A5" wide ascii nocase
    $o1 = "dword_42E8CD" wide ascii nocase
    $o2 = "dword_42E8AD" wide ascii nocase
    $o3 = "x462Du" wide ascii nocase
    $o4 = "x6D5600004239LL" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726173610_4695 {
  strings:
    $o0 = "dword_42E70D" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726173614_3502 {
  condition:
    auto_rule_20250726173607_2636 or auto_rule_20250726173610_4695
}