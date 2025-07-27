rule auto_rule_20250726104551_3515 {
  strings:
    $o0 = "x1073u" wide ascii nocase
    $o1 = "dword_42069C" wide ascii nocase
  condition:
    all of them
}