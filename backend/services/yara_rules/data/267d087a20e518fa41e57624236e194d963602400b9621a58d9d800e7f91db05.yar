rule auto_rule_20250726225941_6773 {
  strings:
    $o0 = "safely" wide ascii nocase
    $o1 = "dword_477100" wide ascii nocase
  condition:
    all of them
}