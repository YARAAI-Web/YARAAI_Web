rule auto_rule_20250726230027_3908 {
  strings:
    $o0 = "dword_786E4" wide ascii nocase
    $o1 = "xFFFEFFFF" wide ascii nocase
  condition:
    all of them
}