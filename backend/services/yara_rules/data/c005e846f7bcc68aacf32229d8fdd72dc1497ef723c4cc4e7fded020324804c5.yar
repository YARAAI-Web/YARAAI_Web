rule auto_rule_20250726071018_3680 {
  strings:
    $o0 = "_commit" wide ascii nocase
    $o1 = "dword_45AF98" wide ascii nocase
  condition:
    all of them
}