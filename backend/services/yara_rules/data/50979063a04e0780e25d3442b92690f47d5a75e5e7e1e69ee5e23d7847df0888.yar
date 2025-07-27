rule auto_rule_20250726114526_3762 {
  strings:
    $o0 = "dword_401890" wide ascii nocase
  condition:
    all of them
}