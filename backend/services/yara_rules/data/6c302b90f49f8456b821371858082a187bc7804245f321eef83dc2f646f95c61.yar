rule auto_rule_20250726170044_7105 {
  strings:
    $o0 = "dword_6403034C" wide ascii nocase
  condition:
    all of them
}