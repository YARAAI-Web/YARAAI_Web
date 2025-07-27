rule auto_rule_20250726062902_8834 {
  strings:
    $o0 = "_mm_stream_si32" wide ascii nocase
    $o1 = "xBB4F" wide ascii nocase
  condition:
    all of them
}