rule auto_rule_20250726115413_4215 {
  strings:
    $o0 = "xE149EBCu" wide ascii nocase
    $o1 = "x3BC4" wide ascii nocase
    $o2 = "x2442u" wide ascii nocase
  condition:
    3 of ($o*)
}