rule auto_rule_20250727041111_7947 {
  strings:
    $o0 = "dword_640334D8" wide ascii nocase
  condition:
    all of them
}