rule auto_rule_20250726220911_4695 {
  strings:
    $o0 = "x7C62u" wide ascii nocase
    $o1 = "x6F7B" wide ascii nocase
    $o2 = "xF89C85D5" wide ascii nocase
  condition:
    3 of ($o*)
}