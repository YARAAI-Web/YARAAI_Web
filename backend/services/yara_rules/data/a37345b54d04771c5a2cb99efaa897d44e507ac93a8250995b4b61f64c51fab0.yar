rule auto_rule_20250726060814_6227 {
  strings:
    $o0 = "byte_4051F7" wide ascii nocase
    $o1 = "dword_419260" wide ascii nocase
    $o2 = "dword_419418" wide ascii nocase
    $o3 = "dword_4193C0" wide ascii nocase
    $o4 = "byte_4142F5" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726060817_4554 {
  strings:
    $o0 = "vTUljwt9EH9Ou" wide ascii nocase
    $o1 = "dword_40EA80" wide ascii nocase
    $o2 = "dword_40BB78" wide ascii nocase
    $o3 = "WwXrR3Zy" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726060820_0409 {
  condition:
    auto_rule_20250726060814_6227 or auto_rule_20250726060817_4554
}