rule auto_rule_20250726154918_3463 {
  strings:
    $o0 = "dword_428ECB" wide ascii nocase
  condition:
    all of them
}