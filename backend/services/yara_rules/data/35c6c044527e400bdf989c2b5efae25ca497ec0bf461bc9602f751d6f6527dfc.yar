rule auto_rule_20250726073010_3978 {
  strings:
    $o0 = "__sbh_alloc_new_region" wide ascii nocase
    $o1 = "byte_45D580" wide ascii nocase
  condition:
    all of them
}