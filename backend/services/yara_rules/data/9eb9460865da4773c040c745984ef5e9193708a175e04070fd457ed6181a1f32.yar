rule auto_rule_20250727014402_4289 {
  strings:
    $o0 = "aClsid101a8fb9F" wide ascii nocase
  condition:
    all of them
}