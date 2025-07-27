rule auto_rule_20250727032114_1410 {
  strings:
    $o0 = "dwCreationDisposition" wide ascii nocase
    $o1 = "dword_402250" wide ascii nocase
  condition:
    all of them
}