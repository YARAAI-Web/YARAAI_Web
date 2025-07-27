rule auto_rule_20250726171453_6518 {
  strings:
    $o0 = "word_4673EC" wide ascii nocase
    $o1 = "_nh_malloc_dbg" wide ascii nocase
    $o2 = "FlushFileBuffers" wide ascii nocase
  condition:
    3 of ($o*)
}