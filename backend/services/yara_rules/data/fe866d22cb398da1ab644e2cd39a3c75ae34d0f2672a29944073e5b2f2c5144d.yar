rule auto_rule_20250726161010_6437 {
  strings:
    $o0 = "xFFFFFF90" wide ascii nocase
    $o1 = "dword_4D31C4" wide ascii nocase
  condition:
    all of them
}