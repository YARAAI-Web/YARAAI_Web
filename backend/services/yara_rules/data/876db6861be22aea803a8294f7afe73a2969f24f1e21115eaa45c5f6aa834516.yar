rule auto_rule_20250726211903_0807 {
  strings:
    $o0 = "dword_6402E060" wide ascii nocase
  condition:
    all of them
}