rule auto_rule_20250727032913_9104 {
  strings:
    $o0 = "EF8h" wide ascii nocase
    $o1 = "dword_6402F590" wide ascii nocase
  condition:
    all of them
}