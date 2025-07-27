rule auto_rule_20250726134936_8368 {
  strings:
    $o0 = "acmStreamUnprepareHeader" wide ascii nocase
    $o1 = "dword_44E5F8" wide ascii nocase
  condition:
    all of them
}