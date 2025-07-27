rule auto_rule_20250726142454_3314 {
  strings:
    $o0 = "dword_78358" wide ascii nocase
  condition:
    all of them
}