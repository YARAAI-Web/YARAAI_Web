rule auto_rule_20250726080512_1442 {
  strings:
    $o0 = "x140u" wide ascii nocase
    $o1 = "dword_412228" wide ascii nocase
  condition:
    all of them
}