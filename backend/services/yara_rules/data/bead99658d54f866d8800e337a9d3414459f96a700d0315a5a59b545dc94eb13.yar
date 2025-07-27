rule auto_rule_20250727012816_1449 {
  strings:
    $o0 = "x2FB98u" wide ascii nocase
    $o1 = "output_buffer" wide ascii nocase
  condition:
    all of them
}