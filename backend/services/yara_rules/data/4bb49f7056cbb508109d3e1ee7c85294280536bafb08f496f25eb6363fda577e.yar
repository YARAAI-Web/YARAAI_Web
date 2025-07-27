rule auto_rule_20250726213227_8991 {
  strings:
    $o0 = "IsCharLowerW" wide ascii nocase
    $o1 = "lpMessageCount" wide ascii nocase
  condition:
    all of them
}