rule auto_rule_20250726153759_6790 {
  strings:
    $o0 = "dword_468D54" wide ascii nocase
    $o1 = "dword_4673C0" wide ascii nocase
  condition:
    all of them
}