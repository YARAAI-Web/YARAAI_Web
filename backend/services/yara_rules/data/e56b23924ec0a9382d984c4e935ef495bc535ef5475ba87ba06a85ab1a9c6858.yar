rule auto_rule_20250726062021_7744 {
  strings:
    $o0 = "byte_446CCC" wide ascii nocase
    $o1 = "dword_447B3C" wide ascii nocase
  condition:
    all of them
}