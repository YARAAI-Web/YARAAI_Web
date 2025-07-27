rule auto_rule_20250726104718_5995 {
  strings:
    $o0 = "j_j__free" wide ascii nocase
    $o1 = "dword_6402E994" wide ascii nocase
  condition:
    all of them
}