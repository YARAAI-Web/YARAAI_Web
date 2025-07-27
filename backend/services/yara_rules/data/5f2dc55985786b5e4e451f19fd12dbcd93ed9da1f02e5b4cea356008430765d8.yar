rule auto_rule_20250726072349_4051 {
  strings:
    $o0 = "dword_475670" wide ascii nocase
    $o1 = "main_loop_start" wide ascii nocase
  condition:
    all of them
}