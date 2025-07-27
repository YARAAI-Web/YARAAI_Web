rule auto_rule_20250727003451_6020 {
  strings:
    $o0 = "dword_411D98" wide ascii nocase
  condition:
    all of them
}