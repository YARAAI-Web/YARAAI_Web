rule auto_rule_20250727012623_5495 {
  strings:
    $o0 = "dword_64032D70" wide ascii nocase
  condition:
    all of them
}