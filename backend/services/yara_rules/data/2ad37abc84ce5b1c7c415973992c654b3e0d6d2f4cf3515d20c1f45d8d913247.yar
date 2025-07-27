rule auto_rule_20250726231555_1097 {
  strings:
    $o0 = "x21C00" wide ascii nocase
    $o1 = "dword_458268" wide ascii nocase
  condition:
    all of them
}