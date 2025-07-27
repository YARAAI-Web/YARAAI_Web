rule auto_rule_20250726185208_8210 {
  strings:
    $o0 = "dword_640303D4" wide ascii nocase
  condition:
    all of them
}