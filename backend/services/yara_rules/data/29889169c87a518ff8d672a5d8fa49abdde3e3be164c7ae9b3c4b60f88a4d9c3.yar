rule auto_rule_20250726063804_7886 {
  strings:
    $o0 = "hWritePipe" wide ascii nocase
    $o1 = "byte_64030190" wide ascii nocase
  condition:
    all of them
}