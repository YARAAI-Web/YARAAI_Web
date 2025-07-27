rule auto_rule_20250727032658_1040 {
  strings:
    $o0 = "_nh_malloc_dbg" wide ascii nocase
  condition:
    all of them
}