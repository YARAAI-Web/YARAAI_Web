rule auto_rule_20250726154527_3366 {
  strings:
    $o0 = "dword_4668E0" wide ascii nocase
    $o1 = "dword_4668E4" wide ascii nocase
  condition:
    all of them
}