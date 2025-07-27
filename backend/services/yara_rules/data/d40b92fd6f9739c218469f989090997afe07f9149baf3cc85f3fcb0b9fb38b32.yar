rule auto_rule_20250727031622_6693 {
  strings:
    $o0 = "dword_411F0C" wide ascii nocase
    $o1 = "dword_411D74" wide ascii nocase
  condition:
    all of them
}