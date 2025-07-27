rule auto_rule_20250726115308_1017 {
  strings:
    $o0 = "x1004u" wide ascii nocase
    $o1 = "dword_47731C" wide ascii nocase
  condition:
    all of them
}