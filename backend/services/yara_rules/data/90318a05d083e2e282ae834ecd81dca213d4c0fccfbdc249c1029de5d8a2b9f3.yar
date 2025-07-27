rule auto_rule_20250726214318_6793 {
  strings:
    $o0 = "dword_780C4" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}