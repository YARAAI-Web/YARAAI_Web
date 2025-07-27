rule auto_rule_20250727000845_3002 {
  strings:
    $o0 = "EnumWindowStationsA" wide ascii nocase
    $o1 = "lpwcx" wide ascii nocase
  condition:
    all of them
}