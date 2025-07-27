rule auto_rule_20250726192801_4973 {
  strings:
    $o0 = "dword_455A50" wide ascii nocase
  condition:
    all of them
}