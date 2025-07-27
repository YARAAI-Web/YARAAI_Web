rule auto_rule_20250726084633_3868 {
  strings:
    $o0 = "dword_45D3CC" wide ascii nocase
    $o1 = "copy_tail_loop" wide ascii nocase
  condition:
    all of them
}