rule auto_rule_20250726115743_3692 {
  strings:
    $o0 = "dword_429524" wide ascii nocase
    $o1 = "x2057" wide ascii nocase
    $o2 = "BC8h" wide ascii nocase
    $o3 = "off_429100" wide ascii nocase
    $o4 = "dword_4295F0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726115746_4927 {
  strings:
    $o0 = "dword_429640" wide ascii nocase
    $o1 = "dword_429384" wide ascii nocase
    $o2 = "dword_429600" wide ascii nocase
    $o3 = "dword_42969C" wide ascii nocase
    $o4 = "dword_4294F0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726115749_1827 {
  condition:
    auto_rule_20250726115743_3692 or auto_rule_20250726115746_4927
}