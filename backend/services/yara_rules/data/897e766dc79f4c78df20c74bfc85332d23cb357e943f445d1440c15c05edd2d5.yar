rule auto_rule_20250727014558_3056 {
  strings:
    $o0 = "x4721AD2E" wide ascii nocase
  condition:
    all of them
}