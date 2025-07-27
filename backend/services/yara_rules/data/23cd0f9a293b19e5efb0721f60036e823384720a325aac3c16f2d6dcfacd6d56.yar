rule auto_rule_20250727013138_6765 {
  strings:
    $o0 = "dword_46E010" wide ascii nocase
  condition:
    all of them
}