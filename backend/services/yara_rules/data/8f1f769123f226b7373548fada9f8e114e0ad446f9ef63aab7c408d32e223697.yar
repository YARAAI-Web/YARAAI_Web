rule auto_rule_20250726103138_7355 {
  strings:
    $o0 = "off_455214" wide ascii nocase
    $o1 = "off_455220" wide ascii nocase
    $o2 = "main_loop_entrance" wide ascii nocase
    $o3 = "dword_455330" wide ascii nocase
    $o4 = "_ms_p5_test_fdiv" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726103141_3833 {
  strings:
    $o0 = "dword_456500" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726103144_8830 {
  condition:
    auto_rule_20250726103138_7355 or auto_rule_20250726103141_3833
}