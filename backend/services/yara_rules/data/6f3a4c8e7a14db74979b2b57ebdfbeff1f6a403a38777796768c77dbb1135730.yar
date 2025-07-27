rule auto_rule_20250726192548_6939 {
  strings:
    $o0 = "copy_tail_loop" wide ascii nocase
    $o1 = "dword_444FE0" wide ascii nocase
  condition:
    all of them
}