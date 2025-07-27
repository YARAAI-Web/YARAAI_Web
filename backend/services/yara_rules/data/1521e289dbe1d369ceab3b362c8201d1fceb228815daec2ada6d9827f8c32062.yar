rule auto_rule_20250726123939_7916 {
  strings:
    $o0 = "dword_4D014C" wide ascii nocase
  condition:
    all of them
}