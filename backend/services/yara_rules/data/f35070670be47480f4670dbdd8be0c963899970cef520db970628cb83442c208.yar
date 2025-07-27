rule auto_rule_20250727023948_6471 {
  strings:
    $o0 = "off_45C914" wide ascii nocase
  condition:
    all of them
}