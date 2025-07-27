rule auto_rule_20250727031409_3066 {
  strings:
    $o0 = "dword_1E77C" wide ascii nocase
  condition:
    all of them
}