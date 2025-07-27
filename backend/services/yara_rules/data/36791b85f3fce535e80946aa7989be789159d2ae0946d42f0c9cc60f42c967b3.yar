rule auto_rule_20250726123827_5339 {
  strings:
    $o0 = "dword_780D0" wide ascii nocase
  condition:
    all of them
}