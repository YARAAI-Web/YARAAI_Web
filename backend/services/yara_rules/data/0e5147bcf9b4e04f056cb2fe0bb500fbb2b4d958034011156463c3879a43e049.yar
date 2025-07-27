rule auto_rule_20250727043251_3738 {
  strings:
    $o0 = "Driver" wide ascii nocase
    $o1 = "dword_7F590" wide ascii nocase
  condition:
    all of them
}