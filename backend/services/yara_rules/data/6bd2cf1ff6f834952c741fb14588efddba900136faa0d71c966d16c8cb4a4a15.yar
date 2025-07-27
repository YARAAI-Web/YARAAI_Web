rule auto_rule_20250727012612_4009 {
  strings:
    $o0 = "TrailDown1" wide ascii nocase
    $o1 = "dword_411D9C" wide ascii nocase
  condition:
    all of them
}