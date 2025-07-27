rule auto_rule_20250726104036_2621 {
  strings:
    $o0 = "fpstat" wide ascii nocase
    $o1 = "dword_4C218C" wide ascii nocase
  condition:
    all of them
}