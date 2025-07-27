rule auto_rule_20250727032932_5633 {
  strings:
    $o0 = "dword_1001EEF0" wide ascii nocase
  condition:
    all of them
}