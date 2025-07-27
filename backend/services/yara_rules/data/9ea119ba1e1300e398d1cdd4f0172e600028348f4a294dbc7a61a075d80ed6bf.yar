rule auto_rule_20250727031857_5233 {
  strings:
    $o0 = "dwInitParam" wide ascii nocase
    $o1 = "GetUserObjectSecurity" wide ascii nocase
  condition:
    all of them
}