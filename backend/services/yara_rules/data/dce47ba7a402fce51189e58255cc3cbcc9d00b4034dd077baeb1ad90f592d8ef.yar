rule auto_rule_20250726134540_8796 {
  strings:
    $o0 = "found_bx" wide ascii nocase
    $o1 = "dword_476980" wide ascii nocase
  condition:
    all of them
}