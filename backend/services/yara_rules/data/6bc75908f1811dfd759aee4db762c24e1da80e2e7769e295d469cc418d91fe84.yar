rule auto_rule_20250726164049_1771 {
  strings:
    $o0 = "nCmdShow" wide ascii nocase
    $o1 = "aNegopenkeyw" wide ascii nocase
  condition:
    all of them
}