rule auto_rule_20250726225910_2236 {
  strings:
    $o0 = "dword_4555E4" wide ascii nocase
    $o1 = "dword_454F70" wide ascii nocase
  condition:
    all of them
}