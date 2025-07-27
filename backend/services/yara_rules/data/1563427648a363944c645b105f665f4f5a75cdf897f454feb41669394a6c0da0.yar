rule auto_rule_20250727020904_7439 {
  strings:
    $o0 = "dword_41834C" wide ascii nocase
  condition:
    all of them
}