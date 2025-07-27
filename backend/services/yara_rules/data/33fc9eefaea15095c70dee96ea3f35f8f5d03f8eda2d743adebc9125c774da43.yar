rule auto_rule_20250726234631_7306 {
  strings:
    $o0 = "_pFirstBlock" wide ascii nocase
    $o1 = "dword_4695BC" wide ascii nocase
  condition:
    all of them
}