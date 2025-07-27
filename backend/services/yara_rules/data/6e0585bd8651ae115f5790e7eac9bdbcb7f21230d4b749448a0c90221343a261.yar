rule auto_rule_20250726091109_8254 {
  strings:
    $o0 = "slice_start_index_len_fail" wide ascii nocase
  condition:
    all of them
}