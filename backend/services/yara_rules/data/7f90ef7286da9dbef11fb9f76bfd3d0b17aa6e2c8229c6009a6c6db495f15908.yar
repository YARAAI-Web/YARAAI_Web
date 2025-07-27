rule auto_rule_20250727012807_6302 {
  strings:
    $o0 = "dword_41D990" wide ascii nocase
    $o1 = "TextOutA" wide ascii nocase
  condition:
    all of them
}