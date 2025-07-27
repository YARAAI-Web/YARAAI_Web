rule auto_rule_20250726164452_3111 {
  strings:
    $o0 = "UnwindUp5_0" wide ascii nocase
    $o1 = "stdenvp" wide ascii nocase
  condition:
    all of them
}