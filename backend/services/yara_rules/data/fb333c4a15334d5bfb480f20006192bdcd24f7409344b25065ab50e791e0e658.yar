rule auto_rule_20250727012946_1478 {
  strings:
    $o0 = "LibraryA" wide ascii nocase
    $o1 = "dword_45AA8C" wide ascii nocase
  condition:
    all of them
}