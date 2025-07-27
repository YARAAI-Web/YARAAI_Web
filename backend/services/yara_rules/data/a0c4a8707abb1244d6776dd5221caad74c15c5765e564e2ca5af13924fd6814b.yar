rule auto_rule_20250726180417_6240 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "phmx" wide ascii nocase
  condition:
    all of them
}