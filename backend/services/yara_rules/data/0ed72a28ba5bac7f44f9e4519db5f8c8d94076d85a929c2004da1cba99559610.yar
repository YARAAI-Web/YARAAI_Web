rule auto_rule_20250727003952_2917 {
  strings:
    $o0 = "__tzset" wide ascii nocase
    $o1 = "aPrivateKeyWill" wide ascii nocase
    $o2 = "same" wide ascii nocase
  condition:
    3 of ($o*)
}