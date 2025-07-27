rule auto_rule_20250727033952_5533 {
  strings:
    $o0 = "dword_64031354" wide ascii nocase
    $o1 = "isprint" wide ascii nocase
  condition:
    all of them
}