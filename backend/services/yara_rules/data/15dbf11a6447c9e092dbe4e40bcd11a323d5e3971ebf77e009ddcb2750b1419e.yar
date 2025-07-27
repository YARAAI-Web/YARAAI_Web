rule auto_rule_20250726233603_1322 {
  strings:
    $o0 = "rand" wide ascii nocase
    $o1 = "nIDFirstButton" wide ascii nocase
  condition:
    all of them
}