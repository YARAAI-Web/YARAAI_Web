rule auto_rule_20250726150021_5224 {
  strings:
    $o0 = "dword_4C15F8" wide ascii nocase
  condition:
    all of them
}