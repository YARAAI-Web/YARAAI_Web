rule auto_rule_20250726065224_0058 {
  strings:
    $o0 = "dword_6402E060" wide ascii nocase
  condition:
    all of them
}