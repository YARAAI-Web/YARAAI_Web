rule auto_rule_20250726124039_3555 {
  strings:
    $o0 = "GetUserObjectSecurity" wide ascii nocase
    $o1 = "RealGetWindowClassA" wide ascii nocase
    $o2 = "cmdInsert" wide ascii nocase
  condition:
    3 of ($o*)
}