rule auto_rule_20250726100008_4743 {
  strings:
    $o0 = "UnwindUp6_0" wide ascii nocase
    $o1 = "dword_45C314" wide ascii nocase
  condition:
    all of them
}