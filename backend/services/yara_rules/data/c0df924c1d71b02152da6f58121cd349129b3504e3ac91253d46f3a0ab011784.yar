rule auto_rule_20250726133950_3371 {
  strings:
    $o0 = "dword_545BD4" wide ascii nocase
  condition:
    all of them
}