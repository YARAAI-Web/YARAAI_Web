rule auto_rule_20250727024936_0691 {
  strings:
    $o0 = "dword_14015B4A8" wide ascii nocase
    $o1 = "dword_14015B4C4" wide ascii nocase
    $o2 = "dword_14015B4E0" wide ascii nocase
    $o3 = "v272" wide ascii nocase
  condition:
    4 of ($o*)
}