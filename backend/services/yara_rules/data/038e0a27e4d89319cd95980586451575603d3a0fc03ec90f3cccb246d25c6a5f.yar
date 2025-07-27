rule auto_rule_20250726134417_8377 {
  strings:
    $o0 = "dword_42796C" wide ascii nocase
    $o1 = "dword_427998" wide ascii nocase
  condition:
    all of them
}