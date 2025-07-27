rule auto_rule_20250727001030_0054 {
  strings:
    $o0 = "UnwindUp6_0" wide ascii nocase
    $o1 = "byte_40FA34" wide ascii nocase
    $o2 = "chsifnegret" wide ascii nocase
  condition:
    3 of ($o*)
}