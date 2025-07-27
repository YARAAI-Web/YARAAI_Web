rule auto_rule_20250727022221_5654 {
  strings:
    $o0 = "GdipFree" wide ascii nocase
    $o1 = "dword_4561E4" wide ascii nocase
  condition:
    all of them
}