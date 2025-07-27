rule auto_rule_20250726092136_7972 {
  strings:
    $o0 = "dword_7837C" wide ascii nocase
  condition:
    all of them
}