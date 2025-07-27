rule auto_rule_20250727005025_1818 {
  strings:
    $o0 = "x10054D68" wide ascii nocase
    $o1 = "finish_loop" wide ascii nocase
  condition:
    all of them
}