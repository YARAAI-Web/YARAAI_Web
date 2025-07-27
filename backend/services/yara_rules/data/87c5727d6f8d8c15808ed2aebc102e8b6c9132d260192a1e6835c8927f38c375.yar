rule auto_rule_20250726084052_2385 {
  strings:
    $o0 = "dword_101FE144" wide ascii nocase
    $o1 = "dword_101FDB18" wide ascii nocase
    $o2 = "iostream" wide ascii nocase
  condition:
    3 of ($o*)
}