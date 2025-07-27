rule auto_rule_20250726110320_5262 {
  strings:
    $o0 = "IsBadWritePtr" wide ascii nocase
    $o1 = "dword_467CCC" wide ascii nocase
  condition:
    all of them
}