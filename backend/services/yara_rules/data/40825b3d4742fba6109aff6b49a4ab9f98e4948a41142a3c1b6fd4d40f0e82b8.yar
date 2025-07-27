rule auto_rule_20250726194530_5570 {
  strings:
    $o0 = "main_loop_0" wide ascii nocase
    $o1 = "dword_45D8A8" wide ascii nocase
  condition:
    all of them
}