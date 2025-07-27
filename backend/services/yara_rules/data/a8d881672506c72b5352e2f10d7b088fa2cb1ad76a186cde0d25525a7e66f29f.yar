rule auto_rule_20250726115317_3621 {
  strings:
    $o0 = "dword_437728" wide ascii nocase
  condition:
    all of them
}