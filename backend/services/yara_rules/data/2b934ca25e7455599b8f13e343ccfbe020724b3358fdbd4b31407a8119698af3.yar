rule auto_rule_20250727032706_5169 {
  strings:
    $o0 = "nModule" wide ascii nocase
    $o1 = "_getextendedkeycode" wide ascii nocase
    $o2 = "Client" wide ascii nocase
  condition:
    3 of ($o*)
}