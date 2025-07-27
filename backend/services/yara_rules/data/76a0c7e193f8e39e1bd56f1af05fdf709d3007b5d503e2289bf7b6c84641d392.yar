rule auto_rule_20250726175303_4178 {
  strings:
    $o0 = "asc_419760" wide ascii nocase
    $o1 = "AVIStreamCreate" wide ascii nocase
  condition:
    all of them
}