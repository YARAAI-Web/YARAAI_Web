rule auto_rule_20250726070945_2041 {
  strings:
    $o0 = "_Init_locks" wide ascii nocase
    $o1 = "Western" wide ascii nocase
  condition:
    all of them
}