rule auto_rule_20250726201759_2795 {
  strings:
    $o0 = "dword_1EA74" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}