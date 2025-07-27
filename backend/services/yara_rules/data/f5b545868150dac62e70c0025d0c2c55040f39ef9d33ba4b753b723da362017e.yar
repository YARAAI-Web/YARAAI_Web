rule auto_rule_20250727034323_9207 {
  strings:
    $o0 = "__crtMessageBoxA" wide ascii nocase
    $o1 = "dword_45D8B8" wide ascii nocase
  condition:
    all of them
}