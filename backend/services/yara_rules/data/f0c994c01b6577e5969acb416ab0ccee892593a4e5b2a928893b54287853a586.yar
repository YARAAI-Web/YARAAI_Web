rule auto_rule_20250727033546_3337 {
  strings:
    $o0 = "CPtoLCID" wide ascii nocase
    $o1 = "dword_449AA0" wide ascii nocase
  condition:
    all of them
}