rule auto_rule_20250726065048_2426 {
  strings:
    $o0 = "__sbh_alloc_new_region" wide ascii nocase
    $o1 = "x4046F1" wide ascii nocase
  condition:
    all of them
}