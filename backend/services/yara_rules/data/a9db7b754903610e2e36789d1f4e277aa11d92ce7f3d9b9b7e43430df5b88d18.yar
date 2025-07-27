rule auto_rule_20250727034843_0406 {
  strings:
    $o0 = "dword_465464" wide ascii nocase
    $o1 = "main_loop_1" wide ascii nocase
  condition:
    all of them
}