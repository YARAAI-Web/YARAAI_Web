rule auto_rule_20250727044654_0129 {
  strings:
    $o0 = "dword_640303DC" wide ascii nocase
  condition:
    all of them
}