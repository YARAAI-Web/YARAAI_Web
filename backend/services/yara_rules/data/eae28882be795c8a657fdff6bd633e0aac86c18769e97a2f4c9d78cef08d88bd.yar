rule auto_rule_20250727001231_6929 {
  strings:
    $o0 = "main_loop_entrance" wide ascii nocase
    $o1 = "dword_462020" wide ascii nocase
  condition:
    all of them
}