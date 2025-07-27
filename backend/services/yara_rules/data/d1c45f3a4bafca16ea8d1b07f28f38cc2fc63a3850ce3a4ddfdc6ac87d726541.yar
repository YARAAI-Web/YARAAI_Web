rule auto_rule_20250727044112_6676 {
  strings:
    $o0 = "x44ECu" wide ascii nocase
    $o1 = "dword_429018" wide ascii nocase
  condition:
    all of them
}