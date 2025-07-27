rule auto_rule_20250727033245_7443 {
  strings:
    $o0 = "lpIconName" wide ascii nocase
    $o1 = "x17000u" wide ascii nocase
  condition:
    all of them
}