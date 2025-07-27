rule auto_rule_20250726124206_3350 {
  strings:
    $o0 = "dword_464280" wide ascii nocase
    $o1 = "Offset" wide ascii nocase
  condition:
    all of them
}