rule auto_rule_20250726090728_4941 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "byte_73520" wide ascii nocase
    $o2 = "dword_78174" wide ascii nocase
  condition:
    3 of ($o*)
}