rule auto_rule_20250726113946_4703 {
  strings:
    $o0 = "dword_43641A" wide ascii nocase
  condition:
    all of them
}