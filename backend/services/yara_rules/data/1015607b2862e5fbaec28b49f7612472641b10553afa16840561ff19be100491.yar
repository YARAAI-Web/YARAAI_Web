rule auto_rule_20250726131124_7183 {
  strings:
    $o0 = "dword_42A771" wide ascii nocase
    $o1 = "x7E45" wide ascii nocase
    $o2 = "dword_42A7C1" wide ascii nocase
  condition:
    3 of ($o*)
}