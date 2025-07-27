rule auto_rule_20250727003236_7424 {
  strings:
    $o0 = "dword_78570" wide ascii nocase
    $o1 = "byte_73B70" wide ascii nocase
    $o2 = "dword_786C8" wide ascii nocase
    $o3 = "ZwOpenProcess" wide ascii nocase
  condition:
    4 of ($o*)
}