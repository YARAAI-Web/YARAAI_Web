rule auto_rule_20250726103318_2986 {
  strings:
    $o0 = "off_446CB8" wide ascii nocase
    $o1 = "dword_4479E8" wide ascii nocase
  condition:
    all of them
}