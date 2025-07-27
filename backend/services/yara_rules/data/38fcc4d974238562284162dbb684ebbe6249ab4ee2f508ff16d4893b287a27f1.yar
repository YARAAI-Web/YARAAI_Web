rule auto_rule_20250727032537_5553 {
  strings:
    $o0 = "dword_427FB4" wide ascii nocase
    $o1 = "xBD3u" wide ascii nocase
  condition:
    all of them
}