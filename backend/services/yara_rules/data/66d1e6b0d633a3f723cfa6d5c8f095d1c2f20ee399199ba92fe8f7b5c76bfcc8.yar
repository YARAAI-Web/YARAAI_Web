rule auto_rule_20250727024348_2883 {
  strings:
    $o0 = "dword_46CB28" wide ascii nocase
    $o1 = "dword_46D1A4" wide ascii nocase
  condition:
    all of them
}