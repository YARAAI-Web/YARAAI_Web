rule auto_rule_20250727035802_8919 {
  strings:
    $o0 = "dword_40320C" wide ascii nocase
  condition:
    all of them
}