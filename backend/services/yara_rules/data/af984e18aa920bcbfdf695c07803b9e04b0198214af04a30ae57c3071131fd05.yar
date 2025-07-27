rule auto_rule_20250726060359_0106 {
  strings:
    $o0 = "x4E61" wide ascii nocase
    $o1 = "dword_4285D7" wide ascii nocase
  condition:
    all of them
}