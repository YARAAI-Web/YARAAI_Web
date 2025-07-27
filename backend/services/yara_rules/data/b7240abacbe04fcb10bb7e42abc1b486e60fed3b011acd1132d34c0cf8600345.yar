rule auto_rule_20250726141332_4902 {
  strings:
    $o0 = "dword_14010F6DC" wide ascii nocase
  condition:
    all of them
}