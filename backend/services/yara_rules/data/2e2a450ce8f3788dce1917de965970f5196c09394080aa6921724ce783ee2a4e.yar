rule auto_rule_20250726131714_5916 {
  strings:
    $o0 = "dword_45B498" wide ascii nocase
    $o1 = "dword_45AFE4" wide ascii nocase
  condition:
    all of them
}