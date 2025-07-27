rule auto_rule_20250726175229_4224 {
  strings:
    $o0 = "dword_14010F2E0" wide ascii nocase
  condition:
    all of them
}