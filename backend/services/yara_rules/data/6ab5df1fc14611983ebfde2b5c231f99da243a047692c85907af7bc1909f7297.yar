rule auto_rule_20250726094248_0932 {
  strings:
    $o0 = "dword_781A4" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}