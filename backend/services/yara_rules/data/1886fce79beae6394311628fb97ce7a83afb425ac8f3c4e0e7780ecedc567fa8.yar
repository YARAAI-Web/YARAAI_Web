rule auto_rule_20250726160007_5713 {
  strings:
    $o0 = "lpsUserUserInfo" wide ascii nocase
  condition:
    all of them
}