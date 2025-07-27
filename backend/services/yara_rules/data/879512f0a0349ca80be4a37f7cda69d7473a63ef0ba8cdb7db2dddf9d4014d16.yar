rule auto_rule_20250727031335_1922 {
  strings:
    $o0 = "dword_456F8C" wide ascii nocase
  condition:
    all of them
}