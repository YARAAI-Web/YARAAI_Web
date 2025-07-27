rule auto_rule_20250726224847_8456 {
  strings:
    $o0 = "dword_462020" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "dword_4643D4" wide ascii nocase
    $o3 = "tail_loop_start" wide ascii nocase
    $o4 = "copy_tail_loop" wide ascii nocase
  condition:
    4 of ($o*)
}