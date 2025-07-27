rule auto_rule_20250726115851_7625 {
  strings:
    $o0 = "DefaultChar" wide ascii nocase
    $o1 = "x73B3" wide ascii nocase
    $o2 = "x66E0u" wide ascii nocase
  condition:
    3 of ($o*)
}