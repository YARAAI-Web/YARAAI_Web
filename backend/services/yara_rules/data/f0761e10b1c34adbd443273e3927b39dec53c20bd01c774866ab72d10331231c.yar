rule auto_rule_20250726103521_6524 {
  strings:
    $o0 = "dword_449AB0" wide ascii nocase
    $o1 = "dword_449938" wide ascii nocase
  condition:
    all of them
}