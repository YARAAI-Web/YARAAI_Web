rule auto_rule_20250726095739_2317 {
  strings:
    $o0 = "dword_469B9C" wide ascii nocase
    $o1 = "byte_469D80" wide ascii nocase
  condition:
    all of them
}