rule auto_rule_20250726124229_4135 {
  strings:
    $o0 = "CreatePipe" wide ascii nocase
    $o1 = "dword_64031358" wide ascii nocase
  condition:
    all of them
}