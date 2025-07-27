rule auto_rule_20250726170804_7279 {
  strings:
    $o0 = "aWmCommand" wide ascii nocase
    $o1 = "dword_41DA98" wide ascii nocase
  condition:
    all of them
}