rule auto_rule_20250726074632_4425 {
  strings:
    $o0 = "fFlags" wide ascii nocase
    $o1 = "dword_44A08C" wide ascii nocase
  condition:
    all of them
}