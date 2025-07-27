rule auto_rule_20250727022010_9211 {
  strings:
    $o0 = "lstrcatW" wide ascii nocase
    $o1 = "dword_402F34" wide ascii nocase
  condition:
    all of them
}